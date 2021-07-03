from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def about(request):
    return render(request,'about.html')
def index(request):
    sales = [
        {'name':'ARK: Survival Evolved', 'ogprice':'CDN$ 33.99', 'percentage':'-67%','afprice':'CDN$ 11.21'},
        {'name':'Dont Starve Together', 'ogprice':'CDN$ 16.99', 'percentage':'-66%','afprice':'CDN$ 5.77'},
        {'name':'PAYDAY 2', 'og-price':'CDN$ 11.49', 'percentage':'-90%','af-price':'CDN$ 1.14'},
        {'name':'Gunfire Reborn', 'ogprice':'CDN$ 13.49', 'percentage':'-21%','afprice':'CDN$ 10.65'},
        {'name':'DARK SOULS III', 'ogprice':'CDN$ 66.49', 'percentage':'-75%','afprice':'CDN$ 16.62'},
        {'name':'Sea of Thieves', 'ogprice':'CDN$ 49.99', 'percentage':'-33%','afprice':'CDN$ 33.49'},
        {'name':'The Sims™ 4', 'og-price':'CDN$ 39.99', 'percentage':'-88%','af-price':'CDN$ 4.79'},
        ]
    return render(request, 'sales/index.html', { 'sales': sales })