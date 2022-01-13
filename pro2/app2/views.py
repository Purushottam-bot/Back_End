from django.shortcuts import render
from django.http import HttpResponse
from app2.models import User
# Create your views here.
def MyView(request):
    var = HttpResponse("<em>My Second App!</em>")
    return var

def MyView2(request):

    my_dict = {'insert_me':"Help page from views.py"}
    return render(request,'app2/index.html',context = my_dict)

def userPage(request):

    user_list = User.objects.order_by('first_name')
    user_dict = {'users' :user_list}
    return render(request,'app2/users.html',context = user_dict)
