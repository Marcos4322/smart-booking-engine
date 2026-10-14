# AGENTS.md

## Stack del Proyecto
- **Backend**: Python 3 con Django 5.2 (LTS), ubicado en la carpeta `backend/`.
- **Frontend**: Vue 3 + Vite + Tailwind CSS v3, ubicado en la carpeta `frontend/`.
- **Base de datos**: SQLite3 (por defecto para desarrollo local).

## Cómo arrancar en local
- **Backend**: `cd backend`, activar el entorno virtual (`env\Scripts\activate` en Windows o `source env/bin/activate` en Linux/Mac), y ejecutar `python manage.py runserver`.
- **Frontend**: `cd frontend` y ejecutar `npm run dev`.

## Convenciones del equipo (Vivecoding)
- Commits en español, en imperativo ("añade", "corrige", "modifica").
- No tocar la rama `main` directamente: trabajamos en ramas `feature/...` o `develop`.
- Nunca subir secretos reales ni la base de datos `db.sqlite3` a GitHub.
- La carpeta del entorno virtual (`env/`) debe estar siempre ignorada en el `.gitignore`.

## Qué NO debe hacer el agente sin preguntar
- No ejecutar `git push`, `git push --force` ni borrar ramas.
- No instalar dependencias nuevas sin decirlo explícitamente en el prompt en modo Plan.
- No modificar el código de Vue cuando se le pidan tareas de Django, a menos que se especifique.