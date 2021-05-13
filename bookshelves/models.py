from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class Shelf(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}: {self.name}'


class Book(models.Model):
    isbn = models.CharField(verbose_name='ISBN number', max_length=30)
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    spine_width = models.FloatField(max_length=5)
    spine_height = models.FloatField(max_length=5)
    spine_color = models.CharField(max_length=20)
    image = models.ImageField(default='default.jpg', upload_to='spine_photos')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

        img2 = img.resize((1, 1))
        color = img2.getpixel((0, 0))
        self.spine_color = '#{:02x}{:02x}{:02x}'.format(*color)
        super(Book, self).save(*args, **kwargs)
