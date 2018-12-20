from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView
from webapp.models import Article, User, Comment
from webapp.forms import ArticleSearchForm, ArticleForm, CommentForm, UpdateCommentForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404


class ArticleListView(ListView, FormView):
    template_name = 'index.html'
    model = Article
    form_class = ArticleSearchForm

    def get_queryset(self):
        article_name = self.request.GET.get('article_name')
        if article_name:
            return self.model.objects.filter(title__icontains=article_name) | self.model.objects.filter(text__icontains=article_name)
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


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article_update.html'
    form_class = ArticleForm
    success_url = reverse_lazy('index')


class CommentCreateView(CreateView):
    model = Comment
    template_name = 'comment_create.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('article_view', kwargs={'pk': self.object.commented_to.pk})

    def form_valid(self, form):
        form.instance.commented_to = get_object_or_404(Article, pk=self.kwargs['pk'])
        return super().form_valid(form)


class CommentUpdateView(UpdateView):
    model = Comment
    template_name = 'comment_update.html'
    form_class = UpdateCommentForm

    def get_success_url(self):
        return reverse('article_view', kwargs={'pk': self.object.commented_to.pk})

