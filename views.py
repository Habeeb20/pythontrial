from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response
from .form import CustomerForm
from .models import *
from django.contrib import messages

# Create your views here.

class CustomerAPIView(APIView):
    def get(self,request):
        all=Customer.objects.all().values()
        return Response({"message":"List of Customers", "Customer list":all})


    
    def post(self,request):

        Customer.objects.Create(id=request.data["id"],
                                name=request.data["name"],
                                gender=request.data["gender"]    
                        
                                )
        Customer=Customer.objects.all().filter(id=request.data["id"]).values
        return Response({"message":"added", "Customer":Customer})




def add(request):
    return render(request, 'add.html')

def addcart(request):
    return render(request, 'addcart.html')

def delete(request):
    customer = Customer.object.get(id=id)
    customer.delete
    return render(request, "viewproduct.html")

def edit(request):
    customer = Customer.object.get(id=id)
    return render(request, "edit.html", {'customer': customer})

def listproduct(request):
    return render(request, "listproduct.html")

def login(request):
    if request.method == "POST":
    
         form = CustomerForm(request.POST or None),
         if form.is_valid():
            form.save
            message.success(request, ("you have successfully logged in"))
            return render(request, "viewproduct.html")
         else:
            return reverse(request, "signup.html")
    else:
        return render(request, ("login.html"))

    return render(request,'login.html')

def signup(request):
    if request.method == "POST":
        form = Customerdetails(request.POST or None),
        if form.is_valid():
            try:
                form.save
                return render(request, "viewproduct.html")
            except:
                pass
    else:
        form = Customerdetails
    return render(request, "signup.html", {'form':form})

   
def viewcart(request):
    return render(request, "viewproduct.html")

def viewproduct(request):
    return render(request, "viewproduct.html")
