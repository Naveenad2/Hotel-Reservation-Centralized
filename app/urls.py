from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.main_page,name='main_page'),
    path('locationpage',views.locationpage,name='locationpage'),

    path('login_',views.login_,name='login_'),
    path('register',views.registration,name='registration'),

    path('view_hotel/<int:id>',views.view_hotel,name='view_hotel'),
    path('hotel_details/<int:id>',views.hotel_details,name='view_hotel_detailshotel'),
    path('booking',views.booking,name='booking'),
    path('mybookings',views.mybookings,name='mybookings'),
    path('delete_my_bookings/<int:id>',views.delete_my_bookings,name='delete_my_bookings'),

    path('logout',views.Logout_,name="Logout_"),
   
]