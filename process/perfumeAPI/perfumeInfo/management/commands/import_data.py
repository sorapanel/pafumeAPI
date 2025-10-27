import csv
from django.core.management.base import BaseCommand, CommandError
from perfumeInfo.models import perfumeInfo, perfumeCategory

class Command(BaseCommand):
    help = 'Imports perfume data from a CSV file.'
    def add_arguments(self, parser):
        parser.add_argument('perfumeInfo_v2', type=str, help='The path to the CSV file')

    def handle(self, *args, **options):
        csv_file_path = options['perfumeInfo_v2']

        try:
            with open(csv_file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        categories = row['category'].split('/')

                        for c in categories:
                            if not perfumeCategory.objects.filter(category=c).exists():
                                perfumeCategory.objects.create(
                                    category = c,
                                )
                        
                        perfume_item = perfumeInfo.objects.create(
                        title = row['title'],
                        brand = row['brand'],
                        brandJp = row['brandJp'],
                        description = row['description']
                        )

                        categories_objects = perfumeCategory.objects.filter(category__in=categories)

                        perfume_item.categories.set(categories_objects)
                        perfume_item.save()

                    except Exception as e:
                        raise CommandError(f'An error occurred during importing data: {e}')
        except Exception as e:
            raise CommandError(f'An error occurred during opening file: {e}')