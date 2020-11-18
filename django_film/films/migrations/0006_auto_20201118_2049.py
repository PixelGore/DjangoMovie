# Generated by Django 3.1 on 2020-11-18 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0005_auto_20201118_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='category',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='category',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='film',
            name='country_en',
        ),
        migrations.RemoveField(
            model_name='film',
            name='country_ru',
        ),
        migrations.RemoveField(
            model_name='film',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='film',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='film',
            name='tagline_en',
        ),
        migrations.RemoveField(
            model_name='film',
            name='tagline_ru',
        ),
        migrations.RemoveField(
            model_name='film',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='film',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='filmstills',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='filmstills',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='filmstills',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='filmstills',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='name_ru',
        ),
    ]