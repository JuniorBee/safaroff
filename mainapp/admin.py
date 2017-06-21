from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import (Worker, Work, Quote, Portfolio, Service, Category,
                     About, BlogPost, Blog, Tag)


@register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_filter = ('blog', 'changed_at', 'tags')


@register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_filter = ('job', )
    list_display = ('picture', 'name', 'surname', 'job')

    def picture(self, obj):
        return '<img src={url} style="width: 100px; height=100px; ' \
               'border-radius:50%;"/>'.format(url=obj.image.url)
    picture.allow_tags = True
    picture.short_description = 'Picture'


admin.site.register(Work)
admin.site.register(Quote)
admin.site.register(Portfolio)
admin.site.register(Service)
admin.site.register(Category)
admin.site.register(About)
admin.site.register(Tag)
admin.site.register(Blog)
