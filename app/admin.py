from django.contrib import admin
from app.models import *
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by')
    prepopulated_fields = {'blog_slug':('title',)}


admin.site.register(Category)
admin.site.register(Quote)
admin.site.register(Project)
admin.site.register(Team)
admin.site.register(Careers)
admin.site.register(Package)
admin.site.register(Testimonials)
admin.site.register(Contact)
admin.site.register(Home)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Gallery)
admin.site.register(Package_order)
admin.site.register(Subscribe)
admin.site.register(Faq)