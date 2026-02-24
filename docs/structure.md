# B3_EPSI_MSPR_2026
projet-mspr/
│
├── api/                        # API FastAPI
│   ├── app/
│   │   ├── main.py             # Point d’entrée FastAPI
│   │   ├── core/               # Config, sécurité, JWT
│   │   │   ├── config.py
│   │   │   └── security.py
│   │   ├── db/                 # Connexion DB
│   │   │   ├── session.py
│   │   │   └── base.py
│   │   ├── models/             # Modèles SQLAlchemy (app_*)
│   │   ├── schemas/            # Schémas Pydantic
│   │   ├── routes/             # Endpoints API
│   │   │   ├── auth.py
│   │   │   ├── users.py
│   │   │   ├── dashboard.py
│   │   │   └── exports.py
│   │   └── services/           # Logique métier
│   ├── tests/                  # Tests API
│   ├── Dockerfile
│   └── requirements.txt
│
├── etl/                        # Ingestion des données (ETL)
│   ├── ingest/
│   │   ├── source_1.py
│   │   └── source_2.py
│   ├── run_all.py              # Lance toutes les ingestions
│   ├── utils/                  # Fonctions communes (logs, helpers)
│   ├── Dockerfile
│   └── requirements.txt
│
├── transform/                  # Nettoyage & qualité
│   ├── clean/
│   │   ├── clean_source_1.py
│   │   └── clean_source_2.py
│   ├── quality/
│   │   └── checks.py           # Règles qualité / tests
│   ├── run_all.py
│   └── requirements.txt
│
├── data/
│   ├── raw/                    # Données brutes (optionnel)
│   ├── staging/                # Données staging (debug)
│   └── exports/                # CSV / JSON finaux
│
├── db/
│   ├── migrations/             # Alembic
│   ├── alembic.ini
│   └── init.sql                # Init DB si besoin
│
├── frontend/                   # Frontend Nuxt.js (dashboard admin)
│   ├── app.vue
│   ├── pages/
│   │   ├── login.vue
│   │   ├── index.vue           # Dashboard
│   │   ├── quality.vue
│   │   └── exports.vue
│   ├── components/
│   ├── services/               # Appels API
│   ├── middleware/             # Guard auth
│   ├── nuxt.config.ts
│   ├── Dockerfile
│   └── package.json
│
├── infra/                      # DevOps / orchestration
│   ├── docker-compose.yml
│   ├── cron/
│   │   └── etl-cron            # Planification ETL
│   └── .env.example
│
├── docs/                       # Documentation projet
│   ├── cahier_des_charges_backend.md
│   ├── installation.md
│   ├── architecture.md
│   ├── api.md
│   ├── data_quality.md
│   └── sources.md
│
├── Makefile                    # Commandes simplifiées
├── README.md                   # README principal
└── .gitignore