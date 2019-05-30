from django.contrib import admin
from api.models import CategoryModel, TagsModel, LogoModel
# Register your models here.
admin.site.register(CategoryModel)
admin.site.register(TagsModel)
admin.site.register(LogoModel)
