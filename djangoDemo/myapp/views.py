from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    # return HttpResponse("Welcome to the Home Page!")
    return render(request,"home.html", {"title":"数字列表","list":[1,2,3,4]} )
def about(request,index,name):

    # return HttpResponse("Welcome to the About Page!",{"a":1})
    return render(request,"about.html", {"index":index , "name":name} )
