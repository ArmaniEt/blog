from django import forms
from webapp.models import Article, Comment


class ArticleSearchForm(forms.Form):
    article_name = forms.CharField(max_length=200, required=False, label='Название статьи')


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        exclude = ['created_at']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['comment_to_comment']


class UpdateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['commented_to', 'commented_by', 'comment_to_comment']