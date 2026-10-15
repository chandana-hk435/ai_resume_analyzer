
SKILLS=["python","java","c++","sql","excel","pandas","numpy","scikit-learn","tensorflow","pytorch","machine learning","deep learning","nlp","opencv","power bi","tableau","aws","docker","fastapi","git","linux"]
def extract_skills(text):
    return list(set([s for s in SKILLS if s in text.lower()]))
