from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import CommissionForm, Agency

class IndexView(generic.ListView):
    template_name = 'loaders/index.html'
    context_object_name = 'latest_commission_form_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return CommissionForm.objects.order_by('-pub_date')[:5]

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
