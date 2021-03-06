from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        queryset = super(PublishedManager, self)\
            .get_queryset()\
            .filter(status='published')
        
        return queryset


class Post(models.Model):
    STATUS_CHOICE = (
        ('draft', 'Draft'), ('published', 'Published')
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICE,
                              default='draft')

    published = PublishedManager()
    objects = models.Manager()

    class Meta:
        ordering = ('-publish',)

    def __str___(self):
        return self.title
