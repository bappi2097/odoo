# Generated by Django 5.0 on 2023-12-18 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.AlterField(
            model_name='entry',
            name='authors',
            field=models.ManyToManyField(to='author.author'),
        ),
    ]
