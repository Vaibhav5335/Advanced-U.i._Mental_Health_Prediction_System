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
            name='PredictionResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=10)),
                ('sleep_hours', models.FloatField()),
                ('study_hours', models.FloatField()),
                ('meals_per_day', models.IntegerField()),
                ('social_media_hours', models.FloatField()),
                ('physical_activity_hours', models.FloatField()),
                ('substance_use', models.CharField(max_length=10)),
                ('academic_percentage', models.FloatField()),
                ('predicted_category', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
