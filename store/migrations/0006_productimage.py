# Generated by Django 5.0.6 on 2024-06-06 18:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_clothing_is_on_sale_alter_footwear_is_on_sale_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Nuotrauka')),
                ('clothing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='store.clothing', verbose_name='Drabužis')),
                ('footwear', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='store.footwear', verbose_name='Avalynė')),
                ('otherproduct', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='store.otherproduct', verbose_name='Kita')),
            ],
            options={
                'verbose_name': 'Prekės nuotrauka',
                'verbose_name_plural': 'Prekės nuotraukos',
            },
        ),
    ]
