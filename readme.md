# Fast Food Gasy Backend

Backend REST API développé avec **Django** et **Django REST Framework** pour la gestion d'un service de restauration Fast Food.

Le projet utilise PostgreSQL pour la base de données, Docker pour la conteneurisation et GitHub Actions pour l'intégration et le déploiement continus.

---

## Technologies utilisées

* Python 3.12
* Django 5.2
* Django REST Framework
* PostgreSQL
* Simple JWT
* Pytest
* Docker
* Docker Compose
* GitHub Actions
* GitHub Container Registry
* Gunicorn

---

## Architecture du projet

```text
fast_food_gasy_backend_django/
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── cd.yml
│
├── fast_food_gasy/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── menu/
│   ├── migrations/
│   ├── templates/
│   │   └── menu/
│   │       └── index.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── tests/
│   ├── test_admin.py
│   ├── test_apps.py
│   ├── test_asgi.py
│   ├── test_models.py
│   ├── test_serializers.py
│   ├── test_urls.py
│   ├── test_views.py
│   └── test_wsgi.py
│
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── manage.py
├── requirements.txt
└── README.md
```

---

# Fonctionnement de l'application

L'application Django contient une application `menu` permettant de gérer :

* les tacos ;
* les ingrédients des tacos ;
* les pizzas ;
* les ingrédients des pizzas ;
* les boissons ;
* les informations de contact ;
* les photos.

---

# Modèles

Les principaux modèles sont :

```text
Ingredient_tacos
Tacos

Ingredient_pizza
Pizzas

Boissons

Contact

Photo
```

Les tacos et les pizzas possèdent une relation `ManyToMany` avec leurs ingrédients.

---

# API REST

Le projet utilise Django REST Framework.

Les serializers permettent de convertir les modèles Django en données JSON et inversement.

Exemple :

```python
class TacosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tacos
        fields = "__all__"
```

---

# Authentification JWT

Le projet utilise Simple JWT pour l'authentification des API.

Les endpoints principaux sont :

```text
/api/token/
/api/token/refresh/
```

Le projet possède également des `ModelViewSet` protégés par :

```python
IsAuthenticatedOrReadOnly
```

Cela permet notamment :

* aux utilisateurs non authentifiés de consulter les données ;
* aux utilisateurs authentifiés de modifier les données selon les permissions configurées.

---

# Tests

Les tests sont réalisés avec Pytest et pytest-django.

La structure des tests est :

```text
tests/
├── test_admin.py
├── test_apps.py
├── test_asgi.py
├── test_models.py
├── test_serializers.py
├── test_urls.py
├── test_views.py
└── test_wsgi.py
```

Pour lancer tous les tests :

```bash
pytest -v
```

Pour lancer uniquement les tests des modèles :

```bash
pytest tests/test_models.py -v
```

Pour tester les API :

```bash
pytest tests/test_views.py -v
```

---

# Installation locale

## 1. Cloner le projet

```bash
git clone https://github.com/Mamy-cloud/fast_food_gasy_backend_django.git
```

Entrer dans le projet :

```bash
cd fast_food_gasy_backend_django
```

---

## 2. Créer l'environnement virtuel

```bash
python3 -m venv venv
```

Activer l'environnement :

```bash
source venv/bin/activate
```

---

## 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

Installer les outils de test :

```bash
pip install pytest pytest-django
```

---

## 4. Configurer les variables d'environnement

Créer un fichier :

```text
.env
```

Exemple :

```env
DEBUG=True

SECRET_KEY=change-me

DB_NAME=fast_food_gasy
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

Le fichier `.env` ne doit jamais être envoyé sur GitHub.

---

# Migrations Django

Créer les migrations :

```bash
python manage.py makemigrations
```

Appliquer les migrations :

```bash
python manage.py migrate
```

---

# Lancer l'application localement

```bash
python manage.py runserver
```

L'application sera disponible sur :

```text
http://127.0.0.1:8000/
```

---

# Docker

Le projet peut être exécuté avec Docker Compose.

Construire les conteneurs :

```bash
docker compose build
```

Démarrer l'application :

```bash
docker compose up -d
```

Afficher les conteneurs :

```bash
docker compose ps
```

Afficher les logs :

```bash
docker compose logs -f web
```

Arrêter les conteneurs :

```bash
docker compose down
```

---

# Architecture Docker

```text
                    Docker Compose
                         │
              ┌──────────┴──────────┐
              │                     │
              ▼                     ▼
       Django / Gunicorn       PostgreSQL
       port 8000                    │
              │                     │
              └──────────┬──────────┘
                         │
                    PostgreSQL
                     Volume
```

Les données PostgreSQL sont conservées dans un volume Docker :

```text
postgres_data
```

Les fichiers statiques et médias utilisent également des volumes :

```text
static_volume
media_volume
```

---

# CI - Continuous Integration

Le workflow :

```text
.github/workflows/ci.yml
```

est exécuté lors d'un `push` ou d'une Pull Request.

Le processus est :

```text
Git Push
   │
   ▼
GitHub Actions
   │
   ├── Installation Python
   │
   ├── Installation des dépendances
   │
   ├── Démarrage PostgreSQL
   │
   ├── Django Check
   │
   ├── Django Migrations
   │
   ├── Pytest
   │
   └── Vérification des migrations
```

Si un test échoue, le pipeline CI échoue également.

---

# CD - Continuous Deployment

Le workflow :

```text
.github/workflows/cd.yml
```

est exécuté après la réussite du workflow CI sur la branche `main`.

Le processus est :

```text
CI réussi
    │
    ▼
Build Docker
    │
    ▼
GitHub Container Registry
    │
    ▼
Connexion SSH au serveur
    │
    ▼
docker compose pull
    │
    ▼
docker compose up -d
    │
    ▼
Application déployée
```

---

# GitHub Container Registry

L'image Docker est publiée dans :

```text
ghcr.io/mamy-cloud/fast_food_gasy_backend_django
```

Deux tags sont utilisés :

```text
latest
```

et :

```text
commit SHA
```

Le SHA permet d'identifier précisément la version déployée.

---

# Déploiement serveur

Le serveur doit disposer de :

* Linux ;
* Docker ;
* Docker Compose ;
* accès SSH.

Le projet est placé par exemple dans :

```text
/opt/fast-food-gasy
```

Le serveur utilise ensuite :

```bash
docker compose pull
docker compose up -d
```

pour récupérer et démarrer la nouvelle version.

---

# Secrets GitHub Actions

Les informations sensibles ne sont pas stockées dans le code.

Les secrets nécessaires sont :

```text
SERVER_HOST
SERVER_USER
SERVER_SSH_KEY

GHCR_USERNAME
GHCR_TOKEN
```

Les secrets permettent à GitHub Actions de :

* se connecter au registry ;
* accéder au serveur ;
* déployer automatiquement l'application.

---

# Sécurité

Les fichiers suivants ne doivent jamais être commités :

```text
.env
*.pem
*.key
```

Les mots de passe, clés API, tokens et clés SSH doivent être stockés dans :

```text
GitHub Secrets
```

ou dans les variables d'environnement du serveur.

---

# Workflow de développement

Le workflow recommandé est :

```text
1. Développement local
        │
        ▼
2. Tests pytest
        │
        ▼
3. git add .
        │
        ▼
4. git commit
        │
        ▼
5. git push
        │
        ▼
6. GitHub Actions CI
        │
        ├── ❌ Tests échoués → correction
        │
        └── ✅ Tests réussis
                    │
                    ▼
              7. Build Docker
                    │
                    ▼
              8. Push GHCR
                    │
                    ▼
              9. Déploiement
                    │
                    ▼
             10. Docker Compose
                    │
                    ▼
              Application en ligne
```

---

# Objectif du projet

Ce projet démontre l'utilisation d'une architecture moderne basée sur :

```text
Django
    +
Django REST Framework
    +
PostgreSQL
    +
JWT
    +
Pytest
    +
Docker
    +
Docker Compose
    +
GitHub Actions
    +
GitHub Container Registry
    +
Déploiement SSH
```

Il constitue également un exemple de mise en pratique des principes **CI/CD et DevOps** sur une application web Django.

```
```
