# Generated by Django 4.2 on 2023-05-04 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0004_news_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
    ]
