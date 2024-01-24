from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Like, Dislike
from .forms import PostForm
from django.http import JsonResponse
from django.core import serializers


# Create your views here.



# Post Views

def post_list(request):
    posts = Post.objects.all().order_by("-id")
    serialized_posts = []

    for post in posts:
        serialized_post = {
            'id': post.id,
            'content': post.content,
            'date': post.date,
            'author': {
                'id': post.author.id,
                'username': post.author.username,
                'function': post.author.function,  # Include other user fields as needed
                'profile_photo': str(post.author.profile_photo),
            },
            'comment': [],  # You might need to serialize comments here as well
            'likesCounter':post.count_likes()
        }
        serialized_posts.append(serialized_post)

    return JsonResponse({'posts': serialized_posts})

@login_required
def success(request):
    return render(request,'myapp/success.html')

@login_required
def create_post(request):
    myPost = PostForm()
    if request.method == 'POST':
        myPost = PostForm(request.POST)
        if myPost.is_valid():
            author_username = request.user.username

            post = myPost.save(commit = False)
            post.author = request.user
            post.save()
            return redirect('success/')
    else:
        myPost = PostForm()
    return render(request, 'myapp/homepage.html',{'form':myPost})
# Comment View

@login_required
def add_comment_to_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        # Process the form data and add a comment
        # ...
        return redirect('post_detail', post_id=post.id)
    return render(request, 'add_comment_to_post.html', {'post': post})

# Like and Dislike Views

@login_required
def like_post(request):
    post_id = request.POST.get('post_id')

    post = Post.objects.get(id=post_id)

    # Check if the user has already liked the post
    existing_like = Like.objects.filter(user=request.user, post=post).first()

    if existing_like:
        # User has already liked the post, return an appropriate response
        return JsonResponse({'success': False,'message':'You already liked this post.'})
    else:
        # Create a new like
        like = Like(user=request.user, post=post)
        like.save()
        # Update the likes count in the Post model
        likes_count = post.count_likes()
        return JsonResponse({'success':True,'likes_count': likes_count,'message':'You liked this post.'})

@login_required
def delete_post(request):
    print('in views delete')
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)
        if request.user == post.author or request.user.is_staff:
            post.delete()
            return JsonResponse({"message":"post deleted"})
        else:
            return JsonResponse({"message":"can't do this dude"})
    else:
        None
        

@login_required
def dislike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    Dislike.objects.get_or_create(user=request.user, post=post)
    return redirect('post_detail', post_id=post.id)

@login_required
def add_comment(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=post_id)
        text = request.POST.get('text', '')
        Comment.objects.create(post=post, text=text)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})