# Generated by Django 2.1.5 on 2019-12-18 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(help_text='Enter the book title.', max_length=200),
        ),
    ]
