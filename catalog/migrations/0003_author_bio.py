# Generated by Django 2.0.2 on 2018-03-14 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='bio',
            field=models.TextField(help_text='Enter a brief bio of the author', max_length=1000, null=True),
        ),
    ]
