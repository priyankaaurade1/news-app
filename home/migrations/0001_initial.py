# Generated by Django 3.2.11 on 2022-09-23 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('url', models.CharField(max_length=1000)),
                ('urlToImage', models.CharField(max_length=1000)),
                ('publishedAt', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
    ]