from django import forms

CAMERA_CHOICES= [
    ('camera','20MP Camera'),
    ('caemra','18MP Camera'), 
    ('camera','8MP Front Camera'),
    ]

RAM_CHOICES= [
    ('memory','2GB RAM'),
    ('memory','4GB RAM'), 
    ('memory','8GB RAM'),
    ]

FCAMERA_CHOICES= [
    ('fcam','8MP Front-Face Camera'),
    ('fcam','12MP Front-Face Camera'), 
    ('fcam','32MP Front-Face Camera'),
    ]

class ItemForm(forms.Form):
    pname = forms.CharField(label='Phone Name', max_length=100)
    desc = forms.CharField(label="Description", max_length=100)
    price = forms.IntegerField(max_value=100000)
    feature1 = forms.CharField(label='Select main camera Feature', widget=forms.Select(choices=CAMERA_CHOICES))
    feature2 = forms.CharField(label='Select Memory Feature', widget=forms.Select(choices=RAM_CHOICES))
    feature3 = forms.CharField(label='Select front camera Feature', widget=forms.Select(choices=FCAMERA_CHOICES))
