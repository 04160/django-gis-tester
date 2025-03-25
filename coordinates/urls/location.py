from django.urls import path
from coordinates.views import location

urlpatterns = [
    path('list/', location.LocationModelListView.as_view(), name='location-list'),
    path('<slug:entity_slug>/create/', location.LocationModelCreateView.as_view(), name='location-create'),
    # path('<slug:entity_slug>/update/<uuid:location_pk>/', location.LocationModelUpdateView.as_view(), name='location-update'),
]