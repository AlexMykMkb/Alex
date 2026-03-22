# LA GUÉRISON — Système de gestion simplifié

Scaffold Django minimal pour gérer la circulation d'informations : consultation, facturation, caisse, rapports journaliers.

Quick start (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

URL publique temporaire:

```powershell
.\start_public.ps1
```

Fonctionnalités incluses dans ce scaffold:
- Modèles: Patient, Consultation, Invoice, InvoiceLine, Payment, DailyReport
- Admin Django pour gestion rapide

Prochaine étape: initialiser Git et faire le commit initial.
