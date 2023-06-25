from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()


class Profile(models.Model):
    user=models.OneToOneField(User,related_name='profile', on_delete=models.CASCADE)
    image=models.ImageField(null=True)
    caption=models.TextField(default="")
    created_at=models.DateTimeField(auto_now_add="True")
    updated_at=models.DateTimeField(auto_now="True")

    class Meta:
        db_table="profile"




class Post(models.Model):
    user=models.ForeignKey(User,related_name='post', on_delete=models.CASCADE)
    image=models.ImageField(null=True)
    caption=models.TextField(default="")
    created_at=models.DateTimeField(auto_now_add="True")
    updated_at=models.DateTimeField(auto_now="True")

    class Meta:
        db_table="post"
# Create your models here.




class LikePost(models.Model):
    user=models.ForeignKey(User,related_name='like_post', on_delete=models.CASCADE)
    post=models.ForeignKey(Post,related_name='like_post', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add="True")
    updated_at=models.DateTimeField(auto_now="True")

    class Meta:
        db_table="like_post"
# Create your models here.
