from django.urls import path
from . import views

urlpatterns = [
    #path('home/', views.homepage, name='homepage'),
    path('', views.homepage, name='homepage'),
    path('signup/', views.signuppage, name='signuppage'),
    path('login/', views.loginpage, name='loginpage'),
    path('profile/', views.profilepage, name='profilepage'),
    path('create/', views.createeventpage, name='createeventpage'),
    path('detail/', views.detaileventpage, name='detaileventpage'),
    path('edit/', views.editeventpage, name='editeventpage'),
    path('register/', views.registereventpage, name='registereventpage'),
]