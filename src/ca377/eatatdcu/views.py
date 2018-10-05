from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from eatatdcu.models import Restaurant, Campus

def index(request):
    return render(request, 'eatatdcu/index.html')

def restaurants(request):
    query = request.GET.get('search', None)
    context = {}
    if query and request.method == 'GET':
        results = Restaurant.objects.filter(campus_id=query)
        context.update({'results': results})
        return render(request, 'eatatdcu/restaurants.html', context)
