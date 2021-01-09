from django.shortcuts import render
import requests


def home(request):
    cvbankas = requests.get("https://www.cvbankas.lt/?miestas=&padalinys%5B%5D=76&keyw=python")
    cvonline = requests.get("https://www.cvonline.lt/")
    cvbankas_status = cvbankas.status_code
    cvonline_status = cvonline.status_code
    cont = {'cvbankas_status': cvbankas_status, 'cvonline_status': cvonline_status}
    return render(request, 'base.html', context=cont)

