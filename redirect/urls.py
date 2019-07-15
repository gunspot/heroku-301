from django.contrib import admin
from django.urls import path, re_path
from django.shortcuts import redirect

# Get domain
from .domain import redirect_domain



def redirect_view(request):
    response = redirect('https://'+redirect_domain)
    response.status_code = 301
    return response


urlpatterns = [
    re_path('.*', redirect_view)
]
