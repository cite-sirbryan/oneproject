from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
# def index(request):
#     return HttpResponse("<h1>Philippine Trip</h1>")

def index(request):
    template = "main/base.html"
    context = {
        "product" : [ 
                {   
                    "id" : "123",
                    "name" : "Iphone 13 Pro Max",
                    "desc" : "Smart Phone",
                    "price" : "80000",
                    "feature" : ["20MP Camera", "4GB RAM", "12MP Front Camera"],
                } , 
                {   
                    "id" : "124",
                    "name" : "Iphone 13",
                    "desc" : "Smart Phone",
                    "price" : "50000",
                    "feature" : ["12MP Camera", "4GB RAM", "8MP Front Camera"],
                } , 
                {
                    "id" : "125",
                    "name" : "Iphone 14 Pro Max",
                    "desc" : "Smart Phone",
                    "price" : "90000",
                    "feature" : ["20MP Camera", "4GB RAM", "18MP Front Camera"],
                
                } 
            ],

        "number": 70,

        "user" : "Teacher",

        "Message": "The quick brown fox jumps over the lazy dog",

        "notification": 0,

        "listofnames" : ["Mark", "Jonah", ["Josie", "Jessie", "Jenny"],"David"],

        "datenow": datetime.datetime.now(),


        # "id" : "123",
        # "name" : "Iphone 13 Pro Max",
        # "desc" : "Smart Phone",
        # "price" : "80000",
        # "feature" : ["20MP Camera", "4GB RAM", "12MP Front Camera"],
    }
    return render(request, template, context)



def aboutme(request):
    template = "main/aboutme.html"
    context = {
        "name": "Bryan Dadiz",
        "address": "QC"
    }

    return render(request, template, context)

def bootstrap(request):
    template = "main/boot`strap.html"

    return render(request, template)