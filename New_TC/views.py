from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post 
from .forms import PostForm

# Create your views here.

def index(request): 
    # If the Method is post 
    if request.method == 'POST':
        form=PostForm(request.POST,request.FILES)
        # if the form is valid
        if form.is_valid():
            # if yes, save
            form.save()

             # Redirect to Home
            return HttpResponseRedirect('/')

                
        else:
            # no, show error
            return HttpResponseRedirect(form.erros.as_json())

    # get all posts , limit=20
    posts=Post.objects.all().order_by('-created_at')[:20]

    # Show
    return render(request,'posts.html',
                    {'posts':posts})


def delete(request,post_id):
    # Find post
    post=Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')




def edit(request, post_id):
    posts = Post.objects.get(id=post_id)
    if request.method == "POST":
       
        form = PostForm(request.POST, request.FILES, instance=posts)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            return HttpResponse("not valid")

    return render(request,'edit.html', {'posts': posts})




def like(request,post_id):
    like = Post.objects.get(id=post_id)
    like.likes += 1
    like.save()
    return HttpResponseRedirect('/')
