from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Post(models.Model):

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    publish_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comments=True)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):

    post = models.ForeignKey('myblog.Post', on_delete=models.CASCADE)
    author = models.CharField(max_length=256)
    text = models.TextField()
    approved_comments = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now())

    def approve(self):
        self.approved_comments = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.title


class Visitor(models.Model):
    v_name = models.CharField(max_length=256)
    v_email = models.EmailField(required=False)
    address = models.TextField()
    date_of_birth = models.DateTimeField()
