from django.shortcuts import render
from django.views.generic import ListView, DetailView
from webapp.models import Article


class ArticleListView(ListView):
    template_name = 'index.html'
    model = Article


class ArticleDetailView(DetailView):
    template_name = 'article_view.html'
    model = Article