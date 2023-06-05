from django.urls import path
from signinout import views

urlpatterns = [ 
    path('',views.index),
    path('login/',views.loginUser),
    path('signup/',views.signup),
    path('logout/',views.logoutUser),
    path('project/',views.project),
    path('chats/',views.chats),
    path('profile/',views.profile),
]