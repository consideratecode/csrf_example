from django import forms

from . import models


class StatusForm(forms.ModelForm):

    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
        return instance

    class Meta:
        model = models.Status
        fields = ['message']
