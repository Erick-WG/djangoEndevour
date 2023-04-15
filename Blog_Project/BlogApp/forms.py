from django import forms
from .models import Post, Category


# making a query set that accesses our db.
choices = Category.objects.all().values_list('name', 'name')

# creating a list to store our query set's values.
choice_list = []

# appending the choices in our query set to our choice list.
for choice in choices:
    choice_list.append (choice)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "title_tag", "author", "category", "body")

        widgets = {
            "title" : forms.TextInput(attrs={'class': "form-control"}),
            "title_tag" : forms.TextInput(attrs={'class': "form-control"}),
            "author" : forms.Select(attrs={'class': "form-control"}),
            "category" : forms.Select(choices=choice_list, attrs={'class': "form-control"}),
            "body" : forms.Textarea(attrs={'class': "form-control"}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "title_tag", "body")

        widgets = {
            "title" : forms.TextInput(attrs={'class': "form-control"}),
            "title_tag" : forms.TextInput(attrs={'class': "form-control"}),
            #Edit form without the author field.
            "body" : forms.Textarea(attrs={'class': "form-control"}),
        }











