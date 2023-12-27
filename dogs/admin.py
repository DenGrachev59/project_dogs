from django.contrib import admin

from dogs.models import Dog, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description',)

    search_fields = ('name', 'category', 'birth_day')


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'category', 'birth_day',)
    list_filter = ('category',)
    search_fields = ('name', 'category', 'birth_day')
