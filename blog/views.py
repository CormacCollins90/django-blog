from django.shortcuts import render, redirect, HttpResponse, reverse, get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.

def get_index(request):
    posts = Post.objects.all()
    return render(request, "blog/index.html", {'posts': posts})
    
def read_post(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, "blog/read_post.html", {'post': post})
    

def edit_post(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        form.save()
        return redirect("/")
    else:        
        form=PostForm(instance=post)
        return render(request, "blog/post_form.html", {'form': form })    
        
def add_post(request):
   if request.method == "POST":
       form = PostForm(request.POST)
       if form.is_valid():
           post = form.save()
           return redirect(read_post, post.id)
   else:
       form = PostForm()
       return render(request, "blog/post_form.html", {'form' : form})        
    