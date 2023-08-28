from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.

def index (request):
    post = Post.objects.all().order_by('-id')
    category = Category.objects.all()
    
    query = request.GET.get('q')
    if query:
        post = post.filter(
            Q(title__icontains=query)|
            Q(postText__icontains=query)|
            Q(postCategory__title__icontains=query)
        ).distinct
    
    context = {
        'post':post,
        'category':category
    }
    
    return render (request,'index.html',context)

def category(request, id):
    
    category = Category.objects.all()
    post = Post.objects.filter(postCategory=id)
    
    context = {
        'post':post,
        'category':category
    }
    
    return render (request,'category.html',context)

def detail (request, id):
    post = Post.objects.get(id=id)
    category = Category.objects.all()
    comment = Comment.objects.filter(postComment=post)

    if request.method == "POST":
        comment =request.POST['comment']
        comn = Comment(comment=comment, postComment=post,user=request.user)
        comn.save()
        
        return redirect ('/detay/' + id + '/') 
    
    context = {
        'post':post,
        'category':category,
        'comment': comment,
        'profil':profil
    }
    
    return render (request,'detail.html',context)


def register(request):
    
    if request.method == "POST":
        name = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password==password2:
            if User.objects.filter(username=name).exists():
            #? 'exists' veri tabanında sorgu yaparak inputtan gelen name ile username karşılaştırmasını yapar
                context = {
                    'information':'Bu kullanıcı adı kullanılmaktadır. Farklı bir kullanıcı adı deneyiniz'
                }
                
                return render (request,'register.html',context)
            
            if User.objects.filter(email=email).exists():
                context = {
                    'information':'Girmiş mail adresi sistemimizde kayıtlıdır. Farklı bir mail adresiyle tekrar kayıt olmayı deneyin'
                }
                return render (request,'register.html',context)
            
            else:
                user = User.objects.create_user(username=name,email=email,first_name=name,last_name=lastname,password=password)
                user.save()
                return redirect ('/')
            
        else:
            context = {
                'informatin': 'Parolanız girmiş olduğunuz tekrar parolasıyla uyuşmuyor parolanızı kontrol edin'
            }
            return render (request,'register.html',context)
        
    return render (request,'part/register.html')
    
    
def loginn (request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('anasayfa')
        else:
            context = {
                'information':'Girmiş olduğunuz kullanıcı adı veya parola hatalı tekrar deneyin.'
            }
            
            return render(request,'part/login.html',context)
    
    return render (request,'part/login.html')

def logoutt (request):
    logout(request)
    
    return redirect('anasayfa')


@login_required(login_url='/giris/')
def profil (request):
    
    categories = Category.objects.all()
    
    if request.user.is_authenticated:
        try: 
            profil = Profil.objects.get(user_id=request.user)
        except Profil.DoesNotExist:
            
            profil = Profil(user=request.user)
            profil.save()
        
    if request.method =='POST' and 'profil-img' in request.POST:
        filee =request.FILES.get('image')
        
        if filee:
            profil.profil_img = filee
            profil.save()
    
    
    if request.method == "POST" and "person-btn" in request.POST:
        user = request.user
        user.username=request.POST['username']
        user.firstname=request.POST['firstname']
        user.lastname = request.POST['lastname']
        user.email = request.POST['email']
        
        user.save()       
        
    if request.method =='POST' and "post-btn" in request.POST:
        title=request.POST['title']
        postText=request.POST['postText']
        postImg = request.FILES['postImg']
        category_id = request.POST['category']
        
        category = Category.objects.get(id=category_id)

        post = Post(title=title,postText=postText,postImg=postImg,postCategory=category, user=request.user)
        post.save()
        
        return redirect('anasayfa')
        
    context = {
        'categories':categories,
        'profil':profil
    }
        
    return render (request,'profil.html',context)

@login_required
def likeds (request, post_id):
    post = Post.objects.get(id=post_id)
    
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        
    else: 
        post.likes.add(request.user)
        
    post.likes_count=post.likes.count()
    
    post.save()
    
   
    return redirect('anasayfa')

def trends (request):
    
    trend_post = Post.objects.filter(likes_count__gte=5).order_by('-likes_count')
    
    context={
        'trend_post':trend_post
    }
    
    return render (request,'trends.html',context)