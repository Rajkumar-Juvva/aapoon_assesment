from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
import csv
from .models import TeachersInformation

# Create your views here.

class TeacherDataUpload(View):
    def get(self,request):
        return render(request,'file_upload.html',locals())
    
    def post(self,request):
        message = "File updoad success"
        duplicate_email_count = 0
        success_data_count = 0
        duplicate_email_data = []
        file = request.FILES['file'] 
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        existing_emails = list(TeachersInformation.objects.values_list("email_address",flat=True))
        for row in reader:
            subjects = row.get('Subjects taught','').split(',')[:5]
            email = row.get("Email Address",'')
            if email in existing_emails:
                duplicate_email_count+=1
                duplicate_email_data.append(row)
                continue
            existing_emails.append(email)
            TeachersInformation.objects.create(
                    first_name = row.get("First Name",""),
                    second_name = row.get("Last Name",""),
                    profile_picture = row.get("Profile picture",""),
                    email_address = email,
                    phone_number = row.get("Phone Number",""),
                    room_number = row.get("Room Number",""),
                    subjects_taught = ','.join(subjects)
            )
            success_data_count+=1
        if duplicate_email_count>0:
            message = f"{success_data_count} rows added successfully <br> {duplicate_email_count} duplicate email rows found<br>{duplicate_email_data}"
        return render(request,'file_upload.html',locals())

class TeacherInformation(View):
    def get(self,request):
        data = TeachersInformation.objects.all()
        return render(request,'teacher_dashboard.html',locals())

class TeacherDetails(View):
    def get(self,request,id = None):
        data = TeachersInformation.objects.filter(id = id).all()

        return render(request,'teacher_details.html',locals())