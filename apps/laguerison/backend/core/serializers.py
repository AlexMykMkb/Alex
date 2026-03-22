from rest_framework import serializers
from .models import Patient, Consultation, Invoice, InvoiceLine, Payment, DailyReport

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'first_name', 'last_name', 'date_of_birth', 'phone', 'created_at']

class ConsultationSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    patient_id = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all(), write_only=True, source='patient')

    class Meta:
        model = Consultation
        fields = ['id', 'patient', 'patient_id', 'attended_by', 'notes', 'created_at']

class InvoiceLineSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = InvoiceLine
        fields = ['id', 'description', 'amount', 'quantity', 'total']

    def get_total(self, obj):
        return obj.total()

class InvoiceSerializer(serializers.ModelSerializer):
    lines = InvoiceLineSerializer(many=True, read_only=True)
    patient = PatientSerializer(read_only=True)
    patient_id = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all(), write_only=True, source='patient')
    total = serializers.SerializerMethodField()

    class Meta:
        model = Invoice
        fields = ['id', 'patient', 'patient_id', 'created_at', 'is_paid', 'lines', 'total']

    def get_total(self, obj):
        return obj.total()

class PaymentSerializer(serializers.ModelSerializer):
    invoice = InvoiceSerializer(read_only=True)
    invoice_id = serializers.PrimaryKeyRelatedField(queryset=Invoice.objects.all(), write_only=True, source='invoice')

    class Meta:
        model = Payment
        fields = ['id', 'invoice', 'invoice_id', 'paid_amount', 'paid_at', 'received_by']

class DailyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyReport
        fields = ['id', 'date', 'created_by', 'total_collected', 'deposited', 'created_at']
