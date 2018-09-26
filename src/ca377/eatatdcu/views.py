from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('eatatdcu/index.html')
    return HttpResponse(template.render({},request))
def restaurants(request):
   return render(request, 'eatatdcu/restaurants.html')

