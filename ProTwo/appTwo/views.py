from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(input):

    return HttpResponse("<em>My second project</em>")
