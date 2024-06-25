import os
import sys
import django
from django.apps import apps
from django.core import serializers

def export_db_to_json():
    # Pridėti projekto šaknies katalogą į sys.path
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    if project_root not in sys.path:
        sys.path.append(project_root)

    # Nustatyti aplinkos kintamuosius
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'system.settings')

    # Inicializuoti Django
    django.setup()

    # Sąrašas aplikacijų, kurias norite eksportuoti
    app_labels = ['store', 'users', 'orders']

    for app_label in app_labels:
        app_config = apps.get_app_config(app_label)
        file_path = f'{app_label}_data.json'
        with open(file_path, 'w', encoding='utf-8') as f:
            for model in app_config.get_models():
                if model._meta.abstract:
                    continue
                data = serializers.serialize('json', model.objects.all())
                f.write(data)
                f.write('\n')  # Pridėti naują eilutę tarp modelių duomenų

if __name__ == "__main__":
    export_db_to_json()

# Paleidimas
# python scripts/export_db.py