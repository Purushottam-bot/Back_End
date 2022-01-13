from django.shortcuts import render
from django.http import HttpResponse

def Welcome(request):
    my_dict={'insert_me':"Hello Friends Chai Pilo!"}

    return render(request,'first_app/index.html',context=my_dict)

# Create your views here.
