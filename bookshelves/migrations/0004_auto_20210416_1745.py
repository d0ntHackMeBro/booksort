# Generated by Django 3.1.7 on 2021-04-16 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelves', '0003_auto_20210406_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='spine_color',
            field=models.CharField(max_length=20),
        ),
    ]
