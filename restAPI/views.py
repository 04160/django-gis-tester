from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


def index(request):
    return JsonResponse(data={'body': "rest API index"})
