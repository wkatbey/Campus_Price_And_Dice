from campus.models import Restaurant, Item, BusinessHours
from django import forms

class SaveBusinessHoursForm(forms.ModelForm):

    class Meta:
        model = BusinessHours
        fields = ('from', 'to')

        widgets = {
            'from': forms.TimeField(attrs = {
                'class': 'form-control'
            }),
            'to': forms.TimeField(attrs = {
                'class': 'form-control'
            })
        }


class SaveRestaurantForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = ('name', 'location', 'phone_number', 'description')

        widgets = {
            'name': forms.TextInput(attrs = {
                'class': 'form-control'
            }),
            'location': forms.TextInput(attrs = {
                'class': 'form-control'
            }),
            'phone_number': forms.TextInput(attrs = {
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs = {
                'class': 'form-control'
            })
        }

    def save(self, maintainer, commit=True):
        restaurant = super().save(commit=False)
        restaurant.set_maintainer(maintainer)

        if commit:
            restaurant.save()

        return restaurant

    