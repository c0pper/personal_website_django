from django.contrib import admin
from .models import Skill, Experience, Project, Category, Place, Institution, Certification, Testimonial


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'date')
    list_filter = ("date",)
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'exp_type')
    list_filter = ("start_time",)
    search_fields = ['name']


# Register your models here.

admin.site.register(Skill)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)
admin.site.register(Place)
admin.site.register(Institution)
admin.site.register(Certification)
admin.site.register(Testimonial)