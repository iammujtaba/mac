# Generated by Django 2.2.4 on 2019-09-28 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proudct',
            name='product_catogery',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='proudct',
            name='product_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='proudct',
            name='product_sub_catogery',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='proudct',
            name='proudct_image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
    ]
