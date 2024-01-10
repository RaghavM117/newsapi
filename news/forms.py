from django import forms

class NewsFilterForm(forms.Form):
    COUNTRIES = [
        ('us','United States'),
        ('gb', 'United Kingdom'),
        ('in','India'),
        ('ca','Canada'),
    ]
    
    CATEGORIES = [
        ('general', 'General'),
        ('bussiness','Bussiness'),
        ('health','Health'),
        ('education','Education'),
    ]

    country = forms.ChoiceField(choices=COUNTRIES, label='Select Country')
    category =forms.ChoiceField(choices=CATEGORIES,label='Select Category')