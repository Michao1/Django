from personal_blog.forms import CommentForm
from django.shortcuts import render
from personal_blog.models import Post, Comment

def index_blog(request):
    posts = Post.objects.all().order_by('-create_on')
    context = {
        "posts" : posts,
    }
    return render(request, "blogs/index.html", context)


def category_blog(request, category):
    posts = Post.objects.filter(
        categories__name__constain = category
    ).order_by(
        '-created_on'
    )
    context = {
        'category' : category,
        'posts': posts
    }
    return render(request, 'blogs/category.html', context)


def detail_blog(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
    if form.is_valid():
        comment = Comment(
            author=form.cleaned_data["author"],
            body=form.cleaned_data["body"],
            post=post
        )
        comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }

    return render(request, 'blogs/detail.html', context)