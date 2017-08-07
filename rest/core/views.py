from django.shortcuts import render, HttpResponse
from rest_framework import authentication, permissions, viewsets

import requests, json

def index(request):    

    url = "https://api.github.com/users/philippe28/following"
    repos = json.loads(requests.get(url).text)
    return render(request, 'produto.html', {'git_list': repos})



