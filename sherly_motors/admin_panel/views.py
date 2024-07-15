from django.shortcuts import render,redirect
from . models import *


# Create your views here.
def add_car(request):
    if request.method=="POST":
        carname=request.POST.get("carname")
        carmodel=request.POST.get("carmodel")
        caryear=request.POST.get("caryear")
        carprice=request.POST.get("carprice")
        carmlg=request.POST.get("carmlg")
        carphoto=request.FILES["carphoto"]
        data=cardetails(carname=carname,carmodel=carmodel,caryear=caryear,carprice=carprice,carmlg=carmlg,carphoto=carphoto)
        data.save()
    return render(request,'add_car.html')

def admin_carviews(request):
    data=cardetails.objects.all()
    return render(request,'admin_carviews.html',{'result':data})


def cardelete(request,id):
    m=cardetails.objects.get(pk=id)
    m.delete()
    return redirect(admin_carviews)

def carupdate(request,id):
    data=cardetails.objects.get(pk=id)
    return render(request,'car_update.html',{'result':data})

def car_update(request,id):
    if request.method=="POST":
        carname=request.POST.get("carname")
        carmodel=request.POST.get("carmodel")
        caryear=request.POST.get("caryear")
        carprice=request.POST.get("carprice")
        carmlg=request.POST.get("carmlg")
        carphoto=request.FILES["carphoto"]
        data=cardetails(carname=carname,carmodel=carmodel,caryear=caryear,carprice=carprice,carmlg=carmlg,carphoto=carphoto,id=id)
        data.save()
        return redirect(admin_carviews)
    return render(request,'car_update.html')

def user_carviews(request):
    data=cardetails.objects.all()
    return render(request,'user_carviews.html',{'result':data})

