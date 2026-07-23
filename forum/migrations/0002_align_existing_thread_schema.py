import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.RemoveField(
                    model_name='thread',
                    name='description',
                ),
                migrations.AlterField(
                    model_name='thread',
                    name='creator',
                    field=models.ForeignKey(
                        db_column='created_by_id',
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='threads',
                        to='auth.user',
                        verbose_name='Автор',
                    ),
                ),
            ],
        ),
    ]