from django.shortcuts import render, redirect
import json
import requests
# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import CandidateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


@csrf_exempt
def home(request):
    if request.method == 'POST':
        data = request.POST
        username = data['username']
        password = data['password']
        url = 'https://recruitment.fisdev.com/api/login/'
        headers={'Content-type':'application/json', 'Accept':'application/json'}
        payload = { 
            'username': username,
            'password': password
        }
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        data = json.loads(r.content)
        if r.status_code == 200:
            token = data['token']
            return redirect('/profile/')
        else:
            msg_dict = {'msg': 'Login Failed. Wrong Username Or Password.'}
            return render(request, 'login/home.html', {'msg_dict': msg_dict})
    else:
        return render(request, 'login/index.html')

@csrf_exempt
def profile(request):
    form = CandidateForm()
    if request.method == 'POST':
        data = request.POST
        payload = json.dumps(data)
        data_dict = json.loads(payload)
        f = CandidateForm(request.POST, request.FILES)
        if f.is_valid():
            user = f.save()
            tsync_id = int(user.tsync_id)
            dc = {'cv_file' : {'tsync_id': tsync_id}}
            data_dict.update(dc)
            payload = json.dumps(data_dict)
            url = 'https://recruitment.fisdev.com/api/v0/recruiting-entities/'
            headers={'Content-type':'application/json', 'Accept':'application/json', 'Authorization': 'Token b197d0a02035d16416b1757d6989f8c21eb9eb04'}
            r = requests.post(url, data=payload, headers=headers)
            response_data = json.loads(r.content)
            print(response_data)
            cv_file_id = response_data['cv_file']['id']
            cv_upload(cv_file_id, user)
            return HttpResponse("Profile Updated Successfully.")
        else:
           return render(request, 'login/profile.html',{'form': f})
    return render(request, 'login/profile.html', {'form': CandidateForm})


def cv_upload(cv_file_id, user):
    url = "https://recruitment.fisdev.com/api/file-object/" + str(cv_file_id) + "/"
    headers={'Accept':'application/json', 'Authorization': 'Token b197d0a02035d16416b1757d6989f8c21eb9eb04'}
    file_path = user.my_file.path
    up = {'file': (file_path, open(file_path, 'rb'), "multipart/form-data")}
    r = requests.put(url, files=up, headers=headers)
    print(r.content)
        
