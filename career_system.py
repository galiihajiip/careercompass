"""
═══════════════════════════════════════════════════════════════════════════════
                   CAREER RECOMMENDATION SYSTEM
          A Production-Grade Application Using OOP & Streamlit
═══════════════════════════════════════════════════════════════════════════════
Author: CareerCompass AI
Version: 1.0.0

Demonstrates:
    ✓ Multilevel Inheritance (User → SkillProfile → CareerEngine)
    ✓ Method Overriding (display_info())
    ✓ Encapsulation (protected attributes, property decorators)
    ✓ Complex Scoring Algorithm (weighted, not simple if-else)
    ✓ Modern Dashboard UI with custom CSS
═══════════════════════════════════════════════════════════════════════════════
"""

import streamlit as st
import re
import time
import json
import pandas as pd
import plotly.graph_objects as go
from typing import List, Dict, Optional

# ═════════════════════════════════════════════════════════════════════════════
# CONSTANTS
# ═════════════════════════════════════════════════════════════════════════════
AVAILABLE_SKILLS = sorted([
    "Python","JavaScript","TypeScript","Java","C#","C++","Go","Rust","Swift",
    "Kotlin","React","Vue","Angular","Node.js","Django","Flask","Spring Boot",
    ".NET","TensorFlow","PyTorch","Scikit-learn","Keras","Docker","Kubernetes",
    "Jenkins","Git","SQL","MongoDB","Redis","AWS","Azure","GCP","Figma","Unity",
    "Machine Learning","Deep Learning","Data Analysis","Cloud Computing",
    "Cybersecurity","Mobile Development","Game Development","UI/UX Design",
    "Network Security","Ethical Hacking","Solidity","Web3","Data Visualization",
    "Statistics","Microservices","CI/CD"
])

INTEREST_FIELDS = [
    "Artificial Intelligence & Machine Learning",
    "Data Science & Analytics",
    "Web Development",
    "Mobile Development",
    "Cloud & DevOps",
    "Cybersecurity",
    "Game Development",
    "UI/UX Design",
    "Blockchain & Web3",
    "Software Architecture"
]

SKILL_WEIGHTS = {
    "Python":1.2,"JavaScript":1.1,"TypeScript":1.0,"Java":1.1,"C#":1.0,
    "C++":1.0,"Go":0.9,"Rust":0.9,"Swift":1.0,"Kotlin":1.0,"React":1.1,
    "Vue":0.9,"Angular":0.9,"Node.js":1.0,"Django":0.9,"Flask":0.8,
    "Spring Boot":0.9,".NET":0.9,"TensorFlow":1.1,"PyTorch":1.1,
    "Scikit-learn":1.0,"Keras":0.9,"Docker":1.0,"Kubernetes":1.0,
    "Jenkins":0.8,"Git":0.7,"SQL":1.0,"MongoDB":0.9,"Redis":0.8,
    "AWS":1.1,"Azure":1.0,"GCP":1.0,"Figma":0.9,"Unity":1.0,
    "Machine Learning":1.3,"Deep Learning":1.2,"Data Analysis":1.0,
    "Cloud Computing":1.1,"Cybersecurity":1.1,"Mobile Development":1.0,
    "Game Development":1.0,"UI/UX Design":1.0,"Network Security":1.0,
    "Ethical Hacking":1.0,"Solidity":0.9,"Web3":0.9,
    "Data Visualization":0.9,"Statistics":1.0,"Microservices":1.0,"CI/CD":0.9
}

LEVEL_MATRIX = {
    ("Beginner","Beginner"):1.0,("Beginner","Intermediate"):0.7,
    ("Beginner","Advanced"):0.5,("Intermediate","Beginner"):1.1,
    ("Intermediate","Intermediate"):1.0,("Intermediate","Advanced"):0.8,
    ("Advanced","Beginner"):0.9,("Advanced","Intermediate"):1.1,
    ("Advanced","Advanced"):1.2,
}


# ═════════════════════════════════════════════════════════════════════════════
# CLASS 1: USER (BASE CLASS) — Encapsulation & Validation
# ═════════════════════════════════════════════════════════════════════════════
class User:
    """
    Base class for a user in the career recommendation system.
    Demonstrates ENCAPSULATION via protected attributes and @property decorators.

    Attributes:
        _name (str): Protected – user's full name
        _email (str): Protected – user's email
        _age (int|None): Protected – optional age

    Usage:
        >>> u = User("Alice","alice@mail.com",25)
        >>> u.display_info()
    """

    def __init__(self, name: str, email: str, age: Optional[int] = None):
        self.name = name
        self.email = email
        self._age = age

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, v: str):
        if not isinstance(v, str) or len(v.strip()) < 2:
            raise ValueError("Name must be at least 2 characters.")
        if len(v.strip()) > 50:
            raise ValueError("Name must be at most 50 characters.")
        if not re.match(r"^[A-Za-z\s\-']+$", v.strip()):
            raise ValueError("Name: letters, spaces, hyphens, apostrophes only.")
        self._name = v.strip()

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, v: str):
        if not self.validate_email(v):
            raise ValueError("Please enter a valid email address.")
        self._email = v.strip()

    @property
    def age(self) -> Optional[int]:
        return self._age

    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate email format with regex."""
        return bool(re.match(r'^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$', email.strip()))

    def display_info(self) -> dict:
        """Return basic user information. Designed to be OVERRIDDEN."""
        info = {"name": self._name, "email": self._email}
        if self._age:
            info["age"] = self._age
        return info

    def __str__(self):
        return f"User('{self._name}', '{self._email}')"


# ═════════════════════════════════════════════════════════════════════════════
# CLASS 2: SKILLPROFILE (INTERMEDIATE) — Inheritance + Override via super()
# ═════════════════════════════════════════════════════════════════════════════
class SkillProfile(User):
    """
    Extends User with skill information. Inherits from User.
    INHERITANCE CHAIN: User → SkillProfile

    New Attributes:
        _skills, _skill_level, _interest_field
    Overridden: display_info() calls super().display_info() then extends

    Usage:
        >>> sp = SkillProfile("Bob","bob@x.com",["Python","SQL"],"Intermediate","Data Science & Analytics")
    """

    def __init__(self, name, email, skills, skill_level, interest_field, age=None):
        super().__init__(name, email, age)
        self._skills = list(skills)
        self._skill_level = skill_level
        self._interest_field = interest_field

    def add_skill(self, skill: str) -> bool:
        if skill in AVAILABLE_SKILLS and skill not in self._skills:
            self._skills.append(skill); return True
        return False

    def remove_skill(self, skill: str) -> bool:
        if skill in self._skills:
            self._skills.remove(skill); return True
        return False

    def get_skill_count(self) -> int:
        return len(self._skills)

    def calculate_skill_score(self) -> float:
        """Weighted skill score = sum(weights) * level_multiplier."""
        if not self._skills: return 0.0
        raw = sum(SKILL_WEIGHTS.get(s, 0.5) for s in self._skills)
        mult = {"Beginner":0.7,"Intermediate":1.0,"Advanced":1.2}.get(self._skill_level, 1.0)
        return round(raw * mult, 2)

    def display_info(self) -> dict:
        """Override: calls super().display_info() then adds skill fields."""
        info = super().display_info()
        info.update({
            "skills": self._skills, "skill_count": self.get_skill_count(),
            "skill_level": self._skill_level, "interest_field": self._interest_field,
            "skill_score": self.calculate_skill_score()
        })
        return info

    def __str__(self):
        return f"SkillProfile('{self._name}', skills={len(self._skills)})"


# ═════════════════════════════════════════════════════════════════════════════
# CLASS 3: CAREERENGINE (DERIVED) — Multilevel Inheritance + Complex Scoring
# ═════════════════════════════════════════════════════════════════════════════
class CareerEngine(SkillProfile):
    """
    Career recommendation engine — multilevel inheritance.
    INHERITANCE CHAIN: User → SkillProfile → CareerEngine

    Key Methods:
        generate_recommendations(): top 3-5 careers via weighted scoring
        calculate_career_match_score(): complex multi-factor algorithm

    Usage:
        >>> e = CareerEngine("Alice","a@b.com",["Python","ML"],"Advanced","AI & ML","Remote")
        >>> recs = e.generate_recommendations()
    """

    def __init__(self, name, email, skills, skill_level, interest_field, work_preference, age=None):
        super().__init__(name, email, skills, skill_level, interest_field, age)
        self._work_preference = work_preference
        self._career_database = self._load_career_database()
        self._recommendations = []

    @staticmethod
    def _load_career_database() -> dict:
        return {
            "AI/ML Engineer": {
                "required_skills":["Python","Machine Learning","Deep Learning","TensorFlow"],
                "preferred_skills":["PyTorch","Keras","Statistics","Docker"],
                "interest_field":"Artificial Intelligence & Machine Learning",
                "min_skill_level":"Intermediate","base_popularity":92,
                "salary_range":(100000,160000),"growth_outlook":"High",
                "description":"Design and deploy machine-learning models and intelligent systems.",
                "work_pref_compat":{"Remote":1.0,"Hybrid":1.0,"Office":0.85}
            },
            "Data Scientist": {
                "required_skills":["Python","SQL","Statistics","Data Visualization"],
                "preferred_skills":["Machine Learning","Scikit-learn","Data Analysis"],
                "interest_field":"Data Science & Analytics",
                "min_skill_level":"Intermediate","base_popularity":90,
                "salary_range":(85000,140000),"growth_outlook":"High",
                "description":"Extract insights from complex datasets to drive decisions.",
                "work_pref_compat":{"Remote":1.0,"Hybrid":1.0,"Office":0.9}
            },
            "Full Stack Web Developer": {
                "required_skills":["JavaScript","React","Node.js","SQL"],
                "preferred_skills":["TypeScript","MongoDB","Docker","Git"],
                "interest_field":"Web Development",
                "min_skill_level":"Intermediate","base_popularity":88,
                "salary_range":(75000,135000),"growth_outlook":"High",
                "description":"Build complete web applications from front-end to back-end.",
                "work_pref_compat":{"Remote":1.0,"Hybrid":1.0,"Office":0.9}
            },
            "Frontend Developer": {
                "required_skills":["JavaScript","React","TypeScript","UI/UX Design"],
                "preferred_skills":["Vue","Angular","Figma","Git"],
                "interest_field":"Web Development",
                "min_skill_level":"Beginner","base_popularity":85,
                "salary_range":(65000,120000),"growth_outlook":"High",
                "description":"Create engaging, responsive user interfaces for web apps.",
                "work_pref_compat":{"Remote":1.0,"Hybrid":1.0,"Office":0.9}
            },
            "Backend Developer": {
                "required_skills":["Python","SQL","Microservices","Docker"],
                "preferred_skills":["Java","Redis","AWS","CI/CD"],
                "interest_field":"Web Development",
                "min_skill_level":"Intermediate","base_popularity":86,
                "salary_range":(80000,140000),"growth_outlook":"High",
                "description":"Design server-side logic, APIs, and database architectures.",
                "work_pref_compat":{"Remote":1.0,"Hybrid":1.0,"Office":0.85}
            },
            "Mobile Developer": {
                "required_skills":["Swift","Kotlin","Mobile Development","UI/UX Design"],
                "preferred_skills":["React","TypeScript","Git","CI/CD"],
                "interest_field":"Mobile Development",
                "min_skill_level":"Intermediate","base_popularity":82,
                "salary_range":(78000,138000),"growth_outlook":"Medium",
                "description":"Build native and cross-platform mobile applications.",
                "work_pref_compat":{"Remote":0.95,"Hybrid":1.0,"Office":0.9}
            },
            "DevOps Engineer": {
                "required_skills":["Docker","Kubernetes","CI/CD","Cloud Computing"],
                "preferred_skills":["AWS","Azure","Jenkins","Python"],
                "interest_field":"Cloud & DevOps",
                "min_skill_level":"Intermediate","base_popularity":87,
                "salary_range":(90000,150000),"growth_outlook":"High",
                "description":"Automate infrastructure, deployments, and monitoring at scale.",
                "work_pref_compat":{"Remote":1.0,"Hybrid":1.0,"Office":0.8}
            },
            "Cloud Architect": {
                "required_skills":["AWS","Cloud Computing","Microservices","Docker"],
                "preferred_skills":["Azure","GCP","Kubernetes","Python"],
                "interest_field":"Cloud & DevOps",
                "min_skill_level":"Advanced","base_popularity":89,
                "salary_range":(120000,180000),"growth_outlook":"High",
                "description":"Architect scalable, resilient cloud infrastructure solutions.",
                "work_pref_compat":{"Remote":1.0,"Hybrid":1.0,"Office":0.8}
            },
            "Cybersecurity Analyst": {
                "required_skills":["Cybersecurity","Network Security","Ethical Hacking","Python"],
                "preferred_skills":["Cloud Computing","Docker","SQL","Git"],
                "interest_field":"Cybersecurity",
                "min_skill_level":"Intermediate","base_popularity":88,
                "salary_range":(80000,140000),"growth_outlook":"High",
                "description":"Protect organisations from cyber threats and vulnerabilities.",
                "work_pref_compat":{"Remote":0.9,"Hybrid":1.0,"Office":1.0}
            },
            "UI/UX Designer": {
                "required_skills":["Figma","UI/UX Design","Data Visualization","JavaScript"],
                "preferred_skills":["React","TypeScript","Statistics","Git"],
                "interest_field":"UI/UX Design",
                "min_skill_level":"Beginner","base_popularity":80,
                "salary_range":(60000,115000),"growth_outlook":"Medium",
                "description":"Craft intuitive, beautiful user experiences and interfaces.",
                "work_pref_compat":{"Remote":1.0,"Hybrid":1.0,"Office":0.9}
            },
            "Game Developer": {
                "required_skills":["Unity","C#","Game Development","UI/UX Design"],
                "preferred_skills":["C++","Python","Git","Data Visualization"],
                "interest_field":"Game Development",
                "min_skill_level":"Intermediate","base_popularity":78,
                "salary_range":(60000,120000),"growth_outlook":"Medium",
                "description":"Create immersive gaming experiences across platforms.",
                "work_pref_compat":{"Remote":0.9,"Hybrid":0.95,"Office":1.0}
            },
            "QA Engineer": {
                "required_skills":["Python","CI/CD","Git","SQL"],
                "preferred_skills":["JavaScript","Docker","Jenkins","Microservices"],
                "interest_field":"Software Architecture",
                "min_skill_level":"Beginner","base_popularity":75,
                "salary_range":(60000,110000),"growth_outlook":"Medium",
                "description":"Ensure software quality through testing and automation.",
                "work_pref_compat":{"Remote":1.0,"Hybrid":1.0,"Office":0.9}
            },
            "Blockchain Developer": {
                "required_skills":["Solidity","Web3","JavaScript","Cybersecurity"],
                "preferred_skills":["Python","React","Docker","Git"],
                "interest_field":"Blockchain & Web3",
                "min_skill_level":"Intermediate","base_popularity":76,
                "salary_range":(90000,160000),"growth_outlook":"Medium",
                "description":"Build decentralised applications and smart contracts.",
                "work_pref_compat":{"Remote":1.0,"Hybrid":1.0,"Office":0.8}
            },
            "Data Engineer": {
                "required_skills":["SQL","Python","Cloud Computing","Docker"],
                "preferred_skills":["AWS","Data Analysis","Microservices","CI/CD"],
                "interest_field":"Data Science & Analytics",
                "min_skill_level":"Intermediate","base_popularity":86,
                "salary_range":(90000,150000),"growth_outlook":"High",
                "description":"Build robust data pipelines and warehousing solutions.",
                "work_pref_compat":{"Remote":1.0,"Hybrid":1.0,"Office":0.85}
            },
            "Software Architect": {
                "required_skills":["Microservices","Docker","Python","Cloud Computing"],
                "preferred_skills":["Kubernetes","AWS","CI/CD","Java"],
                "interest_field":"Software Architecture",
                "min_skill_level":"Advanced","base_popularity":91,
                "salary_range":(130000,200000),"growth_outlook":"High",
                "description":"Design high-level software structures and technical strategy.",
                "work_pref_compat":{"Remote":0.95,"Hybrid":1.0,"Office":1.0}
            },
        }

    # ── Complex scoring helpers ─────────────────────────────────────────────
    def _required_skills_match(self, career: dict) -> float:
        req = career["required_skills"]
        if not req: return 0.0
        return (sum(1 for s in req if s in self._skills) / len(req)) * 40

    def _preferred_skills_match(self, career: dict) -> float:
        pref = career["preferred_skills"]
        if not pref: return 0.0
        matched = sum(1 for s in pref if s in self._skills)
        return (matched / len(pref)) * 25

    def _interest_bonus(self, career: dict) -> float:
        if self._interest_field == career["interest_field"]:
            return 15.0
        user_w = set(self._interest_field.lower().split())
        career_w = set(career["interest_field"].lower().split())
        return min(15, len(user_w & career_w) * 5.0)

    def _level_modifier(self, career: dict) -> float:
        return LEVEL_MATRIX.get((self._skill_level, career["min_skill_level"]), 1.0)

    def _work_multiplier(self, career: dict) -> float:
        return career["work_pref_compat"].get(self._work_preference, 0.9)

    def calculate_career_match_score(self, career: dict) -> float:
        """
        Complex weighted scoring:
        SCORE = (required + preferred + interest) * level_mod * work_mult * (popularity/100)
        """
        raw = (self._required_skills_match(career)
               + self._preferred_skills_match(career)
               + self._interest_bonus(career))
        raw *= self._level_modifier(career) * self._work_multiplier(career)
        return round(min(100, raw * (career["base_popularity"] / 100)), 2)

    def _build_explanation(self, career: dict, score: float) -> str:
        matched = [s for s in career["required_skills"] if s in self._skills]
        missing = [s for s in career["required_skills"] if s not in self._skills]
        parts = []
        if matched:
            parts.append(f"Your skills in {', '.join(matched)} align well with this role.")
        if self._interest_field == career["interest_field"]:
            parts.append(f"Your interest in {self._interest_field} is a direct match.")
        if career["work_pref_compat"].get(self._work_preference, 0) >= 1.0:
            parts.append(f"{self._work_preference} work is fully supported.")
        if missing:
            parts.append(f"Consider developing: {', '.join(missing)}.")
        return " ".join(parts) if parts else "A solid career option based on your profile."

    def generate_recommendations(self) -> list:
        """Generate top 3-5 career recommendations sorted by score (desc)."""
        scored = []
        for name, data in self._career_database.items():
            score = self.calculate_career_match_score(data)
            scored.append({
                "name": name, "score": score,
                "salary_range": data["salary_range"],
                "growth_outlook": data["growth_outlook"],
                "description": data["description"],
                "matched_skills": [s for s in data["required_skills"] if s in self._skills],
                "missing_skills": [s for s in data["required_skills"] if s not in self._skills],
                "pref_matched": [s for s in data["preferred_skills"] if s in self._skills],
                "pref_missing": [s for s in data["preferred_skills"] if s not in self._skills],
                "interest_field": data["interest_field"],
                "min_level": data["min_skill_level"],
                "work_compat": data["work_pref_compat"].get(self._work_preference, 0.9),
                "explanation": self._build_explanation(data, score)
            })
        scored.sort(key=lambda x: x["score"], reverse=True)
        for i, r in enumerate(scored):
            r["score"] = round(r["score"] - i * 0.01, 2)
        self._recommendations = scored[:5]
        return self._recommendations

    def display_info(self) -> dict:
        """Override: calls super().display_info() then adds career insights."""
        info = super().display_info()
        info["work_preference"] = self._work_preference
        info["recommendations_count"] = len(self._recommendations)
        if self._recommendations:
            info["top_career"] = self._recommendations[0]["name"]
            info["top_score"] = self._recommendations[0]["score"]
        return info

    def export_report(self) -> str:
        return json.dumps({"profile": self.display_info(), "recommendations": self._recommendations}, indent=2, default=str)

    def __str__(self):
        return f"CareerEngine('{self._name}', skills={len(self._skills)}, pref='{self._work_preference}')"


# ═════════════════════════════════════════════════════════════════════════════
# CUSTOM CSS
# ═════════════════════════════════════════════════════════════════════════════
def inject_css():
    st.markdown("""<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    html, body, [class*="css"] {font-family:'Inter',sans-serif}
    .stApp, .main {color:#334155}
    .main{
        background: linear-gradient(180deg,#f5f7fa 0%,#eef2f5 100%);
    }
    [data-testid="stSidebar"]{
        background:#f3f6f8;
        border-right:1px solid #d8e0e7;
    }
    [data-testid="stSidebar"] * {
        color:#334155 !important;
    }
    [data-testid="stSidebar"] .stTextInput input,
    [data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] > div,
    [data-testid="stSidebar"] .stMultiSelect div[data-baseweb="select"] > div {
        background:#ffffff !important;
        border:1px solid #d0d9e2 !important;
        color:#334155 !important;
    }
    .header-title{font-size:2.2rem;font-weight:800;text-align:center;padding:1rem 0 .25rem;color:#1f2937;letter-spacing:-0.02em}
    .header-sub{text-align:center;color:#526173;font-size:1rem;margin-bottom:1.4rem}
    .card{background:#ffffff;border-radius:16px;padding:1.5rem;margin:1rem 0;border:1px solid #dbe3ea;box-shadow:0 6px 18px rgba(15,23,42,.05);transition:border-color .2s ease, box-shadow .2s ease}
    .card:hover{border-color:#c6d2de;box-shadow:0 8px 20px rgba(15,23,42,.07)}
    .top-card{background:linear-gradient(180deg,#ffffff 0%,#f8fafb 100%);border:1px solid #d6dde5;border-left:4px solid #64748b;border-radius:18px;padding:2rem;overflow:hidden;box-shadow:0 8px 22px rgba(15,23,42,.07)}
    .badge{display:inline-block;padding:.35rem .85rem;border-radius:999px;font-weight:700;font-size:.82rem;color:#fff}
    .badge-high{background:#3f6f57}.badge-med{background:#8f6b32}.badge-low{background:#8e4f4f}
    .skill-tag{display:inline-block;background:#edf2f6;padding:.2rem .65rem;border-radius:999px;margin:.15rem;font-size:.8rem;border:1px solid #d5dee7;color:#334155}
    .skill-tag.matched{background:#e8eff6;border-color:#c2d1e0;color:#2f4d68}
    .skill-tag.missing{background:#f6ecec;border-color:#e3cbcb;color:#7a4a4a}
    .metric-box{background:#ffffff;border-radius:14px;padding:1rem;text-align:center;border:1px solid #dbe3ea;box-shadow:0 4px 12px rgba(15,23,42,.05)}
    .metric-val{font-size:1.8rem;font-weight:800;color:#1f2937}
    .metric-lbl{font-size:.78rem;color:#64748b;text-transform:uppercase;letter-spacing:.08em}
    .section-hdr{display:flex;align-items:center;gap:.5rem;font-size:1.16rem;font-weight:700;color:#273444;margin:1.5rem 0 1rem;padding-bottom:.5rem;border-bottom:1px solid #d2dbe3}
    .stExpander{border:1px solid #d8e1e8!important;border-radius:12px!important;background:#ffffff!important}
    .footer-credit{margin-top:2rem;padding:1rem 1.25rem;border-top:1px solid #d8e1e8;color:#5b6876;font-size:.92rem;text-align:center;background:#f8fafb;border-radius:14px}
    </style>""", unsafe_allow_html=True)


# ═════════════════════════════════════════════════════════════════════════════
# UI HELPERS
# ═════════════════════════════════════════════════════════════════════════════
def score_badge(s):
    if s >= 75:
        c = "badge-high"
    elif s >= 50:
        c = "badge-med"
    else:
        c = "badge-low"
    return f'<span class="badge {c}">{s}%</span>'

def stags(skills, matched, cls=""):
    return " ".join(f'<span class="skill-tag {"matched" if s in matched else cls}">{s}</span>' for s in skills)

def render_profile(info):
    st.markdown('<div class="section-hdr">Profile Summary</div>', unsafe_allow_html=True)
    cols = st.columns(4)
    items = [
        ("SKILLS", info["skill_count"]),
        ("LEVEL", info["skill_level"]),
        ("SCORE", info.get("skill_score", "-")),
        ("PREFERENCE", info.get("work_preference", "-")),
    ]
    for col, (label, value) in zip(cols, items):
        col.markdown(
            f'''<div class="metric-box">
            <div class="metric-val">{value}</div>
            <div class="metric-lbl">{label}</div>
            </div>''',
            unsafe_allow_html=True,
        )

def render_top(rec):
    sal = rec["salary_range"]
    st.markdown('<div class="section-hdr">Top Recommendation</div>', unsafe_allow_html=True)
    st.markdown(
        f'''<div class="top-card">
        <div style="display:flex;justify-content:space-between;align-items:center;gap:1rem;flex-wrap:wrap">
            <h2 style="color:#0f172a;margin:0">{rec["name"]}</h2>
            <span>Match: {score_badge(rec["score"])}</span>
        </div>
        <p style="color:#475569;margin:.4rem 0 1rem">{rec["description"]}</p>
        <div style="display:flex;gap:1rem;flex-wrap:wrap;font-size:.95rem;color:#0f172a">
            <span>Salary: {sal}</span>
            <span>Growth: <b>{rec["growth_outlook"]}</b></span>
            <span>Work fit: {rec["work_compat"]*100:.0f}%</span>
        </div>
        <p style="color:#334155;font-style:italic;margin-top:.8rem">{rec["explanation"]}</p>
        <div style="margin-top:.75rem"><b style="color:#166534">Matching:</b> {stags(rec["matched_skills"], rec["matched_skills"])}</div>
        <div style="margin-top:.5rem"><b style="color:#b91c1c">To Develop:</b> {stags(rec["missing_skills"], [], "missing")}</div>
        </div>''',
        unsafe_allow_html=True,
    )

def render_chart(recs):
    st.markdown('<div class="section-hdr">Score Breakdown</div>', unsafe_allow_html=True)
    names = [r["name"] for r in recs][::-1]
    scores = [r["score"] for r in recs][::-1]
    colors = ["#2563eb" if s >= 70 else "#d97706" if s >= 45 else "#b91c1c" for s in scores]
    fig = go.Figure(go.Bar(
        x=scores,
        y=names,
        orientation='h',
        marker=dict(color=colors, line=dict(color="#e2e8f0", width=1)),
        text=[f"{s}%" for s in scores],
        textposition="outside",
        hovertemplate="<b>%{y}</b><br>Match Score: %{x}%<extra></extra>",
    ))
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#0f172a", family="Inter"),
        xaxis=dict(range=[0, 105], showgrid=False),
        yaxis=dict(showgrid=False),
        margin=dict(l=0, r=40, t=10, b=10),
        height=40 * len(recs) + 60,
    )
    st.plotly_chart(fig, use_container_width=True)

def render_others(recs):
    if len(recs) <= 1:
        return
    st.markdown('<div class="section-hdr">Other Recommendations</div>', unsafe_allow_html=True)
    labels = {1: "Second choice", 2: "Third choice", 3: "Fourth choice", 4: "Fifth choice"}
    for i, rec in enumerate(recs[1:], start=1):
        sal = rec["salary_range"]
        with st.expander(f"{labels.get(i, 'Additional option')} #{i+1}: {rec['name']}  -  {rec['score']}%"):
            c1, c2, c3 = st.columns(3)
            c1.metric("Salary", sal)
            c2.metric("Growth", rec["growth_outlook"])
            c3.metric("Work Fit", f"{rec['work_compat']*100:.0f}%")
            st.markdown(f"**Why this fits:** {rec['explanation']}")
            st.markdown(f"**Your Skills:** {stags(rec['matched_skills'], rec['matched_skills'])}", unsafe_allow_html=True)
            st.markdown(f"**To Develop:** {stags(rec['missing_skills'], [], 'missing')}", unsafe_allow_html=True)


# ═════════════════════════════════════════════════════════════════════════════
# MAIN APPLICATION
# ═════════════════════════════════════════════════════════════════════════════
def main():
    st.set_page_config(page_title="CareerCompass AI", page_icon="C", layout="wide", initial_sidebar_state="expanded")
    inject_css()
    st.markdown('<div class="header-title">CareerCompass AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="header-sub">Discover your ideal career path with a data-driven recommendation engine</div>', unsafe_allow_html=True)

    for k, v in {"recommendations": None, "engine": None, "generated": False}.items():
        if k not in st.session_state: st.session_state[k] = v

    with st.sidebar:
        st.markdown("### Your Profile")
        name = st.text_input("Full Name", placeholder="e.g. Jane Doe")
        email = st.text_input("Email", placeholder="e.g. jane@example.com")
        skills = st.multiselect("Skills (select 3-10)", AVAILABLE_SKILLS)
        skill_level = st.selectbox("Skill Level", ["Beginner","Intermediate","Advanced"], index=1)
        interest = st.selectbox("Interest Field", INTEREST_FIELDS)
        work_pref = st.radio("Work Preference", ["Remote","Hybrid","Office"], horizontal=True)
        st.divider()
        generate = st.button("Analyze Career Match", use_container_width=True, type="primary")
        reset = st.button("Reset", use_container_width=True)

    if reset:
        st.session_state.recommendations = None; st.session_state.generated = False; st.rerun()

    if generate:
        errors = []
        if not name or len(name.strip()) < 2: errors.append("Name must be 2-50 characters, letters only.")
        if not email or not User.validate_email(email): errors.append("Please enter a valid email address.")
        if len(skills) < 3: errors.append("Select at least 3 skills for accurate recommendations.")
        if len(skills) > 10: errors.append("Select at most 10 skills.")
        if errors:
            for e in errors: st.sidebar.error(e)
        else:
            try:
                ph = st.empty()
                for i, s in enumerate(["Analyzing your profile...","Matching with careers...","Calculating scores...","Generating recommendations..."]):
                    ph.progress((i+1)*25, text=s); time.sleep(0.35)
                ph.empty()
                engine = CareerEngine(name, email, skills, skill_level, interest, work_pref)
                recs = engine.generate_recommendations()
                st.session_state.engine = engine
                st.session_state.recommendations = recs
                st.session_state.generated = True
                st.rerun()
            except ValueError as ve:
                st.sidebar.error(f"{ve}")

    if st.session_state.generated and st.session_state.recommendations:
        engine = st.session_state.engine
        recs = st.session_state.recommendations
        render_profile(engine.display_info())
        render_top(recs[0])
        render_chart(recs)
        render_others(recs)
        st.divider()
        c1, c2 = st.columns(2)
        c1.download_button("Export JSON", engine.export_report(), "career_report.json", "application/json", use_container_width=True)
        c2.download_button("Export Text", json.dumps([{"career":r["name"],"score":r["score"]} for r in recs], indent=2), "career_summary.txt", "text/plain", use_container_width=True)
    elif not st.session_state.generated:
        st.markdown('<div class="card" style="text-align:center;padding:2.5rem"><h2 style="color:#0f172a">Welcome to CareerCompass</h2><p style="color:#475569;max-width:600px;margin:auto">Fill in your profile on the sidebar, select your skills, and click <b>Analyze Career Match</b> to discover your ideal career path.</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="section-hdr">How It Works</div>', unsafe_allow_html=True)
        c1,c2,c3 = st.columns(3)
        for col,(ic,t,d) in zip([c1,c2,c3],[("01","Build Your Profile","Enter your name, email, and select your technical skills."),("02","Analysis","The algorithm matches your profile against 15+ career paths."),("03","Get Results","Receive personalised recommendations with scores and insights.")]):
            col.markdown(f'<div class="card" style="text-align:center"><div style="font-size:2rem;font-weight:800;color:#2563eb">{ic}</div><h3 style="color:#0f172a">{t}</h3><p style="color:#475569">{d}</p></div>', unsafe_allow_html=True)

    st.markdown('<div class="footer-credit">Developed by Galih Aji Pangestu | NPM 24081010123 | OOP Class C</div>', unsafe_allow_html=True)


# ═════════════════════════════════════════════════════════════════════════════
# OOP CONCEPTS SUMMARY
# ═════════════════════════════════════════════════════════════════════════════
# 1. ENCAPSULATION  – Protected attrs (_name, _email etc.), @property decorators
# 2. INHERITANCE    – Multilevel: User → SkillProfile → CareerEngine via super()
# 3. POLYMORPHISM   – display_info() overridden in each class, extends via super()
# 4. ABSTRACTION    – Complex scoring hidden behind generate_recommendations()

if __name__ == "__main__":
    main()
