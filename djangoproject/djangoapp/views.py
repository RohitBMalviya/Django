from django.shortcuts import render
from .models import ExampleVariety,ExampleStore
from django.shortcuts import get_object_or_404
from .forms import ExampleForm

# Create your views here.

def djangoApp(request):
    examples = ExampleVariety.objects.all
    return render(request,'djangoapp/index.html',{'examples':examples})


def checkDesc(request,example_id):
    example = get_object_or_404(ExampleVariety,pk=example_id)
    return render(request,'djangoapp/description.html',{'example':example})


def checkPrice(request,example_id):
    example = get_object_or_404(ExampleVariety,pk=example_id)
    return render(request,'djangoapp/price.html',{'example':example})


def exampleStore(request):
    stores = None
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            exampleVarietyform = form.cleaned_data['exampleVariety']
            stores = ExampleStore.objects.filter(exampleVarieties=exampleVarietyform)
    else:
        form = ExampleForm()

    return render(request,'djangoapp/exampleStore.html',{'stores':stores,'form':form})