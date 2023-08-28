from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here
def main_page(request):

    return render(request,"main.html")

def registration(request):
     
     if request.method == 'POST':
           name = request.POST.get('name')    
           email = request.POST.get('email')  
           address = request.POST.get('Address')  
           age = request.POST.get('age')    
           phno = request.POST.get('phno')
           pas = request.POST.get('pass')     
           repass = request.POST.get('repass')

           if pas == repass:

                user = User.objects.filter(username=name)
                isuser = user.exists()
                if isuser is False:
                      new_user = User.objects.create_user(username=name,email=email,password=pas)
                      new_user.save()

                      Customer(
                           connection=new_user,
                           name=name,
                           email=email,
                           age=age,
                           address=address,
                           phone_number =phno
                           
                      ).save()

                      authuser = authenticate(username=name,password=pas)
                      login(request,authuser)
                     
                      return redirect('/')
           else:
                 return HttpResponse("password Does not match ")  
     else:
          
        return render(request,"registration.html")

def login_(request):
      
      if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('pass')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return HttpResponse("Wrong password")
      return render(request,'login.html')
     
def locationpage(request):

    location = Location.objects.all()


    return render(request,"locationpage.html",{"loc":location})

def view_hotel(request,id):

    location = Location.objects.get(id=id)

    hotels = Hotels.objects.filter(Select_location=location)

    return render(request,"view_hotel.html",{"ho":hotels})


def hotel_details(request,id):

    hotel = Hotels.objects.get(id=id)

    
    return render(request,"hotel_details.html",{"ho":hotel})

def booking(request):
   
   if request.user.is_authenticated:
        
           user_id = request.user.id

           user = User.objects.get(id=user_id)

           customer = Customer.objects.get(connection=user)

           sdate = request.POST.get('sdate') 
           edate = request.POST.get('edate')
           days = request.POST.get('days')
           rupees = request.POST.get('rupees')
           id = request.POST.get('id')

           hotel = Hotels.objects.get(id=id)

           Bookings(
                hotel=hotel,
                user=customer,
                start_date = sdate,
                end_date=edate,
                number_of_days=days,
                total_amount_paid=rupees
           ).save()
       
           return redirect("/")
       
       
   else:
        return redirect("/login_")
       
def mybookings(request):
     
      user_id = request.user.id

      user = User.objects.get(id=user_id)

      customer = Customer.objects.get(connection=user)

      hotels = Bookings.objects.filter(user=customer)
     
      return render(request,"mybooking.html",{"ho":hotels})    


def delete_my_bookings(request,id):
     
     Bookings.objects.get(id=id).delete()

     return redirect("/mybookings")

def Logout_(request):
       logout(request)
       return redirect("/")
  
  