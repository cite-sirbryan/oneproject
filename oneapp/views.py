from django.shortcuts import render
from django.http import HttpResponse

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
            ]

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

def login_view(request):
    template = "main/navbar.html"
    context=None
    if request.method == 'POST':
        user = request.POST['username']
        password = request.POST['password']
        if user is not None:
            if user == "admin" and password == "123456":
                context = {'role': 'admin'}
            else:
                context = {'role': 'staff'}
                    
    return render(request, template, context)
