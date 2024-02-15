import datetime

from django import forms

from dogs.models import Dog, Parent


class StyleFromMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class DogForm(StyleFromMixin, forms.ModelForm ):

    class Meta:
        model = Dog
        fields = '__all__'

    def clean_birth_day(self):
        cleaned_data = self.cleaned_data['birth_day']
        now_year = datetime.datetime.now().year

        if now_year - cleaned_data.year > 100:
            raise forms.ValidationError('Указан возраст собаки боле 100 лет')

        return cleaned_data


class ParentForm(StyleFromMixin, forms.ModelForm ):




    class Meta:
        model = Parent
        fields = '__all__'


