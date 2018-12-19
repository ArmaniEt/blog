from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView
from webapp.models import Article, User
from webapp.forms import ArticleSearchForm, ArticleForm
from django.urls import reverse_lazy


class ArticleListView(ListView, FormView):
    template_name = 'index.html'
    model = Article
    form_class = ArticleSearchForm

    def get_queryset(self):
        article_name = self.request.GET.get('article_name')
        if article_name:
            return self.model.objects.filter(title__icontains=article_name)
        else:
            return self.model.objects.all()


class ArticleDetailView(DetailView):
    template_name = 'article_view.html'
    model = Article


class UserListView(ListView):
    template_name = 'users_view.html'
    model = User


class UserDetailView(DetailView):
    template_name = 'usr_view.html'
    model = User


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_create.html'
    form_class = ArticleForm
    success_url = reverse_lazy('index')