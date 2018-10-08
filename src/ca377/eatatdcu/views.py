from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from eatatdcu.models import Restaurant, Campus

def index(request):
    template = loader.get_template('eatatdcu/index.html')
    return HttpResponse(template.render({},request))

def restaurants(request):
   template = loader.get_template('eatatdcu/restaurants.html')
   query = request.GET.get('search')
   results = Restaurant.objects.filter(campus_id__name__icontains=query)
   return HttpResponse(template.render({'results': results}, request ))

