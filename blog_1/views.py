from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy
# Create your views here.
class BlogListview(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailview(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateview(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author','body']

class BlogUpdateview(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title','body']

class BlogDeleteview(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
