from django.shortcuts import render,HttpResponse,redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import *

# Create your views here.
# -------------------------------------------------------------------------------------
#                         LOGIN PAGE
# -------------------------------------------------------------------------------------                        
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request, 'Incorrect Username or password (They are case sensitive)')
        
    return render(request,'login.htm')


# -------------------------------------------------------------------------------------
#                         LOGOUT
# -------------------------------------------------------------------------------------
def logoutUser(request):
    logout(request)
    return redirect('loginPage')


# -------------------------------------------------------------------------------------
#                         HOME PAGE
# -------------------------------------------------------------------------------------
def home(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    myFilter = PostFilter(request.GET,queryset = posts)
    posts = myFilter.qs
    
    page =  request.GET.get('page')
    paginator = Paginator(posts,20)
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        
    
    
    context = {
        'posts': posts,
        'categories':categories,
        'myFilter':myFilter
    }
    
    return render(request, 'index.htm', context)



# -------------------------------------------------------------------------------------
#                         POST VIEW
# -------------------------------------------------------------------------------------
def post(request,slug):
    categories = Category.objects.all()
    post = Post.objects.get(slug = slug)
    
    commentForm = PostCommentForm()
    
    if request.method == 'POST':
        commentForm = PostCommentForm(request.POST)
        if commentForm.is_valid():
            commentForm.save()
        return redirect('home')
        
    
    context = {
        'categories':categories,
        'post':post,
        'commentForm': commentForm
        
    }
    return render(request, 'post.htm',context)



# -------------------------------------------------------------------------------------
#                         VIDEO POSTS VIEW
# -------------------------------------------------------------------------------------
def videoPosts(request):
    categories = Category.objects.all()
    videos = VideoPost.objects.all()
    myFilter = VideoFilter(request.GET,queryset = videos)
    videos = myFilter.qs
    
    page = request.GET.get('page')
    paginator = Paginator(videos,20)
    
    try:
        videos = paginator.page(page)
    except PageNotAnInteger:
        videos = paginator.page(1)
    except EmptyPage:
        videos = paginator.page(paginator.num_pages)
    
    context = {
        'videos':videos,
        'myFilter':myFilter,
        'categories':categories,
    }
    
    return render(request,'video-posts.htm',context)


# -------------------------------------------------------------------------------------
#                         VIDEO POST VIEW
# -------------------------------------------------------------------------------------
def videoPost(request,slug):
    video = VideoPost.objects.get(slug = slug)
    
    commentForm = VideoPostCommentForm()
    
    if request.method == 'POST':
        commentForm = VideoPostCommentForm(request.POST)
        if commentForm.is_valid():
            commentForm.save()
        return redirect('videoPosts')
            
    
    context = {
        'video':video,
        'commentForm':commentForm,
    }
    return render(request,'video-post.htm',context)

# -------------------------------------------------------------------------------------
#                         AUDIO POSTS VIEW
# -------------------------------------------------------------------------------------
def audioPostsView(request):
    categories = Category.objects.all()
    audios = AudioPost.objects.all()
    
    myFilter = VideoFilter(request.GET,queryset = audios)
    audios = myFilter.qs
    
    page = request.GET.get('page')
    paginator = Paginator(audios,20)
    
    try:
        audios = paginator.page(page)
    except PageNotAnInteger:
        audios = paginator.page(1)
    except EmptyPage:
        audios = paginator.page(paginator.num_pages)
    
    
    context = {
        'audios':audios,
        'myFilter':myFilter,
        'categories':categories
    }
    
    return render(request,'audio-posts.htm',context)

# -------------------------------------------------------------------------------------
#                         AUDIO POST VIEW
# -------------------------------------------------------------------------------------

def audioPost(request,slug):
    audio = AudioPost.objects.get(slug = slug)
    categories = Category.objects.all()
    commentForm = AudioPostCommentForm()
    
    if request.method == 'POST':
        commentForm = AudioPostCommentForm(request.POST)
        if commentForm.is_valid():
            commentForm.save()
        return redirect('audioPosts')
            
    
    context = {
        'audio':audio,
        'commentForm':commentForm,
        'categories':categories
    }
    return render(request,'audio-post.htm',context)


# -------------------------------------------------------------------------------------
#                         CATEGORIES VIEW
# -------------------------------------------------------------------------------------
def categoryPosts(request,pk):
    category_posts = Post.objects.filter(category = pk)
    category_video_posts = VideoPost.objects.filter(category = pk)
    category_audio_posts = AudioPost.objects.filter(category = pk)
    
    cats = Category.objects.get(id = pk)


    categories = Category.objects.all()

    page =  request.GET.get('page')
    paginator = Paginator(category_posts,20)
    
    try:
        category_posts = paginator.page(page)
    except PageNotAnInteger:
        category_posts = paginator.page(1)
    except EmptyPage:
        category_posts = paginator.page(paginator.num_pages)

    context= {
        'cats': cats,
        'category_posts': category_posts,
        'category_video_posts':category_video_posts,
        'category_audio_posts':category_audio_posts,
        'categories': categories
    }
    
    return render(request,'category1.htm',context)


# -------------------------------------------------------------------------------------
#                                   CONTACT PAGE
# -------------------------------------------------------------------------------------
def contactView(request):
    return render(request,'contact.htm')


# -------------------------------------------------------------------------------------
#                                   CRUDS
# -------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------
#                        ADD VIDEO POST VIEW
# -------------------------------------------------------------------------------------
def addVideoPost(request):
    form = AddVideoPostForm()
    categories = Category.objects.all()
    
    if request.method == 'POST':
        form = AddVideoPostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('videoPosts')

    context = {
        'categories':categories,
        'videoForm':form
    }

    return render(request,'forms/add-video-post.htm',context)


# -------------------------------------------------------------------------------------
#                        UPDATE VIDEO
# -------------------------------------------------------------------------------------
def updateVideoPost(request,slug):
    video= VideoPost.objects.get(slug = slug)
    
    form = AddVideoPostForm(instance = video)
    
    if request.method == 'POST':
        form = AddVideoPostForm(request.POST,instance = video)
        if form.is_valid():
            form.save()
        return redirect('home')
    
    context = {
        'postForm':form
    }
    return render(request,'forms/update-post.htm',context)    

# -------------------------------------------------------------------------------------
#                         DELETE VIDEO VIEW
# -------------------------------------------------------------------------------------
@login_required(login_url='loginPage')
def deleteVideoPost(request,slug):
    video = VideoPost.objects.get(slug = slug)
    video.delete()
    return redirect('home')



# -------------------------------------------------------------------------------------
#                        ADD AUDIO VIEW
# -------------------------------------------------------------------------------------
@login_required(login_url='loginPage')
def addAudioView(request):
    categories = Category.objects.all()
    form = AddAudioForm()
    
    if request.method == 'POST':
        form = AddAudioForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home') 
        
    context = {
        'categories':categories,
        'audioForm':form
    }    
       
    return render(request,'forms/add-audio.htm',context)



# -------------------------------------------------------------------------------------
#                        UPDATE AUDIO
# -------------------------------------------------------------------------------------
def updateAudioPost(request,slug):
    audio = AudioPost.objects.get(slug = slug)
    
    form = AddAudioForm(instance = audio)
    
    if request.method == 'POST':
        form = AddAudioForm(request.POST,instance = audio)
        if form.is_valid():
            form.save()
        return redirect('home')
    
    context = {
        'postForm':form
    }
    
    return render(request,'forms/update-post.htm',context)   



# -------------------------------------------------------------------------------------
#                         DELETE AUDIO VIEW
# -------------------------------------------------------------------------------------
@login_required(login_url='loginPage')
def deleteAudioPost(request,slug):
    audio = AudioPost.objects.get(slug = slug)
    audio.delete()
    return redirect('home')


# -------------------------------------------------------------------------------------
#                         ADD CATEGORY VIEW
# -------------------------------------------------------------------------------------
@login_required(login_url='loginPage')
def addCategoryView(request):
    categories = Category.objects.all()
    form = AddCategoryForm()
    
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {
        'categories': categories,
        'categoryForm':form
    }
    
    return render(request,'forms/add-category.htm',context)



# -------------------------------------------------------------------------------------
#                        ADD POST VIEW
# -------------------------------------------------------------------------------------
@login_required(login_url='loginPage')
def addPostView(request):
    categories = Category.objects.all()
    form = AddPostForm()
    
    if request.method == 'POST':
        form = AddPostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home') 
        
    context = {
        'categories':categories,
        'postForm':form
    }    
       
    return render(request,'forms/add-post.htm',context)


# -------------------------------------------------------------------------------------
#                         DELETE POST VIEW
# -------------------------------------------------------------------------------------
@login_required(login_url='loginPage')
def deletePost(request,slug):
    post = Post.objects.get(slug = slug)
    post.delete()
    return redirect('home')


# -------------------------------------------------------------------------------------
#                        UPDATE POST VIEW
# -------------------------------------------------------------------------------------
@login_required(login_url='loginPage')
def updatePost(request,slug):
    post= Post.objects.get(slug = slug)
    
    form = AddPostForm(instance = post)
    
    if request.method == 'POST':
        form = AddPostForm(request.POST,instance = post)
        if form.is_valid():
            form.save()
        return redirect('home')
    
    context = {
        'postForm':form
    }
    return render(request,'forms/update-post.htm',context)