from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsInGroupOrReadOnly
from .models import Patient, Consultation, Invoice, InvoiceLine, Payment, DailyReport
from .serializers import (
    PatientSerializer, ConsultationSerializer, InvoiceSerializer,
    InvoiceLineSerializer, PaymentSerializer, DailyReportSerializer
)

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all().order_by('-created_at')
    serializer_class = PatientSerializer
    permission_classes = [IsInGroupOrReadOnly]
    # allow writes to medical staff
    allowed_groups = ['infirmier', 'admin']

class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all().order_by('-created_at')
    serializer_class = ConsultationSerializer
    permission_classes = [IsInGroupOrReadOnly]
    allowed_groups = ['infirmier', 'admin']

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all().order_by('-created_at')
    serializer_class = InvoiceSerializer
    permission_classes = [IsInGroupOrReadOnly]
    allowed_groups = ['caissier', 'admin']

class InvoiceLineViewSet(viewsets.ModelViewSet):
    queryset = InvoiceLine.objects.all()
    serializer_class = InvoiceLineSerializer
    permission_classes = [IsInGroupOrReadOnly]
    allowed_groups = ['caissier', 'admin']

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all().order_by('-paid_at')
    serializer_class = PaymentSerializer
    permission_classes = [IsInGroupOrReadOnly]
    allowed_groups = ['caissier', 'admin']

class DailyReportViewSet(viewsets.ModelViewSet):
    queryset = DailyReport.objects.all().order_by('-date')
    serializer_class = DailyReportSerializer
    permission_classes = [IsInGroupOrReadOnly]
    allowed_groups = ['promoteur', 'admin']
