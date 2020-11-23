from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView
from django.utils import timezone
from .models import Post, Comment

# Create your views here.


# def post_list(request):
#     posts = Post.objects.filter(
#         published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'blog/post_list.html', {'posts': posts})

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = 'posts'
    ordering = ['-published_date']
    paginate_by = 5


class PostCreateView(CreateView):
    model = Post
    fields = ['text', 'amount', 'picture']
    template_name = 'blog/post_edit.html'
    success_url = '/'

    def get_form(self):
        form = super(PostCreateView, self).get_form()
        form.instance.author = self.request.user
        form.instance.published_date = timezone.now()
        return form


# class CommentCreateView(CreateView):
#     model = Comment
#     fields = ['comment']
#     template_name = 'blog/post_edit.html'
#     success_url = '/'


class CommentListView(ListView):
    model = Comment
    template_name = "blog/post_detail.html"
    context_object_name = 'comments'
    ordering = ['-created_date']
    paginate_by = 5


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
