from django.http import HttpResponse
from django.shortcuts import render
def index(request):

    print("this is homepage")
    #return HttpResponse("welcome to homepage")

    return render(request,'home.html')