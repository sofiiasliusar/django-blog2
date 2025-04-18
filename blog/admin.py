from django.contrib import admin
from django.shortcuts import get_object_or_404
from .models import Article, ArticleImage, Category
from .forms import ArticleImageForm
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'slug')
    prepopulated_fields = {'slug': ('category',)}
    fieldsets = (
        ('', {
            'fields': ('category', 'slug'),
        }),
    )


admin.site.register(Category, CategoryAdmin)


class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    form = ArticleImageForm
    extra = 0
    fieldsets = (
        ('', {
            'fields': ('title', 'image',),
        }),
    )


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'slug', 'main_page')
    inlines = [ArticleImageInline]
    multiupload_form = True
    multiupload_list = False
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('category',)  #  ???
    fieldsets = (  #  what is this and () inside is tuple? and why instead of [ use (
        # sections, yes, because it expects tuple
        ('', {
            'fields': ('category', 'pub_date', 'title', 'description', 'main_page'),
        }),
        ((u'Додатково'), { #  grp is what
            # django grappelli for better UI
            'classes': ('grp-collapse grp-closed',),
            'fields': ('slug',),
        }),
    )

    def delete_file(self, pk, request):
        """Delete an image"""
        obj = get_object_or_404(ArticleImage, pk)
        return obj.delete()


admin.site.register(Article, ArticleAdmin)







# admin.site.register(Article)
