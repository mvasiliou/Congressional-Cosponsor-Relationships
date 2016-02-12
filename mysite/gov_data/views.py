from django.shortcuts import render
from django.http import HttpResponse
from .models import Bill, Senator
from django.template import loader
# Create your views here.

def index(request):
    template = loader.get_template('gov_data/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def bills_index(request):
    bill_list = Bill.objects.order_by('title')
    template = loader.get_template('gov_data/bills_index.html')
    context = {'bill_list': bill_list, }
    return HttpResponse(template.render(context, request))

def bill_detail(request, bill_id):
    return HttpResponse("You're looking at bill %s." % bill_id)

def senators_index(request):
    senator_list = Senator.objects.order_by('last')
    template = loader.get_template('gov_data/senators_index.html')
    context = {'senator_list': senator_list, }
    return HttpResponse(template.render(context, request))

def senator_detail(request, id):
    return HttpResponse("You're looking at Senator %s" % id)