# Generated by Django 4.2 on 2023-05-03 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='human',
            options={'ordering': ['id'], 'verbose_name': 'людей', 'verbose_name_plural': 'Люди'},
        ),
        migrations.AlterField(
            model_name='human',
            name='Last_name',
            field=models.TextField(blank=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='human',
            name='Name',
            field=models.CharField(max_length=150, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='human',
            name='age',
            field=models.IntegerField(verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='human',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Публикация'),
        ),
        migrations.AlterField(
            model_name='human',
            name='photo',
            field=models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='human',
            name='profession',
            field=models.CharField(max_length=150, verbose_name='Профессия'),
        ),
    ]
