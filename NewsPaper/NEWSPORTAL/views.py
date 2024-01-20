from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post,Author,Comment
from datetime import datetime

class Newslist(ListView):
    model = Post
    ordering = 'title'
    template_name = 'default.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context

class NewsDetail(DetailView):
    model = Post
    template_name =  'default.html'
    context_object_name =  'posts'



