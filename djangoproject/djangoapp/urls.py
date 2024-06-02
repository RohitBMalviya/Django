from django.urls import path
from . import views
urlpatterns = [
    path("",views.djangoApp,name="djangoApp"),
    path("description/<int:example_id>",views.checkDesc,name="checkDesc"),
    path("prices/<int:example_id>",views.checkPrice,name="checkPrice"),
]