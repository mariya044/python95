from django.contrib.auth.decorators import permission_required, login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from post.forms import PostForm
from post.models import Post



@login_required
def posts(request):
    search_query = request.GET.get("search", "")
    if search_query:
        posts = Post.objects.filter(title__icontains=search_query)
    else:
        posts = Post.objects.all().order_by("id")
    all_images = Post.objects.all()
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page', 1)

    try:
        all_posts = paginator.page(page_number)
    except PageNotAnInteger:
        all_posts = paginator.page(1)
    except EmptyPage:
        all_posts = paginator.page(paginator.num_pages)
    return render(request, "posts.html", {"all_posts": all_posts, "all_images": all_images})


@login_required
def posts_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "posts_view.html", {"post": post})


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




# Create your views here.
