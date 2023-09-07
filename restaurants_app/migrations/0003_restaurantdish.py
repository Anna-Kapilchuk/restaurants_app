# Generated by Django 4.2.4 on 2023-08-29 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants_app', '0002_alter_restaurant_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantDish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='restaurants_app.restaurant')),
            ],
            options={
                'db_table': 'restaurant_dishes',
            },
        ),
    ]
