# Project and Skill Data for the Landing Page

SKILLS = [
    {
        "id": "automation",
        "name": "Automation",
        "theme_color": "alpine-ice",
        "icons": [
            {"name": "Bash", "id": "bash"},
            {"name": "PowerShell", "id": "powershell"},
            {"name": "Python", "id": "python"},
            {"name": "Selenium", "id": "selenium"}
        ]
    },
    {
        "id": "web",
        "name": "Web & Backend",
        "theme_color": "blue-500",
        "icons": [
            {"name": "Flask", "id": "flask"},
            {"name": "Redis", "id": "redis"},
            {"name": "SQLite", "id": "sqlite"},
            {"name": "Tailwind", "id": "tailwind"}
        ]
    },
    {
        "id": "data",
        "name": "Data & Databases",
        "theme_color": "white",
        "icons": [
            {"name": "Data Cleaning", "url": "/static/images/data_cleaning_small.webp"},
            {"name": "PostgreSQL", "id": "postgresql"},
            {"name": "SQL", "id": "mysql"}, # fallback icon
            {"name": "SQLAlchemy", "url": "/static/images/sqlalchemy.svg"}
        ]
    },
    {
        "id": "system",
        "name": "System & DevOps",
        "theme_color": "indigo-500",
        "icons": [
            {"name": "C", "id": "c"},
            {"name": "Docker", "id": "docker"},
            {"name": "Linux", "id": "linux"},
            {"name": "Git", "id": "git"}
        ]
    },
    {
        "id": "api",
        "name": "APIs & AI",
        "theme_color": "purple-500",
        "icons": [
            {"name": "Discord API", "id": "discord"},
            {"name": "Gemini", "url": "/static/images/gemini.svg"},
            {"name": "Vision API", "id": "opencv"}, # fallback
            {"name": "Groq", "url": "/static/images/groq.png"}
        ]
    }
]

PROJECTS = [
    {
        "id": "auriga2google",
        "image": "auriga2google_landing_page.png",
        "name": "AURIGA2GOOGLE",
        "url": "https://auriga2google.pierref.eu",
        "category": "DEPLOYMENTS",
        "badge": "EPITA_Sync_V1",
        "year": "2026",
        "description": "Synchronisation automatique et sur-mesure du planning Auriga EPITA vers Google Calendar. Nettoyage des titres de cours, pastilles de couleur par type d'événement et flux iCalendar permanent.",
        "tags": ["FastAPI", "Python", "iCalendar", "PostgreSQL", "EPITA", "OAuth2", "Sync"],
        "theme_color": "brand-blue",
        "cta": "SYNC_CALENDAR"
    },

    {
        "id": "opticars",
        "image": "opticars__landing_page.png",
        "name": "OPTICARS",
        "url": "https://opticars.pierref.eu",
        "category": "DEPLOYMENTS",
        "badge": "Optimized_Algo",
        "year": "2024-2026",
        "description": "Algorithme de tri multicritère automobile. Calcul de rentabilité, fiches techniques 5000+ véhicules, répertoire des 97 marques et gains Stage 1/2.",
        "tags": ["Python", "Flask", "Docker", "Automobile", "Calculateur ROI", "Performance", "Stage 1"],
        "theme_color": "green-500",
        "custom_template": "partials/cards/opticars.html",
        "cta": "RUN_CALC"
    },

    {
        "id": "streetsraces",
        "image": "streetrace_landing.png",
        "name": "STREETSRACE",
        "url": "https://streetsrace.pierref.eu",
        "category": "DEPLOYMENTS",
        "badge": "Route_Engine_V2",
        "year": "2026",
        "description": "Analyseur autonome de tracés routiers et Touges sur OpenStreetMap. Filtrage géométrique, scoring de sinuosité, raquettes de retournement et chronométrage GPS.",
        "tags": ["Python", "OSMnx", "GeoPandas", "Leaflet", "Touge", "GPS", "Cartographie"],
        "theme_color": "brand-red",
        "custom_template": "partials/cards/streetsraces.html",
        "cta": "ANALYZE_ROADS"
    },

    {
        "id": "musicator",
        "image": "musicator_landing_page.png",
        "name": "MUSICATOR",
        "url": "https://musicator.pierref.eu",
        "category": "DEPLOYMENTS",
        "badge": "Viral_Scraper_3X",
        "year": "2026",
        "description": "Générateur intelligent 3X de playlists virales TikTok vers YouTube. Analyse des requêtes dans les commentaires, résolution de pochette et publication autonome.",
        "tags": ["Python", "Docker", "TikTok", "YouTube", "Scraping", "Musique", "Playlists"],
        "theme_color": "brand-orange",
        "custom_template": "partials/cards/musicator.html",
        "cta": "GENERATE_PLAYLIST"
    },

    {
        "id": "matchshot",
        "image": "matchshotlanding_page.png",
        "name": "MATCHSHOT",
        "url": "https://matchshot.pierref.eu",
        "category": "DEPLOYMENTS",
        "badge": "Vision_Analytics",
        "year": "2026",
        "description": "Plateforme analytique de Computer Vision & télémétrie en temps réel pour l'esport et le tracking vidéo haute précision.",
        "tags": ["Python", "OpenCV", "IA", "Esports", "WebSockets", "Computer Vision", "Analytics"],
        "theme_color": "brand-gold",
        "cta": "EXPLORE_VISION"
    },

    {
        "id": "humanizator",
        "image": "humanizatorlanding_page.png",
        "name": "HUMANIZATOR",
        "url": "https://humanizator.pierref.eu",
        "category": "DEPLOYMENTS",
        "badge": "AI_HUMANIZER",
        "year": "2026",
        "description": "Générateur d'anomalies stochastiques pour textes & code IA. Injection d'erreurs de frappe euclidiennes et variations de débit préservant la syntaxe.",
        "tags": ["Python", "FastAPI", "Tailwind", "IA", "Text Generation", "NLP"],
        "theme_color": "cyan-400",
        "custom_template": "partials/cards/humanizator.html",
        "cta": "HUMANIZE_NOW"
    },

    {
        "id": "creepita",
        "image": "creepita_landing_page.png",
        "name": "CREEPITA",
        "url": "https://creepita.pierref.eu",
        "category": "DEPLOYMENTS",
        "badge": "Core_Engine",
        "year": "v1.1",
        "description": "Jeu d'horreur et d'énigmes en Python pur (POO & Pygame) avec moteur multijoueur Amagachi et protocoles réseau dédiés.",
        "tags": ["Python", "Pygame", "POO", "Amagachi", "Multijoueur", "Gaming", "Réseau"],
        "theme_color": "brand-red",
        "custom_template": "partials/cards/creepita.html",
        "cta": "PLAY_DEMO"
    },

    {
        "id": "mailer",
        "image": "nexumail__landing_page.png",
        "name": "MAILER PRO (GRATUIT)",
        "url": "https://mailer.pierref.eu",
        "category": "DEPLOYMENTS",
        "badge": "Outil_Gratuit_Pros",
        "year": "2026",
        "description": "L'outil gratuit d'automatisation emailing pour les professionnels et indépendants. Moteur anti-bannissement, quota gratuit 50 mails/jour et parrainage.",
        "tags": ["Python", "Emailing", "Anti-Ban", "Automation", "Pro", "Docker", "SaaS"],
        "theme_color": "brand-gold",
        "custom_template": "partials/cards/mailer.html",
        "cta": "ACCÉDER_GRATUITEMENT"
    },

    {
        "id": "cleaning_windows",
        "image": "cwl_landing_page.png",
        "name": "CLEANING WINDOWS",
        "url": "https://cwl.pierref.eu",
        "category": "DEPLOYMENTS",
        "badge": "Operational_ROI",
        "year": "PROFITABLE",
        "description": "Activité commerciale réelle et rentable. Modèle à forte rentabilité opérationnelle optimisé sur 2 années de pratique terrain.",
        "tags": ["Business", "Rentabilité", "Operations", "Auto-Entrepreneur", "B2B", "Finances"],
        "theme_color": "white",
        "custom_template": "partials/cards/cleaning_windows.html",
        "cta": "HQ_PORTAL"
    },

    {
        "id": "sharator",
        "image": "sharator_landing_page.png",
        "name": "SHARATOR",
        "url": "https://sharator.pierref.eu",
        "category": "DEPLOYMENTS",
        "badge": "Legal_Tech",
        "year": "Fullstack",
        "description": "Allocation de capital et génération légale de PDF contractuels. Méthodologie Slicing Pie pour distribution dynamique d'equity.",
        "tags": ["Python", "Flask", "SQLAlchemy", "PostgreSQL", "LegalTech", "Equity", "Slicing Pie"],
        "theme_color": "rose-500",
        "custom_template": "partials/cards/sharator.html",
        "cta": "MANAGE_EQUITY"
    },

    {
        "id": "pepexator",
        "image": "pepexator__landing_page.png",
        "name": "PEPEXATOR",
        "url": "https://pepexator.pierref.eu",
        "category": "DEPLOYMENTS",
        "badge": "Academic_Maps",
        "year": "2026",
        "description": "Cartographie technique et méthodologique pour étudiants EPITA. Feuilles de route complètes d'architecture de survie logicielle.",
        "tags": ["Python", "SQLite", "EPITA", "Mindmap", "Architecture", "Documentation"],
        "theme_color": "cyan-500",
        "custom_template": "partials/cards/pepexator.html",
        "cta": "EXPLORE_MAP"
    },

    {
        "id": "leboncoin_bot",
        "image": "lbcstudio_landing_page.png",
        "name": "LBC Studio",
        "url": "https://lbcstudio.pierref.eu",
        "category": "DEPLOYMENTS",
        "badge": "Neural_System_Active",
        "year": "2026",
        "description": "L'automatisation ultime pour Leboncoin & Vinted. Studio IA de retouche photo, SEO sémantique et Auto-Posting orchestré via Discord.",
        "tags": ["Python", "Discord API", "Vision IA", "Automation", "Leboncoin", "Vinted", "SaaS"],
        "theme_color": "rose-500",
        "custom_template": "partials/cards/lbc_studio.html",
        "cta": "EXPLORE_STUDIO"
    },

    {
        "id": "work_optimizer",
        "image": "auriga.png",
        "name": "Work Optimizer",
        "url": "https://github.com/evaspace",
        "category": "DEPLOYMENTS",
        "badge": "Tooling",
        "year": "v2.4",
        "description": "Suite de scripts d'automatisation d'environnement de travail. Tri de fichiers, affichage de base de données et configuration Unix.",
        "tags": ["Bash", "Automation", "Linux", "Scripting", "DevOps", "Workspace"],
        "theme_color": "indigo-500",
        "custom_template": "partials/cards/work_optimizer.html",
        "cta": "VIEW_CODE"
    },

    {
        "id": "larchitect_lab",
        "image": "larchitect_landing_page.png",
        "name": "Larchitect Lab",
        "url": "https://larchitect.pierref.eu",
        "category": "LIVE_LABS",
        "badge": "System_Active",
        "year": "V2.1",
        "description": "Générateur autonome d'architectures et serveurs Discord par invite de commande IA en langage naturel. Stripe intégration et templates.",
        "tags": ["Python", "Discord", "IA Builder", "Architecture", "Docker", "SaaS", "Stripe"],
        "theme_color": "alpine-ice",
        "custom_template": "partials/cards/larchitect_lab.html",
        "cta": "ACCESS_PORTAL"
    },
    {
        "id": "focusator",
        "image": "focusator_landing_page.png",
        "name": "Focusator",
        "url": "https://focusator.pierref.eu",
        "category": "DEPLOYMENTS",
        "badge": "Cognitive_Remediation",
        "year": "2026",
        "description": "Moteur d'évaluation et de remédiation cognitive. Remplace les conseils génériques de productivité par des blocs durs (Hard blocks).",
        "tags": ["Python", "TF-IDF", "Productivité", "Analytics", "Clustering"],
        "theme_color": "brand-blue",
        "cta": "STAY_FOCUSED"
    },
    {
        "id": "mathsdoomscroll",
        "image": "mathsdoomscroll_landing_page.png",
        "name": "Maths Doomscrolling",
        "url": "https://mathsdoomscrolling.pierref.eu",
        "category": "DEPLOYMENTS",
        "badge": "EdTech_Gamification",
        "year": "2026",
        "description": "Plateforme addictive de doomscrolling mathématique. Théorèmes, QCM, Vrai/Faux, mascotte interactive et feedback pixel art.",
        "tags": ["Python", "Flask", "KaTeX", "Pixel Art", "Maths", "EdTech", "Gamification", "Spaced Repetition", "QCM", "LaTeX", "Flashcards"],
        "theme_color": "brand-blue",
        "cta": "DOOMSCROLL_NOW"
    }
]

BUSINESS_PERFORMANCE = [
    {
        "id": "micro_entrepreneur",
        "name": "Micro-entrepreneur (Services)",
        "url": "https://www.pappers.fr/entreprise/pierrefeu-morgan-942369539",
        "category": "PERFORMANCE",
        "subtitle": "Lyon | 2024 - Present",
        "theme_color": "brand-gold",
        "border_side": "border-l-8",
        "icon_svg": "palais-silhouette",
        "points": [
            "Legal Structure: Registered B2B entity managed with rigorous engineering administrative foundations.",
            "Operations: 100% autonomous billing, contract negotiation, and cash flow management.",
            "Efficiency: ROI-driven mindset applied to real-world industrial and commercial constraints."
        ]
    },
    {
        "id": "measurable_performance",
        "name": "Measurable Performance",
        "url": "https://www.google.com/search?q=liste+des+records+PIERREFEU+Morgan+&sca_esv=5dca0e6f8aa8611e",
        "category": "PERFORMANCE",
        "subtitle": '\"Athletic practice structures professional discipline.\"',
        "theme_color": "white",
        "border_side": "border-l-8",
        "icon_svg": "mountain-whaou",
        "points": [
            "Alpinism: 3 summits > 3000m. Target: Mont Blanc 2026.",
            "Athletics (Sprint): 22.77s on 200m. Focus on continuous detail optimization.",
            "Endurance: Solo expedition in Georgia. Proving mental resilience and logistical autonomy."
        ],
        "hover_color": "brand-orange"
    }
]
