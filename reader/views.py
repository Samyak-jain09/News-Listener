from django.shortcuts import render
from newsapp import settings
import requests
from django.http import HttpResponse
import json
from django.http import JsonResponse
from urllib.parse import unquote


# Create your views here.


def home(request):
    page = request.GET.get('page', 1)
    search = request.GET.get('search', None)

    if search is None or search == "top":
        # get the top news
        url = "https://newsapi.org/v2/top-headlines?country={}&page={}&apiKey={}".format(
            "us", 1, settings.APIKEY
        )
    else:
        # get the search query request
        url = "https://newsapi.org/v2/everything?q={}&sortBy={}&page={}&apiKey={}".format(
            search, "popularity", page, settings.APIKEY
        )
    r = requests.get(url=url)

    data = r.json()

    if data["status"] != "ok":
        return HttpResponse("<h1>Request Failed</h1>")
    data = data["articles"]
    context = {
        "success": True,
        "data": [],
        "search": search
    }
    # seprating the necessary data
    for i in data:
        context["data"].append({
            "title": i["title"],
            "description":  "" if i["description"] is None else i["description"],
            "url": i["url"],
            "image":  i["urlToImage"],
            "publishedat": i["publishedAt"],
            "author": "News" if i["author"] is None else i["author"],
        })
    

    
    # send the news feed to template in context
    return render(request, 'index.html', context=context)



