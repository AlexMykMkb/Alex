from rest_framework import routers
from .api import (
    PatientViewSet, ConsultationViewSet, InvoiceViewSet,
    InvoiceLineViewSet, PaymentViewSet, DailyReportViewSet
)
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'consultations', ConsultationViewSet)
router.register(r'invoices', InvoiceViewSet)
router.register(r'invoice-lines', InvoiceLineViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'daily-reports', DailyReportViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
