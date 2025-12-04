from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'
        ordering = ['-created_at']



class Author(models.Model):
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title} {self.id}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'