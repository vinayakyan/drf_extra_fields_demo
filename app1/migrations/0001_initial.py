# Generated by Django 4.1.1 on 2022-09-20 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('pro_pic', models.ImageField(blank=True, null=True, upload_to='pro_pics')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
