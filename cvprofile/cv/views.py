from django.shortcuts import render
from .models import CvStructure, Link
import requests


def home(request):
     # https://www.cvonline.lt/darbo-skelbimai/q-python/vilniaus
    #  "https://www.cvbankas.lt/?miestas=" + city + "&padalinys%5B%5D=76&keyw=python"
    links = Link.objects.all()
    city = CvStructure.objects.filter(name="Rolandas")[0].city
    technology = CvStructure.objects.filter(name="Rolandas")[0].technology
    print(city, technology, links)
    updated_links = []
    for link in links:
        print('15', link.link)
        if link.link == 'https://www.cvbankas.lt/':
            temp_link = link.link + '?miestas=' + city + '&keyw=' + technology
            # data gathering layer
            resp = requests.get(temp_link)
            status_code = resp.status_code
            updated_links.append({'status': status_code, 'link': temp_link})
        if link.link == 'https://www.cvonline.lt/darbo-skelbimai/q-':
            city_map = {'Vilnius': 'vilniaus'}
            temp_link = link.link + technology.lower() + '/' + city_map[city]
            resp = requests.get(temp_link)
            status_code = resp.status_code
            updated_links.append({'status': status_code, 'link': temp_link})
    cont = {'info': updated_links}
    return render(request, 'base.html', context=cont)

