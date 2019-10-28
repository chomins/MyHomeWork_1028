from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request,"Home.html")

def about(request):
    return render(request,"about.html")

def result(request):
    full=request.GET['fulltext']
    num=len(full)-10
    return render(request,"result.html",{'length':num})

