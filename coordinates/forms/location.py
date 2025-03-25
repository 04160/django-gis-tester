from django.forms import ModelForm, TextInput, EmailInput, NumberInput, FloatField
from coordinates.models.location import LocationModel


class LocationModelForm(ModelForm):
    class Meta:
        model = LocationModel
        fields = [
            'name',
            'lat',
            'lng',
        ]
        widgets = {
            'name': TextInput(attrs={'class': input}),
            'lat': FloatField(
                min_value=-90,
                max_value=90,
                # attrs={'class': input},
            ),
            'lng': FloatField(
                min_value=-180,
                max_value=180,
                # attrs={'class': input},
            ),
        }