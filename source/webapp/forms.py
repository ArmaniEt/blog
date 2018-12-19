from django import forms


class ArticleSearchForm(forms.Form):
    article_name = forms.CharField(max_length=200, required=False, label='Название статьи')