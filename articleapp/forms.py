from django.forms import ModelForm
from django import forms

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    # content 필드가 만들어질 때 class와 style을 미리 결정해준다
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-start',
                                                           'style': 'height: auto;'}))
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)

    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']