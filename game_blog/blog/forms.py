from django import forms
from blog.models import Tag


class TagForm(forms.Form):
    title = forms.CharField(max_lenght=50)
    slug = forms.CharField(max_lenght=50)

    def save(self):
        new_tag = Tag.objects.create(
                title=self.cleaned_data['title'],
                slug=self.objects.cleaned_data['slug']
                )
        return new_tag


