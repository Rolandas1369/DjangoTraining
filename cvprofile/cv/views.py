from django.shortcuts import render
from .models import CvStructure
import requests


def home(request):
    obj = CvStructure.objects.get()
    rolandas = obj.order_by('city')
    print(rolandas)

    cvbankas = requests.get("https://www.cvbankas.lt/?miestas=&padalinys%5B%5D=76&keyw=python")
    cvonline = requests.get("https://www.cvonline.lt/")
    cvbankas_status = cvbankas.status_code
    cvonline_status = cvonline.status_code

    # obj = CvStructure.objects.create(name="Rolandas3", city="Vilnius", job_description="none")
    #
    # print(obj)

    cont = {'statuses': [cvbankas_status, cvonline_status]}
    return render(request, 'base.html', context=cont)

