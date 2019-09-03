from django import forms
from django.db import models
from .models import Abduction, Type, Applience, Bringing, Repair
from django.contrib.admin.widgets import AdminSplitDateTime


class UserModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.type


class UModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.date
'''comment 1'''

class UsModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.information


'''class AbductionForm(forms.ModelForm):
    date = forms.CharField(label='Дата:')

    class Meta:
        model = Abduction
        fields = ('date',)'''

'''BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
            ('blue', 'Blue'),
            ('green', 'Green'),
            ('black', 'Black'),
        ]'''

'''class AbductionForm2(forms.ModelForm):
        birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
        favorite_colors = forms.MultipleChoiceField(
            required=False,
            widget=forms.CheckboxSelectMultiple,
            choices=FAVORITE_COLORS_CHOICES,
        )

        class Meta:
            model = Abduction
            fields = ('date',)'''


class ApplienceForm(forms.ModelForm):
    number_of_applience = forms.IntegerField(label='Номер прибора:')
    typeofapplience = UserModelChoiceField(queryset=Type.objects.filter(), required=False, label='Тип прибора:')
    bringing = UModelChoiceField(queryset=Bringing.objects.filter(), required=False, label='Дата привоза:')
    repair = UsModelChoiceField(queryset=Repair.objects.filter(), required=False,
                                label='Информация о ремонте прибора:')

    class Meta:
        model = Applience
        fields = ('number_of_applience', 'typeofapplience', 'bringing', 'repair',)


class AbductionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AbductionForm, self).__init__(*args, **kwargs)
        # activating calendar
        self.fields['date'].widget = AdminSplitDateTime()

    class Meta:
        model = Abduction
        exclude = ('user', )
