
from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.FormCalender,name='home'),
    path('sign-in/',views.sign_in,name='signIn'),
    path('login/',views.userlogin,name='login'),
    path('logout/',views.userlogut,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('delete/<int:id>/',views.deleteEvent,name='delete'),
    path('edit/<int:id>/',views.EditEvent,name='edit'),
    path('deleting/',views.deleting,name='delete'),
    path('profile/<int:id>/',views.Profile,name='profile')
]