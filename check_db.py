import os
import sys
import django

# Add the app directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from drivers.models import Driver
from races.models import Race, RaceResult

print(f'Drivers: {Driver.objects.count()}')
print(f'Races: {Race.objects.count()}')
print(f'Results: {RaceResult.objects.count()}')

if Race.objects.exists():
    print("\nRaces in database:")
    for race in Race.objects.all()[:5]:
        print(f"  - {race.name} ({race.year})")
