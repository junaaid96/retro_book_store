# Generated by Django 4.2.7 on 2024-02-15 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('books', '0003_remove_book_borrowed_by_book_borrowed_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='borrowed_by',
            field=models.ManyToManyField(blank=True, related_name='borrowed_book', to='users.useraccount'),
        ),
    ]
