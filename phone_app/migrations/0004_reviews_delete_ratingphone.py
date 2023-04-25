# Generated by Django 4.2 on 2023-04-25 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phone_app', '0003_alter_phones_options_ratingphone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500, null=True, verbose_name='Комментарий')),
                ('rate', models.IntegerField(choices=[(1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****')], null=True, verbose_name='Оценка')),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('choice_film', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='phone_app.phones')),
            ],
        ),
        migrations.DeleteModel(
            name='RatingPhone',
        ),
    ]
