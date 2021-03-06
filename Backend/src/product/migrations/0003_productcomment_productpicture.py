# Generated by Django 3.0.3 on 2020-03-05 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200305_2304'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whole_view', models.ImageField(upload_to='')),
                ('top_view', models.ImageField(upload_to='')),
                ('side_view', models.ImageField(upload_to='')),
                ('inner_view', models.ImageField(upload_to='')),
                ('PID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('review', models.DecimalField(decimal_places=1, max_digits=2)),
                ('PID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
        ),
    ]
