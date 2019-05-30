from django.db import models
# Create your models here.


class TagsModel(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title


class CategoryModel(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title


class LogoModel(models.Model):
    title = models.CharField(max_length=120)
    images = models.TextField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    tags = models.ManyToManyField(TagsModel)
