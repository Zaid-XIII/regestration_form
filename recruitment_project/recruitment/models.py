from django.db import models
import csv
class Applicant(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255,null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=32)
    introduction = models.CharField(max_length=100)
    age = models.FloatField()
    CITY_CHOICES = []
    with open('recruitment/csvfiles/iq.csv', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  
        for row in csv_reader:
            CITY_CHOICES.append((row[0], row[0]))

    city = models.CharField(max_length=100, default='Unknown', choices=CITY_CHOICES)

    study = models.CharField(max_length=255)
    DEGREE_CHOICES = [
        ('Undergradute', 'Undergradute'),
        ('Bachelor', 'Bachelor'),
        ('Master', 'Master'),
        ('Ph.D.', 'Ph.D.'),
    ]
    
    degree = models.CharField(max_length=20, choices=DEGREE_CHOICES)
    experience = models.FloatField()
    photo = models.ImageField(upload_to='photos/')
    resume = models.FileField(upload_to='resumes/')

