from django.http.response import HttpResponse
from django.shortcuts import render
import requests
from django.http import JsonResponse
import json
# Create your views here.


def home(request):
    headers = {"Ocp-Apim-Subscription-Key": "9501613007cd41398976a63b0a5bd925",
               "Access-Control-Allow-Origin": "*"}

    getStations = requests.request('GET',
                                   "https://gateway.apiportal.ns.nl/reisinformatie-api/api/v2/stations", headers=headers)

    print(getStations.request.headers)

    return JsonResponse(getStations.json(), safe=False)


def index(request):
    return HttpResponse("<h1>{request}</h1>")

# https://gateway.apiportal.ns.nl/reisinformatie-api/api/v2/stations
