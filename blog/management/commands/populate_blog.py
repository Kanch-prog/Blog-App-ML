import os
import csv
from datetime import datetime
from django.conf import settings
from django.core.management.base import BaseCommand
from blog.models import Post

class Command(BaseCommand):
    help = 'Populate the blog database with data from a CSV file'

    def handle(self, *args, **options):
        file_path = os.path.join(settings.BASE_DIR, 'blog', 'static', 'blog_data.csv')

        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                post = Post.objects.create(
                    title=row['title'],
                    author=row['author'],
                    content=row['content'],
                    published_date=datetime.strptime(row['published_date'], '%Y-%m-%d').date()
                )

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))
