from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from core.models import Patient, Consultation, Invoice, InvoiceLine, Payment, DailyReport
from django.utils import timezone
import random

User = get_user_model()


class Command(BaseCommand):
    help = 'Seed demo data: groups, users, sample patients, consultations, invoices'

    def handle(self, *args, **options):
        # Create groups
        groups = ['infirmier', 'caissier', 'promoteur']
        for g in groups:
            Group.objects.get_or_create(name=g)
        self.stdout.write('Groups created')

        # Create demo users
        if not User.objects.filter(username='nurse').exists():
            nurse = User.objects.create_user('nurse', email='nurse@example.com', password='Nurse123!')
            nurse.groups.add(Group.objects.get(name='infirmier'))
        if not User.objects.filter(username='cashier').exists():
            cashier = User.objects.create_user('cashier', email='cashier@example.com', password='Cashier123!')
            cashier.groups.add(Group.objects.get(name='caissier'))
        if not User.objects.filter(username='promoter').exists():
            promoter = User.objects.create_user('promoter', email='promoter@example.com', password='Promote123!')
            promoter.groups.add(Group.objects.get(name='promoteur'))
        self.stdout.write('Demo users created: nurse/cashier/promoter (passwords: Nurse123!, Cashier123!, Promote123!)')

        # Create patients
        patients = []
        for i in range(1, 6):
            p, _ = Patient.objects.get_or_create(first_name=f'Patient{i}', last_name='Demo', phone=f'+1000000{i}')
            patients.append(p)
        self.stdout.write(f'Created {len(patients)} patients')

        # Create consultations
        for p in patients:
            Consultation.objects.get_or_create(patient=p, notes='Examen initial de démonstration')
        self.stdout.write('Consultations created')

        # Create invoices and lines
        for p in patients:
            inv = Invoice.objects.create(patient=p)
            InvoiceLine.objects.create(invoice=inv, description='Consultation', amount=10.00, quantity=1)
            InvoiceLine.objects.create(invoice=inv, description='Médicament', amount=5.50, quantity=2)
            # create a payment for some
            if random.choice([True, False]):
                Payment.objects.create(invoice=inv, paid_amount=inv.total(), received_by=User.objects.filter(username='cashier').first())
        self.stdout.write('Invoices and payments created')

        # Create a daily report
        DailyReport.objects.get_or_create(date=timezone.now().date(), created_by=User.objects.filter(username='promoter').first(), total_collected=100.0, deposited=False)
        self.stdout.write('Daily report created')
