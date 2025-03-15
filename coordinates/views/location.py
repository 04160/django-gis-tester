
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from coordinates.models import Location

# class CustomerModelListView(DjangoLedgerSecurityMixIn,
    #                         CustomerModelModelViewQuerySetMixIn,
    #                         ListView):
    # template_name = 'django_ledger/customer/customer_list.html'
    # PAGE_TITLE = _('Customer List')
    # extra_context = {
    #     'page_title': PAGE_TITLE,
    #     'header_title': PAGE_TITLE,
    #     'header_subtitle_icon': 'dashicons:businesswoman'
    # }
    # context_object_name = 'customers'
class LocationModelListView(ListView):
    model = Location
    context_object_name = 'location_list'
    template_name = 'locations/locations_list.html'


# class LocationModelCreateView(CreateView):


# class LocationModelUpdateView(UpdateView):


# class LocationModelDeleteView(DeleteView):
