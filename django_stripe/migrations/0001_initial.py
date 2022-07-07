# Generated by Django 3.2.5 on 2022-07-06 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_image', models.ImageField(upload_to='thumbnail')),
                ('book_url', models.URLField()),
            ],
        ),
    ]