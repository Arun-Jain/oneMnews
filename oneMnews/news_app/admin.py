from django.contrib import admin
from .models import NewsTypes, Country, News
from django.contrib.auth import get_user_model
# Register your models here.

@admin.register(NewsTypes)
class NewsTypesAdmin(admin.ModelAdmin):
	list_display = ("id", "news_type")
	list_filter = ("news_type",)
	search_fields = ("id",)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
	list_display = ("id", "country_name")

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
	list_display = ("id", "news_type", "heading","is_trending", "created_at", "updated_at", "country")
	list_filter = ("news_type", "country", "flag", "is_trending")
	search_fields = ("id",)

User = get_user_model()
admin.site.register(User)
