# Generated by Django 4.0.2 on 2022-03-28 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(blank=True, max_length=100)),
                ('product_id', models.IntegerField(blank=True, null=True)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('transaction_id', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'db_table': 'transaction_detail',
            },
        ),
    ]
