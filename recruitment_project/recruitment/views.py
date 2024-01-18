from django.shortcuts import render, redirect
from .models import Applicant
import csv
from recruitment.models import Applicant
import os

# Create the full file path using os.path.join

csv_file_path = os.path.join('recruitment', 'csvfiles', 'iq.csv')

def recruitment_form(request):
    cities = []

    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  
        for row in csv_reader:
            cities.append(row[0])
    print(cities)
    if request.method == 'POST':
        fname = request.POST.get('fname')        
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone_number')
        introduction = request.POST.get('introduction')
        age = request.POST.get('age')
        city= request.POST.get('city')
        study = request.POST.get('study')
        degree = request.POST.get('degree')
        experience = request.POST.get('experience')
        photo = request.FILES['imge']
        resume = request.FILES['resume']

        # Create a new Applicant object and save it to the database
        applicant = Applicant(
            fname=fname,
            lname=lname,
            email=email,
            phone=phone,
            introduction=introduction,
            age=age,
            city=city,
            study=study,
            degree=degree,
            experience=experience,
            photo=photo,
            resume=resume
        )
        applicant.save()

        # You can redirect to a thank you page or any other page after submission
        return redirect('thank')

    return render(request, 'recruitment_form.html',{'cities': cities})
def thank(request):
    return render(request, 'thank.html')

def dashboard(request):
    data = Applicant.objects.all()  # Retrieve all instances of MyModel
    return render(request, 'dashboard.html', {'data': data})

