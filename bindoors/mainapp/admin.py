from django.contrib import admin
from .models import Project, Partner, Review


# Register your models here.

class ProjectConfig(admin.ModelAdmin):
    fields = ('object', 'address', 'date', 'task', 'jobs', 'price', 'img1', 'thumb1', 'img2', 'thumb2', 'img3',
              'thumb3', 'img4', 'thumb4', 'img5', 'thumb5', 'img6', 'thumb6')
    list_display = ('object', 'address', 'price',)

admin.site.register(Project, ProjectConfig)

class PartnerConfig(admin.ModelAdmin):
    fields = ('name', 'img',)
    list_display = ('name',)

admin.site.register(Partner, PartnerConfig)

class ReviewConfig(admin.ModelAdmin):
    fields = ('name', 'city', 'img', 'text',)
    list_display = ('name',)

admin.site.register(Review, ReviewConfig)