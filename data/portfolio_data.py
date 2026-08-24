# -----------------------------------------------------------------------------
# portfolio_data.py
# Single source of truth for every piece of content on the site.
# Edit this file to update the portfolio -- no template edits required.
# Anything wrapped in [ADD ...] is a placeholder Dhivya must replace.
# -----------------------------------------------------------------------------

PROFILE = {
    "name": "S. Dhivya",
    "short_name": "Dhivya",
    "monogram": "SD",
    "headline": "AI & Machine Learning Enthusiast | Data Analytics | Python Developer",
    "hero_intro": (
        "I am S. Dhivya, a final-year Artificial Intelligence and Data Science student "
        "passionate about transforming data into practical, user-friendly solutions. "
        "I build machine learning models and integrate them into web applications using "
        "Python, Flask, HTML, CSS, and JavaScript. My work spans healthcare prediction, "
        "agricultural intelligence, career readiness, and data-driven decision support."
    ),
    "about_summary": (
        "I am an aspiring AI and Machine Learning professional from Pudukkottai, Tamil Nadu. "
        "Through internships, academic work, and independent projects, I have gained hands-on "
        "experience in data preprocessing, exploratory analysis, supervised learning, model "
        "evaluation, and Flask-based deployment. I enjoy learning by building complete "
        "solutions\u2014from understanding a problem and preparing its data to training a model "
        "and presenting its output through an accessible interface. I am currently looking for "
        "an entry-level opportunity where I can strengthen my technical skills, contribute to "
        "real projects, and grow with an experienced team."
    ),
    "email": "dhivyasubash19@gmail.com",
    "phone": "+91 63813 50866",
    "phone_display": "+91 63813 50866",
    "location": "Pudukkottai, Tamil Nadu, India",
    "languages": ["Tamil", "English"],
    "interests": ["Reading books", "Listening to music", "Drawing", "Creating artworks"],
    "availability_badge": "Open to entry-level opportunities and internships",
    "profile_photo": "images/profile/profile.png",
    "resume_path": "documents/resume.pdf",
    "github_url": "https://github.com/dhivyasubash19-glitch",
    "linkedin_url": "https://www.linkedin.com/in/dhivya-subash-7a997b383",
    "value_cards": [
        {
            "title": "Practical ML",
            "text": "Builds and evaluates supervised and unsupervised models end-to-end, from raw data to a working interface.",
            "icon": "cpu",
        },
        {
            "title": "Problem Solving",
            "text": "Breaks down real-world problems -- crop health, patient risk, pricing -- into data questions that models can answer.",
            "icon": "puzzle",
        },
        {
            "title": "Continuous Learning",
            "text": "Steadily building depth in deployment, model improvement, and placement-ready coding practice.",
            "icon": "sprout",
        },
    ],
    "what_i_bring": [
        "Solid Python foundations for data work and application logic",
        "Working knowledge of the ML workflow: preprocessing, training, evaluation, iteration",
        "Comfort with exploratory data analysis and visual storytelling with data",
        "Ability to wrap a trained model in a usable Flask web interface",
    ],
}

NAV_LINKS = [
    {"id": "home", "label": "Home"},
    {"id": "about", "label": "About"},
    {"id": "skills", "label": "Skills"},
    {"id": "experience", "label": "Experience"},
    {"id": "projects", "label": "Projects"},
    {"id": "education", "label": "Education"},
    {"id": "certifications", "label": "Certifications"},
    {"id": "contact", "label": "Contact"},
]

SKILLS = [
    {
        "group": "Programming",
        "items": ["Python", "SQL (Basic)", "JavaScript"],
    },
    {
        "group": "Data & Analysis",
        "items": ["Pandas", "NumPy", "Matplotlib", "Seaborn", "Data Preprocessing", "Exploratory Data Analysis"],
    },
    {
        "group": "Machine Learning",
        "items": ["scikit-learn", "Supervised Learning", "Regression", "Classification", "Clustering", "Feature Engineering", "Model Evaluation"],
    },
    {
        "group": "AI / Deep Learning Exposure",
        "items": ["TensorFlow / Keras", "EfficientNet-based Image Classification"],
    },
    {
        "group": "Web Development",
        "items": ["HTML5", "CSS3", "JavaScript", "Bootstrap", "Flask", "REST API Fundamentals"],
    },
    {
        "group": "Databases & Tools",
        "items": ["SQLite", "Git", "GitHub", "VS Code", "Jupyter Notebook"],
    },
    {
        "group": "Soft Skills",
        "items": ["Communication", "Teamwork", "Problem Solving", "Leadership", "Time Management", "Quick Learning"],
    },
]

EXPERIENCE = [
    {
        "role": "AI & Machine Learning Intern",
        "org": "DigiDARA Technologies Pvt. Ltd.",
        "duration": "4 Weeks \u00b7 July 2026",
        "points": [
            "Completed hands-on training in Python, Python libraries, artificial intelligence, and machine learning concepts.",
            "Worked on a practical AI and Machine Learning project.",
        ],
    },
    {
        "role": "Machine Learning Intern",
        "org": "MECK TECK Research Foundation Pvt. Ltd.",
        "duration": "1 Month",
        "points": [
            "Gained practical experience in data preprocessing, data analysis, ML fundamentals, and model evaluation.",
        ],
    },
]

# Each project can carry a status: "Prototype", "Completed", "In Development"
PROJECTS = [
    {
        "slug": "agro-guardian",
        "title": "Agro-Guardian",
        "subtitle": "AI-Powered Crop Intelligence & Optimization Platform",
        "category": "Machine Learning",
        "status": "Prototype / Concept",
        "context": "Built by Team TECHFORT for the \u2018Nimirndhu Nil\u2019 Hackathon Ideation Camp under EDII-TN / TNYIEDP.",
        "problem": "Farmers need clearer support for crop health, yield planning, weather risks, and timely recommendations.",
        "solution": "A bilingual Tamil-English crop intelligence platform covering yield prediction, disease detection, weather intelligence, smart recommendations, farmer workflow, and market insights.",
        "role": "Team member, Team TECHFORT \u2014 contributed to the AI/ML modules.",
        "tech": ["Python", "Flask", "XGBoost", "Random Forest", "EfficientNet-B4", "SQLite"],
        "result": None,
        "outcome_line": "A hackathon prototype exploring how ML can support farmer decision-making.",
        "github_url": "",
        "demo_url": "",
        "cover_icon": "leaf",
    },
    {
        "slug": "fruit-identification-system",
        "title": "Fruit Identification System",
        "subtitle": "Clustering & Classification on Fruit Feature Data",
        "category": "Machine Learning",
        "status": "Completed",
        "context": None,
        "problem": "Identify and group fruit types from measured feature data without and then with labels available.",
        "solution": "Started as an unsupervised workflow (feature scaling, elbow method, silhouette score, K-Means, centroid analysis), then extended into supervised classification with Random Forest.",
        "role": "Solo project \u2014 data preparation, modelling, and evaluation.",
        "tech": ["Python", "Pandas", "scikit-learn", "Matplotlib", "Seaborn", "Flask", "HTML/CSS/JavaScript"],
        "result": "Random Forest test accuracy of 99.33%",
        "outcome_line": "Random Forest classifier reached 99.33% test accuracy; evidence in the case study.",
        "github_url": "",
        "demo_url": "",
        "cover_icon": "grid",
    },
    {
        "slug": "heart-disease-prediction",
        "title": "Heart Disease Prediction",
        "subtitle": "Educational Decision-Support Prototype",
        "category": "Machine Learning",
        "status": "Educational Prototype \u2014 Not a Medical Diagnosis Tool",
        "context": None,
        "problem": "Estimate the possibility of heart disease from patient health inputs, for learning purposes.",
        "solution": "Trained a supervised learning model and integrated it into a Flask web application for testing predictions.",
        "role": "Solo project \u2014 preprocessing, modelling, and Flask integration.",
        "tech": ["Python", "scikit-learn", "Flask", "HTML/CSS/JavaScript"],
        "result": None,
        "outcome_line": "A working Flask demo that estimates risk from health inputs \u2014 for education, not diagnosis.",
        "github_url": "",
        "demo_url": "",
        "cover_icon": "heart-pulse",
    },
    {
        "slug": "house-price-prediction",
        "title": "House Price Prediction",
        "subtitle": "Regression on Property Features",
        "category": "Data Analytics",
        "status": "Completed",
        "context": None,
        "problem": "Estimate house prices from property features to support pricing decisions.",
        "solution": "Built a regression model and wrapped it in a web interface built with HTML, CSS, JavaScript, and Flask.",
        "role": "Solo project \u2014 modelling and web interface.",
        "tech": ["Python", "scikit-learn", "Flask", "HTML/CSS/JavaScript"],
        "result": None,
        "outcome_line": "A Flask interface that returns a price estimate from user-entered property details.",
        "github_url": "",
        "demo_url": "",
        "cover_icon": "home",
    },
]

PROJECT_FILTERS = ["All", "Machine Learning", "Deep Learning", "Data Analytics", "Full Stack"]

# Reusable case-study skeleton -- filled per project where evidence exists.
CASE_STUDY_FIELDS = [
    "problem", "role", "solution", "tech", "result",
]

EDUCATION = [
    {
        "degree": "B.Tech \u2014 Artificial Intelligence and Data Science",
        "institution": "Sudharsan Engineering College",
        "detail": "CGPA 8.28 (through 6th semester)",
        "year": "Expected 2027",
        "highlight": True,
    },
    {
        "degree": "Higher Secondary (12th)",
        "institution": "Sacred Heart Girls Higher Secondary School",
        "detail": "78%",
        "year": "2023",
        "highlight": False,
    },
    {
        "degree": "Secondary School (10th)",
        "institution": "Sacred Heart Girls Higher Secondary School",
        "detail": "Pass",
        "year": "2021",
        "highlight": False,
    },
]

CERTIFICATIONS = [
    {
        "title": "Data Analytics Masterclass",
        "issuer": "NOVI TECH Pvt. Ltd.",
        "date": "",
        "credential_url": "",  # [ADD CERTIFICATE VERIFICATION URL]
        "image": "",           # [ADD CERTIFICATE IMAGE/PDF]
    },
    {
        "title": "Artificial Intelligence Masterclass",
        "issuer": "NOVI TECH Pvt. Ltd.",
        "date": "",
        "credential_url": "",
        "image": "",
    },
    {
        "title": "\u2018Nimirndhu Nil\u2019 Hackathon \u2014 Ideation Camp",
        "issuer": "Entrepreneurship Development and Innovation Institute, Tamil Nadu (EDII-TN), under TNYIEDP",
        "date": "June 2026",
        "credential_url": "",
        "image": "",
    },
]

CURRENTLY_LEARNING = [
    "Advanced Python",
    "Machine learning model improvement",
    "Model deployment",
    "Placement coding preparation",
]

SITE_META = {
    "title": "S. Dhivya | AI & Data Science Portfolio",
    "description": "Portfolio of S. Dhivya, a final-year B.Tech AI & Data Science student building practical machine learning and Flask-based web solutions.",
    "canonical_url": "",  # [ADD CANONICAL DOMAIN URL ONCE DEPLOYED]
}
