

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='image_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
