from django.shortcuts import render
from . models import *

# Create your views here.
def user_registeration(request):
    if request.method=="POST":
        username=request.POST.get("username")
        useremail=request.POST.get("useremail")
        usermobile=request.POST.get("usermobile")
        userpassword=request.POST.get("userpassword")
        data=Userdetailss(username=username,useremail=useremail,usermobile=usermobile,userpassword=userpassword)
        data.save()
    return render(request,'user_registeration.html')

def user_login(request):
    useremail = request.POST.get('useremail')
    userpassword = request.POST.get('userpassword')
    if useremail == 'admin@gmail.com' and userpassword =='admin':
        request.session['adminemail'] = useremail
        request.session['admin'] ='admin'
        return render(request,'index.html',{'status': 'admin login successfull'} )
 
    elif Userdetailss.objects.filter(useremail=useremail,userpassword=userpassword).exists():
        udet=Userdetailss.objects.get(useremail=request.POST['useremail'],userpassword=userpassword)
        if udet.userpassword == request.POST['userpassword']:
            request.session['uid'] = udet.id
            request.session['uname'] = udet.username
            request.session['uemail'] = useremail
            request.session['user'] = 'user'
            return render(request,'index.html',{'status': 'user login successfull'})
 
    else:
            return render(request, 'user_login.html', {'status': 'incorrect credentials'})
    
def search_car(request):
    return render(request,'search_car.html')   
    
