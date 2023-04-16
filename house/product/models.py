from django.db import models
from django.urls import reverse


class Customer(models.Model):
    title = models.CharField(max_length=300, verbose_name="Nomi")
    description = models.TextField(verbose_name="Mahsulot haqida")
    price = models.PositiveIntegerField()
    photo  = models.ImageField(upload_to='images/')
    create_at = models.DateTimeField(auto_now_add=True)
    cat = models.ForeignKey('Category', blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={"post_slug":self.pk})

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        ordering =['create_at', 'title']



class Category(models.Model):
    name = models.CharField(max_length=300, verbose_name="nomi")
    slug = models.SlugField(max_length=260, unique=True, verbose_name="Url", db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={"cat_id": self.pk})

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['id']




