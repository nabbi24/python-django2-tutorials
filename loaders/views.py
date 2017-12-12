from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404

from .models import CommissionForm

def index(request):
    fs = CommissionForm.objects.order_by('form_id')[:5]
    context = {
        'commission_form_list': fs,
    }
    return render(request, 'loaders/index.html', context)

def detail(request, form_id):
    try:
        fs = CommissionForm.objects.get(form_id=form_id)
    except CommissionForm.DoesNotExist:
        raise Http404("The Form does not exist.")
    return render(request, 'loaders/detail.html', {'form_id': form_id})

def results(request, form_id):
    response = "You're looking at the results of form %s."
    return HttpResponse(response % form_id)

def load(request, form_id):
    return HttpResponse("You're loading a form %s." % form_id)
