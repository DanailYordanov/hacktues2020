# Generated by Django 2.2.15 on 2020-10-04 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(default='asd', max_length=30),
            preserve_default=False,
        ),
    ]
