# Generated by Django 4.0.4 on 2022-04-25 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_articletag_article_alter_articletag_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articletag',
            name='is_main',
            field=models.BooleanField(blank=True, verbose_name='Основной'),
        ),
    ]
