from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import PostForm
from django.utils import timezone
from django.contrib.auth import login, logout
from .models import Post
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('all_posts')
    else:
        form = UserCreationForm()
    return render(request, 'blog/registration/registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('all_posts')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/registration/login.html', {'form': form})

@login_required 
def user_logout(request):
    logout(request)
    return redirect('all_posts')

@login_required  
def all_posts(request):
    # Retrieve all blog posts from the database
    posts = Post.objects.all()
    # Pass the posts to the template for rendering
    return render(request, 'blog/all_posts.html', {'posts': posts})

@login_required
def user_dashboard(request):
    user_posts = Post.objects.filter(author=request.user)
    return render(request, 'blog/user_dashboard.html', {'user_posts': user_posts})

@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('user_dashboard')
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})

@login_required
def edit_post(request, post_id):
    # Get the post object to edit
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            # Save the updated post
            form.save()
            return redirect('user_dashboard')  # Redirect to user dashboard after editing
    else:
        # Create a form instance and populate it with data from the post object
        form = PostForm(instance=post)

    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})


@login_required
def delete_post(request, post_id):
    # Get the post object to delete
    post = get_object_or_404(Post, pk=post_id)
    
    if request.method == 'POST':
        # Delete the post
        post.delete()
        return redirect('user_dashboard')  
    
    return redirect('user_dashboard')  


def view_post(request, post_id):
    # Retrieve the viewed blog post
    viewed_post = get_object_or_404(Post, pk=post_id)

    # Extract content features from all blog posts except the viewed post
    all_posts_except_viewed = Post.objects.exclude(pk=post_id)
    post_contents = [post.content for post in all_posts_except_viewed]

    # Append the content of the viewed post to post_contents
    post_contents.append(viewed_post.content)

    # Create TF-IDF vectors for the content features
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(post_contents)

    # Compute cosine similarity between viewed post and all other posts
    # Index into tfidf_matrix using the index of the viewed post
    viewed_post_index = len(all_posts_except_viewed)  # Index of the viewed post
    cosine_similarities = linear_kernel(tfidf_matrix[viewed_post_index], tfidf_matrix).flatten()

    # Sort posts based on similarity scores (excluding the viewed post itself)
    related_posts_indices = cosine_similarities.argsort()[::-1][1:]

    # Get top 5 related posts as recommendations
    recommended_posts = [all_posts_except_viewed[int(index)] for index in related_posts_indices[:5]]

    # Render the view_post template with viewed post and recommended posts
    return render(request, 'blog/view_post.html', {'post': viewed_post, 'recommended_posts': recommended_posts}) 