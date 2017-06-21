from django.db import models
from django.core.exceptions import ValidationError


class Quote(models.Model):
    quote_text = models.CharField(max_length=100)

    def __str__(self):
        return self.quote_text[:20]


class Worker(models.Model):
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    job = models.CharField(max_length=20)
    image = models.ImageField(upload_to='workers/images')

    def __str__(self):
        return self.name+' '+self.surname


class About(models.Model):
    about_text = models.TextField(max_length=500)
    about_title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'About'

    def save(self, *args, **kwargs):
        if About.objects.exists() and not self.pk:
            raise ValidationError("There must be only one instance of About")
        return super().save(*args, **kwargs)


class Service(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='services/icons')

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Work(models.Model):
    categories = models.ManyToManyField(Category)
    portfolio = models.ForeignKey(Portfolio)
    icon = models.ImageField(upload_to='works/icons')

    def __str__(self):
        return "Work "+str(self.pk)


class Tag(models.Model):
    name = models.CharField(max_length=15, primary_key=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    tags = models.ManyToManyField(Tag)
    blog = models.ForeignKey(Blog)
    changed_at = models.DateTimeField(auto_now=True)
    text = models.TextField(max_length=3000)
    title = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='blog/posts/cover_images')

    def __str__(self):
        return self.title[:20]
