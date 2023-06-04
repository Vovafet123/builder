from django.db import transaction, IntegrityError


def insert_transport(apps, schema_editor):
    Transport = apps.get_model('transportation', 'Transport')
    Transport.objects.create(model='ГАЗ-3302', number_and_region='П266АВ99', max_load_capacity=40,
                            max_loading_volume=100, status='WAIT', place='Москва',)
