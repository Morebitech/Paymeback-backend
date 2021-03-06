# Generated by Django 3.2.6 on 2021-08-25 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lender', models.CharField(max_length=250)),
                ('receiver', models.CharField(max_length=250)),
                ('date', models.DateField()),
                ('amount', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=0)),
                ('amount_paid', models.IntegerField(default=0)),
                ('amount_due', models.IntegerField(default=0)),
                ('transactor', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
        ),
    ]
