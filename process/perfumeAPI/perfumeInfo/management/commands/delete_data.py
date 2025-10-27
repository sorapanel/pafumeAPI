import csv
from django.core.management.base import BaseCommand, CommandError
from perfumeInfo.models import perfumeInfo, perfumeCategory

class Command(BaseCommand):
    help = 'Delete all data from perfumeInfo and perfumeCategory'
    
    def handle(self, *args, **options):
        perfumeInfo.objects.all().delete()
        perfumeCategory.objects.all().delete()