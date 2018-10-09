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
   results = Restaurant.objects.filter(campus_id__name__contains=campus)
   if len(results) == 0:
       #return HttpResponse('OK')
       return HttpResponse(template.render({'error_msg': 'nothing found for ' + campus}, request))
   return HttpResponse(template.render({'results': results}, request ))

