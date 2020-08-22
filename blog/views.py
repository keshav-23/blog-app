from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView , DetailView, CreateView, UpdateView, DeleteView
from .models import Post



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(LoginRequiredMixin, ListView):
    model= Post
    template_name = 'blog/home.html'   #<app_name>/<model>_<view_type>.html -> django convention
    context_object_name = 'posts'
    ordering = ['-date_created']
    

class UserPostListView(LoginRequiredMixin, ListView):
    model= Post
    template_name = 'blog/user_post.html'   #<app_name>/<model>_<view_type>.html -> django convention
    context_object_name = 'posts'
    #ordering = ['-date_created']

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author= user).order_by('-date_created')




class PostDetailView(DetailView):
    model= Post


class PostCreateView(LoginRequiredMixin, CreateView):
    
    model= Post
    fields= ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    
    model= Post
    template_name = 'blog/update.html'
    fields= ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model= Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


def about(request):
    return render(request, 'blog/about.html')