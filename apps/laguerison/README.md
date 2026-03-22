# laguerison

Application Django de gestion hospitalière intégrée au monorepo.

## Structure

- `backend/` : code Django de l'application

## Démarrage rapide

```powershell
cd apps/laguerison/backend
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python manage.py migrate
python manage.py runserver
```
