from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import CommissionForm, Agency

def index(request):
    fs = CommissionForm.objects.order_by('form_id')[:5]
    context = {
        'commission_form_list': fs,
    }
    return render(request, 'loaders/index.html', context)

def detail(request, form_id):
    form = get_object_or_404(CommissionForm, pk=form_id)
    return render(request, 'loaders/detail.html', {'form': form})

def load(request, form_id):
    form = get_object_or_404(CommissionForm, pk=form_id)
    try:
        selected_agency = form.agency_set.get(pk=request.POST['agency'])
    except (KeyError, Agency.DoesNotExist):
        return render(request, 'loaders/detail.html', {
            'form': form,
            'error_message': "You didn't select a valid agency.",
        })
    else:
        selected_agency.area += 1
        selected_agency.save()
        
        return HttpResponseRedirect(reverse('loaders:results', args=(form.id,)))

def results(request, form_id):
    form = get_object_or_404(CommissionForm, pk=form_id)
    return render(request, 'loaders/results.html', {'form': form})
