from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


JOB_ROLES = {
    "Data Analyst": [
        "python", "sql", "excel",
        "pandas", "power bi", "statistics",
        "data analysis"
    ],

    "Machine Learning Engineer": [
        "python", "machine learning",
        "scikit-learn", "pandas",
        "docker", "fastapi"
    ],

    "AI Engineer": [
        "python", "deep learning",
        "tensorflow", "pytorch",
        "transformers", "rest api"
    ],

    "NLP Engineer": [
        "python", "nlp",
        "hugging face", "transformers",
        "machine learning"
    ],

    "Computer Vision Engineer": [
        "python", "opencv",
        "cnn", "deep learning",
        "tensorflow", "pytorch"
    ]
}


def calculate_matches(resume_text):
    roles = list(JOB_ROLES.keys())

    documents = [resume_text] + [
        " ".join(JOB_ROLES[role])
        for role in roles
    ]

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(documents)

    scores = cosine_similarity(
        vectors[0:1],
        vectors[1:]
    )[0]

    results = {}

    for role, score in zip(roles, scores):
        results[role] = round(float(score) * 100, 2)

    return dict(
        sorted(
            results.items(),
            key=lambda item: item[1],
            reverse=True
        )
    )


def get_missing_skills(resume_skills, role):
    required = JOB_ROLES[role]

    return [
        skill for skill in required
        if skill not in resume_skills
    ]