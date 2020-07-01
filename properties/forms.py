from .models import Property

from django import forms


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude = ('profile', 'list_date', 'slug')

        help_texts = {
                'name': 'Enter your Property Name',
                'address': 'Enter property address',
                'city': 'Enter property city',
                'state': 'Enter property state ',
                'zipcode': 'Enter property zipcode',
                'description': 'Enter property description',
                'price': 'Enter property price',
                'bedrooms': 'Enter No of bedrooms in property',
                'bathrooms': 'Enter No of bathrooms in property',
                'garage': 'Enter No of garage in property',
                'lot_size': 'Enter lot_size of property',
                'sqft': 'Enter property sqft',
                'photo_main': 'upload main picture of property',
                'photo_1': 'upload first picture of property',
                'photo_2': 'upload second picture of property',
                'photo_3': 'upload third picture of property',
                'photo_4': 'upload fourth picture of property',
                'photo_5': 'upload fivth picture of property',
                'photo_6': 'upload sixth picture of property',
            }
            
        error_messages = {
            'name': {
                'required': "property name is required",
            },
            'zipcode': {
                'max_length': "max length error",
            },
        }
