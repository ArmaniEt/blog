from django.views.generic import ListView, DetailView
from webapp.models import Article, User


class ArticleListView(ListView):
    template_name = 'index.html'
    model = Article


class ArticleDetailView(DetailView):
    template_name = 'article_view.html'
    model = Article


class UserListView(ListView):
    template_name = 'users_view.html'
    model = User


class UserDetailView(DetailView):
    template_name = 'usr_view.html'
    model = User

