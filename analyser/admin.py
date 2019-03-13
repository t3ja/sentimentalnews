from django.contrib import admin
from django import forms
from .models import *
from django.utils.html import format_html

class ArticleAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(ArticleAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'content':
            formfield.widget = forms.Textarea(attrs={'cols': 80, 'rows': 20})
        if db_field.name == 'title':
            formfield.widget = forms.Textarea(attrs={'cols': 80, 'rows': 3})
        return formfield

    def article_url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.url)

    article_url.allow_tags = True
    fieldsets = [
        (None, {'fields': ['title', 'content', 'label', 'country', 'source', 'author', 'url']}),
        ('Classification DateTime', {'fields': ['analysed_at'], 'classes': ['collapse']})
    ]
    search_fields = ['title', 'country', 'label']
    list_display = ['title', 'content', 'label', 'country', 'published_at', 'article_url']
    list_filter = ['published_at']


    # def current_bid_display(self, obj):
    #     return "£{0}".format(obj.current_bid)


admin.site.register(Article, ArticleAdmin)
