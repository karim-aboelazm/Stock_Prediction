# Generated by Django 3.1.7 on 2021-05-13 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210501_0027'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFollowedStocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_followed_stocks', models.CharField(max_length=30, unique=True)),
            ],
        ),
    ]
