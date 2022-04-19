# Generated by Django 4.0.2 on 2022-03-28 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'ProductSku',
                'verbose_name_plural': 'ProductSkus',
                'db_table': 'product_sku',
                'managed': True,
            },
        ),
    ]