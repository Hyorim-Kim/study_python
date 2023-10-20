from django.contrib import admin
from pro9app.models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'irum', 'juso', 'nai')

admin.site.register(Article, ArticleAdmin)