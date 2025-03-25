from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from coordinates.models import LocationModel
from coordinates.forms import LocationModelForm
from django.db.models import Q


class LocationModelListView(ListView):
    model = LocationModel
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


class LocationModelCreateView(CreateView):
    template_name = 'locations/locations_create.html'
    form_class = LocationModelForm
    context_object_name = 'location'


class LocationModelUpdateView(UpdateView):
    template_name = 'locations/locations_update.html'
    form_class = LocationModelForm
    context_object_name = 'location'
    slug_field = 'id'


# class LocationModelDeleteView(DeleteView):
