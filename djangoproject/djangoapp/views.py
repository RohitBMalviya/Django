from django.shortcuts import render

# Create your views here.

def djangoApp(request):
    return render(request,"djangoapp/index.html")