import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fbvProject1.settings')
django.setup()
from faker import Faker
from myApp.models import Student
f=Faker()
def populate(n):
    for i in range(n):
        fname=f.name()
        fusn=f.random_int(min=1,max=20)
        fsub=f.random_int(min=6, max=10)
        fmarks=f.random_int(min=1,max=100)
        femail=f.email()
        faddr=f.address()
        s=Student.objects.get_or_create(name=fname,usn=fusn,subjects=fsub,marks=fmarks,email=femail,address=faddr)
populate(30)
