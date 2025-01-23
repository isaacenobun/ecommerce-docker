from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render,redirect
import requests


# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)

def admin(request):
    api_url = "http://0.0.0.0:8000/api/v1/item/"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        
        context = {'data' : response.json()}

        return render(request, 'admin.html', context)
    
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)

def add(request):
    if request.method=='POST':
        
        api_url = "http://0.0.0.0:8000/api/v1/item/"
        payload = {
            "name": request.POST.get('name'),
            "description": request.POST.get('description'),
            "stock": request.POST.get('stock')
        }
        
        try:
            response = requests.post(api_url, json=payload)
            response.raise_for_status()
            data = response.json()
            
            messages.success(request, f'The item {request.POST.get("name")}, has been added successsfully')
            
            return redirect('add')
            # return JsonResponse(data, status=response.status_code)
            
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
        
    return render(request, 'add.html')

def customer(request):
    api_url = "http://0.0.0.0:8000/api/v1/item/"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        
        context = {'data' : response.json()}

        return render(request, 'customer.html', context)
    
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)

def buy(request):
    if request.method=='POST':
        
        return redirect('customer')
    
    context = {}
    return render(request, 'buy.html', context)