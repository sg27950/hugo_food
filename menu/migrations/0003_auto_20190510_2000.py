# Generated by Django 2.2.1 on 2019-05-10 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20190510_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='menu',
            field=models.ManyToManyField(related_name='categoryMenu', to='menu.Menu'),
        ),
    ]