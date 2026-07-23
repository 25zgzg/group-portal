from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('announcements', '0002_alter_announcement_id'),
    ]

    operations = [
        migrations.RunSQL(
            sql=[
                'PRAGMA foreign_keys = OFF;',
                'ALTER TABLE announcements_announcement RENAME TO announcements_announcement_old;',
                '''
                CREATE TABLE announcements_announcement (
                    id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
                    title varchar(200) NOT NULL,
                    content text NOT NULL,
                    created_at datetime NOT NULL,
                    is_pinned bool NOT NULL,
                    author_id bigint NOT NULL REFERENCES auth_user (id) DEFERRABLE INITIALLY DEFERRED
                );
                ''',
                '''
                INSERT INTO announcements_announcement
                    (id, title, content, created_at, is_pinned, author_id)
                SELECT id, title, content, created_at, is_pinned, author_id
                FROM announcements_announcement_old;
                ''',
                'DROP TABLE announcements_announcement_old;',
                'PRAGMA foreign_keys = ON;',
            ],
            reverse_sql=migrations.RunSQL.noop,
        ),
    ]