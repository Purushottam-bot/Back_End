from django.urls import path
from . import views

urlpatterns = [
     path('',views.MyView,name='help'),
     path('help/',views.MyView2,name='help'),
     path('user/',views.userPage,name='users')

]
