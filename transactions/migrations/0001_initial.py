# Generated by Django 4.2.7 on 2024-02-12 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('balance_after_transaction', models.DecimalField(decimal_places=2, max_digits=10)),
                ('borrow_timestamp', models.DateTimeField(auto_now_add=True)),
                ('return_timestamp', models.DateTimeField(auto_now=True)),
                ('borrowed_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='books.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='users.useraccount')),
            ],
        ),
    ]
