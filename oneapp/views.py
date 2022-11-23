from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from .forms import ItemForm

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
    template = "main/bootstrap.html"
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
    }

    return render(request, template,context)

def item(request):
    template = "main/item.html"

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ItemForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            return HttpResponseRedirect('/oa/bootstrap')  
            #return redirect('oneapp:bootstrap') #! this is optional of we use namespaces for 
                                              #! our app
    
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ItemForm()
    
    context = {
        'form_key': form     #! ----- >  this is to be used on our template
    } 

    return render(request, template, context)