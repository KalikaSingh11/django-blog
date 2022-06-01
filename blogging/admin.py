from django.contrib import admin

# Register your models here.
from blogging.models import Post, Category


class CategoryInline(admin.TabularInline):
    model = Category.posts.through


class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]
    exclude = ("posts",)


# and a new admin registration
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
