# Generated by Django 3.1.5 on 2021-02-24 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_personel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Kategori adini giriniz', max_length=50, null=True, verbose_name='Kategori')),
                ('slug', models.SlugField(null=True, unique=True)),
            ],
        ),
    ]
