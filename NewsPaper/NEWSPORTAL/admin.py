from django.contrib import admin
from .models import Category, Post

def nullfy_quantity(modeladmin, request, queryset): # все аргументы уже должны быть вам знакомы,
    # самые нужные из них это request — объект хранящий информацию# о запросе и queryset — грубо говоря набор объектов,
    # которых мы выделили галочками.
    queryset.update(quantity=0)
nullfy_quantity.short_description = 'Обнулить товары' # описание для более понятного представления в админ панеле задаётся,
# как будто это объект
class ProductAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ('name', 'price', 'on_stock')  # оставляем только имя и цену товара
    list_filter = ('price', 'quantity', 'name')  # добавляем примитивные фильтры в нашу админку
    search_fields = ('name', 'category__name')  # тут всё очень похоже на фильтры из запросов в базу
# Register your models here.
admin.site.register(Category)
admin.site.register(Post,ProductAdmin)
