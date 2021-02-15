
from django.shortcuts import render

from django.http import HttpResponse
from polls.forms import CommentForm
from polls.models import Post, Comment

def index(reguest):
        return HttpResponse("Hello my first page, thanks God")


def blog_index(reguest):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(reguest, "blog_index.html", context)


def blog_category(request, category):
        posts = Post.objects.filter(categories__name__contains=category).order_by("-created_on")
        context = {"category": category, "posts": posts}
        return render(request, "blog_category.html", context)

def blog_detail(request, pk):
        post = Post.objects.get(pk=pk)
        comments = Comment.objects.filter(post=post)

        form = CommentForm()
        if request.method == "POSTS":
                form = CommentForm(request.POST)
                if form.is_valid():
                        comment = comments(
                                author = form.cleaned_data["author"],
                                body = form.cleaned_data["body"],
                                post = post,
                        )
                        comment.save()
        context = {"post": post, "comments": comments, "form": form}
        return render(request, "blog_detail.html", context)
