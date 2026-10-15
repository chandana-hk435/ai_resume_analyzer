import os
os.makedirs("data", exist_ok=True)

open("resume_parser.py","w").write("""
import fitz
import docx
def extract_text(file):
    text=""
    if file.name.endswith('.pdf'):
        doc=fitz.open(stream=file.read(), filetype="pdf")
        for page in doc:
            text+=page.get_text()
    else:
        d=docx.Document(file)
        text="\\n".join([p.text for p in d.paragraphs])
    return text
""")

open("text_cleaner.py","w").write("""
import re
def clean_text(text):
    text=text.lower()
    text=text.replace('c++','cplusplus').replace('c#','csharp')
    text=re.sub(r'[^a-z0-9\\s]',' ',text)
    return text.replace('cplusplus','c++').replace('csharp','c#')
""")

open("skill_extractor.py","w").write("""
SKILLS=["python","java","c++","sql","excel","pandas","numpy","scikit-learn","tensorflow","pytorch","machine learning","deep learning","nlp","opencv","power bi","tableau","aws","docker","fastapi","git","linux"]
def extract_skills(text):
    return list(set([s for s in SKILLS if s in text.lower()]))
""")

open("job_matcher.py","w").write("""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def calculate_match(resume_text, job_dict):
    docs=[resume_text]+list(job_dict.values())
    tfidf=TfidfVectorizer().fit_transform(docs)
    scores={}
    for i, role in enumerate(job_dict.keys()):
        scores[role]=round(cosine_similarity(tfidf[0],tfidf[i+1])[0][0]*100,2)
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)
""")

open("roadmap_generator.py","w").write("""
def generate_roadmap(missing):
    return [f"Week {i}: Learn {s}" for i,s in enumerate(missing[:4],1)]
def identify_gaps(found, required_str):
    req=[s.strip() for s in required_str.lower().split(',')]
    return [r for r in req if r not in [f.lower() for f in found]]
""")

open("data/job_roles.csv","w").write("""Job Role,Required Skills
Data Analyst,"python, sql, excel, pandas, power bi"
ML Engineer,"python, machine learning, scikit-learn, fastapi"
AI Engineer,"python, deep learning, llm, rag"
""")

print("All files created!")