from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(input):

    return HttpResponse("<em>My second project</em>")

def index1(request):
    # return HttpResponse("<em>HELP</em>")

    helpdict={'help_ack':'HELP AA GYI BETA'}
    return render(request,'appTwo/random.html',context=helpdict)
