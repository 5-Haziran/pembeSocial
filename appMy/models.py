from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(("Kategori Adı"), max_length=50)
    def __str__(self) -> str:
        return self.title

class Post(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(("Post baslik"), max_length=50)
    postText = models.TextField(("Post içerik"))
    postImg = models.ImageField(("Ürün Görseli"), upload_to=None, height_field=None, width_field=None, max_length=None,null=True,blank=True)
    postTime = models.DateTimeField(verbose_name='Oluşturma Zamanı', auto_now=False, auto_now_add=True,null=True,blank=True)
    postCategory = models.ForeignKey(Category, verbose_name=("Kategory"), on_delete=models.CASCADE,null=True,blank=True)
    likes = models.ManyToManyField(User, related_name=("liked_posts"),blank=True)
    likes_count = models.PositiveIntegerField(default=0)
    
    def __str__(self) -> str:
        return self.title    

class Profil(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE,null=True,blank=True)
    profil_img = models.ImageField(("Profil fotoğrafı"), upload_to=None, height_field=None, width_field=None, max_length=None,null=True,blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    
class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE, null=True,blank=True)
    postComment = models.ForeignKey(Post, verbose_name=(""), on_delete=models.CASCADE)
    comment = models.TextField(("Yorum"))
    commentTime = models.DateTimeField((""), auto_now=False, auto_now_add=True,null=True,blank=True) 
    