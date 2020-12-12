from django.db import models
import uuid
from django.core.validators import RegexValidator,MinValueValidator,MaxValueValidator, FileExtensionValidator
from unixtimestampfield.fields import UnixTimeStampField

# Create your models here.

# class Login(models.Model):
#     username = models.CharField(max_length=200)
#     pasword = models.CharField(max_length=200)


class Candidate(models.Model):
    tsync_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, max_length=55)
    name = models.CharField(max_length=256, blank=False)
    email = models.EmailField(max_length=256, blank=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$', message="Phone number must be entered in the format: '+999999999'")
    phone = models.CharField(validators=[phone_regex], max_length=14, blank=False)
    full_address = models.CharField(max_length=512, null=True, blank=True)
    name_of_university = models.CharField(max_length=256, blank=False)
    graduation_year = models.PositiveIntegerField(validators=[MinValueValidator(2015),
                                       MaxValueValidator(2020)], blank=False)
    cgpa = models.FloatField(validators=[MinValueValidator(2.0),
                                       MaxValueValidator(4.0)], blank=True)
    experience_in_months = models.PositiveIntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(100)], blank=True)
    current_work_place_name = models.CharField(max_length=256, blank=True)
    applying_in = models.CharField(max_length=200)
    expected_salary = models.PositiveIntegerField(validators=[MinValueValidator(15000),
                                       MaxValueValidator(60000)], blank=False)
    field_buzz_reference = models.CharField(max_length=256, blank=True)
    github_project_url = models.URLField(max_length=512, blank=False)
    my_file = models.FileField(upload_to='files/',null=True, blank=False, validators=[FileExtensionValidator(['pdf'])])
    # cv_file_tsync_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, max_length=55)
    on_spot_update_time = UnixTimeStampField(auto_now=True)
    on_spot_creation_time = UnixTimeStampField(auto_now_add=True)
