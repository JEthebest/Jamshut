# Generated by Django 4.1.6 on 2023-02-24 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('markets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(blank=True, max_length=225, null=True, verbose_name='')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('MAN', 'Man'), ('WOMAN', 'Woman'), ('BI', 'Bi'), ('OTHER', 'Other')], default='OTHER', max_length=20)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markets.location')),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(blank=True, max_length=225, null=True, verbose_name='')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('MAN', 'Man'), ('WOMAN', 'Woman'), ('BI', 'Bi'), ('OTHER', 'Other')], default='OTHER', max_length=20)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markets.location')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_name', models.CharField(blank=True, max_length=225, null=True, verbose_name='')),
                ('date', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.customer')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.employee')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markets.product')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
    ]
