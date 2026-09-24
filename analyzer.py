import re

SKILLS = [
    "python", "java", "javascript", "c++", "sql",
    "machine learning", "deep learning", "tensorflow",
    "pytorch", "aws", "docker", "git", "github",
    "data science", "pandas", "numpy"
]


def extract_skills(text):
    text = text.lower()
    found = []

    for skill in SKILLS:
        if skill in text:
            found.append(skill)

    return found


def analyze_resume(resume, job_description):
    resume_skills = set(extract_skills(resume))
    job_skills = set(extract_skills(job_description))

    matched = resume_skills.intersection(job_skills)
    missing = job_skills - resume_skills

    score = 0

    if job_skills:
        score = (len(matched) / len(job_skills)) * 100

    return score, matched, missing


resume = input("Paste your resume text:\n")
job = input("\nPaste the job description:\n")

score, matched, missing = analyze_resume(resume, job)

print("\n========== RESUME ANALYSIS ==========")
print(f"Match Score: {score:.1f}%")

print("\nMatched Skills:")
for skill in sorted(matched):
    print(f"✓ {skill}")

print("\nMissing Skills:")
for skill in sorted(missing):
    print(f"✗ {skill}")