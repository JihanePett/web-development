from django.views.generic import ListView, DetailView,\
                                 CreateView, UpdateView, DeleteView
from blog.models import Post
from django.urls import reverse_lazy
from .forms import PostForm


# Create your views here.


class BlogView(ListView):
    model = Post
    template_name = 'blog.html'


class PostDetails(DetailView):
    model = Post
    template_name = 'post_details.html'


class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class EditPost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'edit_post.html'


class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog')
