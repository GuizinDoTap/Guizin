from django.db import models
from django.utils import timezone
from django.contrib.auth.models import  User

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset()\
                                           .filter(status='published')

class Post(models.Model):
    Status = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User,
                              on_delete=models.CASCADE)
    content   = models.TextField()
    published = models.DateTimeField(default=timezone.now())
    created   = models.DateTimeField(auto_now_add=True)
    changed   = models.DateTimeField(auto_now=True)
    status    = models.CharField(max_length=10,
                                 choices=Status,
                                 default='draft')
    objects   = models.Manager()
    publicado = PublishedManager()

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return '{} - {}'.format(self.title,self.slug)



# Create your models here.
