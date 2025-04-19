# Generated by Django 5.2 on 2025-04-19 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_receita_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='video_url',
            field=models.URLField(blank=True, help_text='Insira a URL do vídeo de preparo (YouTube, Vimeo, etc.)', null=True),
        ),
    ]
