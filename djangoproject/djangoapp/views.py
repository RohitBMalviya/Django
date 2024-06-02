from django.shortcuts import render
from .models import ModelExample
from django.shortcuts import get_object_or_404

# Create your views here.

def djangoApp(request):
    examples = ModelExample.objects.all
    return render(request,"djangoapp/index.html",{'examples':examples})


def checkDesc(request,example_id):
    example = get_object_or_404(ModelExample,pk=example_id)
    return render(request,'djangoapp/description.html',{'example':example})


def checkPrice(request,example_id):
    example = get_object_or_404(ModelExample,pk=example_id)
    return render(request,"djangoapp/price.html",{'example':example})