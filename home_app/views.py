from django.shortcuts import render
from .models import product
# Create your views here.
def home(request):
    a=product.objects.all()
    return render(request,"index.html",{"product":a})