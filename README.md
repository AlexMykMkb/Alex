# Monorepo multi-applications

Ce dépôt sert à héberger plusieurs applications dans un seul repo Git.

## Structure

- `apps/` : chaque application dans son propre dossier
- `shared/` : bibliothèques communes, composants réutilisables
- `docs/` : documentation globale

## Ajouter une nouvelle application

PowerShell:

```powershell
.\scripts\add-app.ps1 -Name mon_app
```

## Bonnes pratiques

- Une app = un dossier sous `apps/`
- Chaque app a son propre `README.md`
- Variables sensibles dans `.env` (jamais commit)
- Commits petits et fréquents
