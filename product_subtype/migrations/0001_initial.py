# Generated by Django 4.0.2 on 2022-03-28 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product_type', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField(blank=True, null=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_type.type')),
            ],
            options={
                'verbose_name': 'SubType',
                'verbose_name_plural': 'SubTypes',
                'db_table': 'product_subtype',
                'managed': True,
            },
        ),
    ]
