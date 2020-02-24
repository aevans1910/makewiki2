from django import forms
from wiki.models import Page


class PageForm(forms.ModelForm):
    """ Render and process a form based on the Page model. """
    model = Page


class FriendlyForm(forms.Form):
    post_title = forms.CharField(max_length=250)
    author_name = forms.CharField(max_length=100)