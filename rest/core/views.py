from django.shortcuts import render, HttpResponse
from rest_framework import authentication, permissions, viewsets

import requests

def index(request):    

    
    parsedData = []
   
    req = requests.get('https://api.github.com/users/philippe28/following')
    jsonList = []
    jsonList.append(req.json())
    userData = {}
    login = []
    avatar_url = []
    html_url = []
    repos_url = []
    url = []
    bio = []
    location = []

    item = {}
    for data in jsonList:
        item = data

        for items in data:            
            login.append(items['login'])
            avatar_url.append(items['avatar_url'])
            html_url.append(items['html_url'])
            repos_url.append(items['repos_url'])

            #req_user = requests.get(items['url'])
            #jsonList_user = []
            #jsonList_user.append(req_user.json())
            
            #user_list = jsonList_user[0]
            #bio.append(user_list['bio'])
            #location.append(user_list['location'])
            



    userData['login'] = login
    userData['avatar_url'] = avatar_url
    userData['html_url'] = html_url
    userData['repos_url'] = repos_url
    #userData['bio'] = bio
    #userData['location'] = location

    parsedData.append(userData)

    return render(request, 'produto.html', {'git_list': item})


