from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from eatatdcu.models import Restaurant, Campus

def index(request):
    template = loader.get_template('eatatdcu/index.html')
    return HttpResponse(template.render({},request))

def restaurants(request):
   template = loader.get_template('eatatdcu/restaurants.html')
   campus = str(request.GET.get('campus'))
   results = Restaurant.objects.filter(campus_id__name__iexact=campus)
   campuslist = Campus.objects.filter(name__iexact=campus)
   if len(campuslist) == 0:
       return HttpResponse('No such campus')
   if len(results) == 0:
       return HttpResponse('No restaurants found')
   return HttpResponse(template.render({'results': results}, request ))

