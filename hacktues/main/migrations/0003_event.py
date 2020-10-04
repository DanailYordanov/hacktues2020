# Generated by Django 2.2.15 on 2020-10-04 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_room_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('event', models.CharField(max_length=100)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Room')),
            ],
        ),
    ]