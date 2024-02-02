from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post,Author,Comment
from datetime import datetime
from .filters import PostFilter
from django.views import View
class Newslist(ListView):
    model = Post
    ordering = 'title'
    template_name = 'default.html'
    context_object_name = 'posts'
    paginate_by = 10


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context

        # Переопределяем функцию получения списка товаров

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

class NewsDetail(DetailView):
    model = Post
    template_name =  'default.html'
    context_object_name =  'posts'

class PostSearchView(View):
    template_name = 'NEWSPORTAL/post_search.html'

    def get(self, request, *args, **kwargs):
        filter = PostFilter(request.GET, queryset=Post.objects.all())
        return render(request, self.template_name, {'filter': filter})




