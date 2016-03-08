from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Bill, Senator, Cosponsorship, Leadership
from django.template import loader
# Create your views here.

def index(request):
    return render(request, 'gov_data/index.html')
    
def bills_index(request, bill_range = '1'):
    bill_range = int(bill_range)
    end = 25 * bill_range
    start = end - 25
    bill_list = Bill.objects.order_by('title')[start:end]
    next = str(bill_range + 1)
    if bill_range != 1:
        last = str(bill_range - 1)
    else:
        last = '1'
    context = {'bill_list': bill_list, 'start':start, 'end':end, 'next': next, 'last': last}
    return render(request, 'gov_data/bills_index.html', context)
   
def bill_detail(request, bill_id):
    bill = Bill.objects.get(pk = bill_id)
    sponsor = Senator.objects.get(pk = str(bill.sponsor_id))
    cosponsor_actions = Cosponsorship.objects.filter(bill = bill_id)
    cosponsor_list = []
    for cosponsorship in cosponsor_actions:
        senator = Senator.objects.get(pk = str(cosponsorship.cosponsor))
        cosponsor_list.append(senator)
    context = {'bill': bill, 'sponsor': sponsor, 'cosponsor_list': cosponsor_list}
    return render(request, 'gov_data/bill_detail.html', context)

def senators_index(request):
    senator_list = Senator.objects.order_by('last')
    template = loader.get_template('gov_data/senators_index.html')
    context = {'senator_list': senator_list, }
    return HttpResponse(template.render(context, request))

def senator_detail(request, senator_id):
    senator = Senator.objects.get(pk = senator_id)
    bill_list = Bill.objects.filter(sponsor = senator_id)
    leadership_scores = Leadership.objects.filter(senator_id = senator_id).order_by('congress')
    print(leadership_scores)
    context = {'senator': senator, 'bill_list': bill_list, 'leadership_scores': leadership_scores}
    return render(request, 'gov_data/senator_detail.html', context)