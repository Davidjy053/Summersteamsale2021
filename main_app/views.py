from django.shortcuts import render
from main_app.models import Sales
# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request,'about.html')

def index(request):
    sales = Sales.objects.all()
    return render(request, 'sales/index.html', { 'sales': sales })

def sale_detail(request, sales_id):
  sale = Sales.objects.get(id=sales_id)
  return render(request, 'sales/detail.html', { 'sale': sale })