from django.db import transaction, IntegrityError


def insert_transport(apps, schema_editor):
    try:
        Transport = apps.get_model('transportation', 'Transport')
        trans = Transport(model='ГАЗ-3302', number_and_region='П266АВ99', max_load_capacity=150,
                         max_loading_volume=10, status='Свободен', place='Москва',)
        Transport.objects.create(trans)
