from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import CommissionForm

def index(request):
    fs = CommissionForm.objects.order_by('form_id')[:5]
    template = loader.get_template('loaders/index.html')
    context = {
        'commission_form_list': fs,
    }
    return HttpResponse(template.render(context, request))

def detail(request, form_id):
    return HttpResponse("You're looking at form %s." % form_id)

def results(request, form_id):
    response = "You're looking at the results of form %s."
    return HttpResponse(response % form_id)

def load(request, form_id):
    return HttpResponse("You're loading a form %s." % form_id)
