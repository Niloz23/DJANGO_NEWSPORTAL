from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    rating = models.IntegerField(default=0)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def update_rating(self):
        posts_rating = 0
        comment_rating = 0
        posts_comment_rating = 0
        posts = Post.objects.filter(author = self)
        for p in posts:
            posts_rating += p.rating


        comments = Comment.objects.filter(user = self.user)
        for c in comments:
            comment_rating += c.rating

        posts_comments = Comment.objects.filter(post__author = self)
        for pc in posts_comments:
            posts_comment_rating += pc.rating

        self.rating = posts_rating * 3 + comment_rating + posts_comment_rating
        self.save()







class Category(models.Model):
    category_name = models.CharField(max_length=255 ,unique = True)

class Post(models.Model):
    article = 'ar'
    news = 'ns'
    CHOISES=[
        (article, 'статья'),
        (news, 'новость')
    ]
    type = models.CharField(max_length = 2, choices = CHOISES)
    post_created_at = models.DateTimeField(auto_now_add = True)

    category = models.ManyToManyField(Category, through = 'PostCategory')
    author = models.ForeignKey(Author, on_delete = models.CASCADE,related_name='posts')


    title = models.CharField(max_length = 255)
    main_text = models.TextField()
    post_rating = models.IntegerField(default = 0)

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

    def preview(self):
        preview_length = 124
        if self.main_text[:preview_length] > self.main_text:
            return self.main_text
        else:
            return self.main_text[:preview_length] + '...'


class PostCategory(models.Model):

    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,primary_key= True)

    comment_text = models.TextField()
    comment_created_at = models.DateTimeField(auto_now_add = True)
    comment_rating = models.IntegerField(default = 0)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()



















