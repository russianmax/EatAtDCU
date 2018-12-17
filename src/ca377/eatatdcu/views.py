from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Restaurant,Campus

import json,requests


def index(request):
    # index.html as a template
    template = loader.get_template('eatatdcu/index.html')
    return HttpResponse(template.render({},request))

def restaurants(request):
    # restaurants.html as a template
    template = loader.get_template('eatatdcu/restaurants.html')
	# get campus_name from user input in restaurants.html
    campus_name = request.GET.get('campus','').lower()
    try:
        campus = Campus.objects.get(name=campus_name)
		# filter restaurants based on campus_id and if is_restaurant = True
        restaurants = Restaurant.objects.filter(campus_id=campus,is_restaurant=True)
		# filter cafes based on campus_id and if is_restaurant = False
        cafes = Restaurant.objects.filter(campus_id=campus,is_restaurant=False)
    except Restaurant.DoesNotExist:
		# if restaurant doesn't exist return error message
        return HttpResponse(template.render({'error':'No such restaurant'},request))
    except Campus.DoesNotExist:
		# if campus doesn't exist return error message
        return HttpResponse(template.render({'error':'No such campus'},request))
		# return results for restaurants and cafes, two separate lists
    return HttpResponse(template.render({'restaurants':restaurants,'cafes':cafes},request))


def specials(request,restaurant):
    # specials.html as a template
    template = loader.get_template('eatatdcu/specials.html')
	# call the webservice from pythonanywhere
    webservice_url = 'http://jfoster.pythonanywhere.com/specials/'+restaurant
    real_time_info = requests.get(webservice_url).json()
    if 'error_msg' in real_time_info:
	   # if error, return error message
       return HttpResponse(template.render({'error':real_time_info['error_msg']},request))
    else:
	   # return the results in specials.html
       return HttpResponse(template.render(real_time_info,request))



