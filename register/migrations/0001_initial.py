# Generated by Django 3.1.1 on 2020-09-28 17:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MainSurvey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('electric', models.IntegerField(max_length=10)),
                ('gas', models.IntegerField(max_length=10)),
                ('oil', models.IntegerField(max_length=10)),
                ('car', models.IntegerField(max_length=10)),
                ('flights', models.IntegerField(max_length=10)),
                ('newspaper', models.IntegerField(max_length=10)),
                ('aluminium', models.IntegerField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]