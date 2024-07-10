from django.contrib.auth.decorators import permission_required, login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from post.forms import PostForm
from post.models import Post

from announcement.models import Subject

from post.forms import CommentForm

from post.models import Comment


@login_required
def posts(request,subject_id=None):
 if subject_id:
     post=Post.objects.filter(subject_id=subject_id)
 else:
     post=Post.objects.all()
 paginator = Paginator(post, 2)
 page_number = request.GET.get('page', 1)
 try:
     posts = paginator.page(page_number)
 except PageNotAnInteger:
     posts = paginator.page(1)
 except EmptyPage:
     posts = paginator.page(paginator.num_pages)

 context={
     'subjects':Subject.objects.all(),
     'posts':posts,

 }
 return render(request,"posts.html",context)



@login_required
def posts_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments=Comment.objects.all()
    form=CommentForm()
    return render(request, "posts_view.html", {"post": post,'comments':comments,'form':form})


@permission_required(perm="post.add_post", raise_exception=True)
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            form.save_m2m()
            return redirect("posts")
        else:
            return redirect("posts")
    else:
        form = PostForm()
    return render(request, "create.html", {"form": form})


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.user:
        return redirect(f"/posts/{post_id}/")
    if request.method == "GET":
        form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return redirect("posts")
    return render(request, "edit_post.html", {"form": form, "post": post})


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("posts")
    template_name = "delete_post.html"


def post_comment(request,post_id):
    post=get_object_or_404(Post,id=post_id)
    comment=None
    form=CommentForm(data=request.POST)
    if form.is_valid():
        comment=form.save(commit=False)
        comment.post=post
        comment.name=request.user
        comment.save()
    return render(request,'post_comment.html',{'post':post,'form':form,'comment':comment})
