# Generated by Django 4.0.2 on 2022-03-28 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('users_id', models.IntegerField(blank=True, null=True)),
                ('address', models.TextField(blank=True)),
                ('province', models.CharField(blank=True, max_length=100)),
                ('regencie', models.CharField(blank=True, max_length=100)),
                ('district', models.CharField(blank=True, max_length=100)),
                ('postal_code', models.CharField(blank=True, max_length=100)),
                ('maps', models.CharField(blank=True, max_length=100)),
                ('long', models.CharField(blank=True, max_length=100)),
                ('lat', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'users_address',
            },
        ),
    ]
