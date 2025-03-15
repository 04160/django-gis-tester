
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from coordinates.models import Location
from django.db.models import Q

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
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')

        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(lat__icontains=search_query) |
                Q(lng__icontains=search_query)
            )

        return queryset


# class LocationModelCreateView(CreateView):


# class LocationModelUpdateView(UpdateView):


# class LocationModelDeleteView(DeleteView):
