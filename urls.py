
from django.urls import path,include
from . import views
from rest_framework import routers
from .views import UserViewSet,BookViewSet

router = routers.DefaultRouter()
router.register(r'Users', UserViewSet)
router.register(r'event',BookViewSet)



urlpatterns = [
    # path('', views.sign_in, name='sign_in'),
    path('router/', include(router.urls)),
    path('',views.userlogin,name='home'),
    path('sign-in/',views.userSignup,name='signIn'),
    path('login/',views.userlogin,name='login'),
    path('logout/',views.userlogut,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('delete/<int:id>/',views.deleteEvent,name='delete'),
    path('edit/<int:id>/',views.EditEvent,name='edit'),
    path('deleting/',views.deleting,name='delete'),
    path('profile/<int:id>/',views.Profile,name='profile'),
    path('PersonalEvents/',views.PersonalEvents,name='P_events'),
    path('addEvents/',views.FormCalender,name='add'),
    path('api-auth/', include('rest_framework.urls')),
    path('test/<int:id>/',views.Test,name='Test'),
    path('listCreate/',views.EventCreateList.as_view(),name='listCreate'),
    path('updateDestroy/<int:pk>/',views.EventUpdateDestroy.as_view(),name='updateDestroy'),


  
    # path('sign-out', views.sign_out, name='sign_out'),
    # path('auth-receiver', views.auth_receiver, name='auth_receiver'),
]

