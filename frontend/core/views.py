from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render,redirect
import requests


# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)

def admin(request):
    api_url = "http://api:8000/api/v1/item/"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        
        context = {'data' : response.json()}

        return render(request, 'admin.html', context)
    
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)

def add(request):
    if request.method=='POST':
        
        api_url = "http://api:8000/api/v1/item/"
        payload = {
            "name": request.POST.get('name'),
            "description": request.POST.get('description'),
            "stock": request.POST.get('stock')
        }
        
        try:
            response = requests.post(api_url, json=payload)
            response.raise_for_status()
            data = response.json()
            
            messages.success(request, f'The item {request.POST.get("name")}, has been added successfully')
            
            return redirect('add')
            # return JsonResponse(data, status=response.status_code)
            
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
        
    return render(request, 'add.html')

def edit(request, id):
    api_url = "http://api:8000/api/v1/item/"+str(id)+"/"
    
    if request.method=='POST':
        
        payload = {
            "id": id,
            "name": request.POST.get('name'),
            "description": request.POST.get('description'),
            "stock": request.POST.get('stock')
        }
        
        try:
            response = requests.put(api_url, json=payload)
            response.raise_for_status()
            data = response.json()
            
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
        
        messages.success(request, f'Edit has been made successfully')
        return redirect('administrator')
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        
        context = {'data': data}
        
        return render(request, 'edit.html', context)
        
    except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
        
def delete(request, id):
    api_url = "http://api:8000/api/v1/item/"+str(id)+'/'
    
    try:
        response = requests.delete(api_url)
        response.raise_for_status()
        messages.success(request, f'Item has been deleted successfully')
        
        return redirect('administrator')
        
    except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
        
def customer(request):
    api_url = "http://api:8000/api/v1/item/"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        
        context = {'data' : response.json()}

        return render(request, 'customer.html', context)
    
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)

def buy(request, id):
    api_url = "http://api:8000/api/v1/item/"+str(id)+"/"
    
    if request.method=='POST':
        payload = {
            "id": id,
            "stock": request.POST.get('stock')
        }
        
        current_stock = requests.get(api_url)
        current_stock.raise_for_status()
        current_stock = int(current_stock.json()['stock'])
        
        new_stock = current_stock - int(payload['stock'])
        payload['stock'] = new_stock
        
        try:
            response = requests.patch(api_url, json=payload)
            response.raise_for_status()
            
            messages.success(request, f'Thank you for your purchase')
            return redirect('customer')
        
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        
        context = {'data': data}
        
        return render(request, 'buy.html', context)
    
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)