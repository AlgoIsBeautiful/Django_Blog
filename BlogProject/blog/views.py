from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from comments.forms import CommentForm
from django.utils import timezone
from .models import Post, Category, Project, Tag
from django.db.models import Q

import markdown


def index(request):
    # return HttpResponse("Welcome to my blog")
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


#
class IndexView(ListView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post_list'
    paginate_by = 10

#
class TagView(ListView):
    model = Post
    template_name = 'blog/base.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tags=tag)
#
class CategoryView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super().get_queryset().filter(category=cate)
    def get_context_data(self, *, object_list=None, **kwargs):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        context = super(IndexView, self).get_context_data()
        context['page_title'] = cate.name
        return context
#
#
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super(PostDetailView, self).get(request, *args, **kwargs)
        self.object.increase_views()
        return response

    def get_object(self, queryset=None):
        post = super(PostDetailView, self).get_object(queryset=None)
        post.body = markdown.markdown(post.body,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])
        return post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            'form': form,
            'comment_list': comment_list
        })
        return context
#


class ArchivesView(ListView):
    model = Post
    template_name = 'blog/base.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchivesView, self).get_queryset().filter(created_time_year=year,
                                                               created_time_month=month)

def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

#
#
#


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.increase_views()
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'blog/detail.html', context=context)

#
#
#

def search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = "Please type key words"
        return render(request, 'blog/base.html', {'error_msg': error_msg})

    post_list = Post.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
    return render(request, 'blog/base.html', {'error_msg': error_msg,
                                               'post_list': post_list})

def about(request):
    return render(request, 'blog/about.html')

def home(request):
    post_list = Post.objects.all().order_by('-created_time')[:3]
    proj_list = Project.objects.all().order_by('-created_time')[:4]
    return render(request, 'blog/home.html', context={
        'post_list': post_list,
        'proj_list': proj_list
    })