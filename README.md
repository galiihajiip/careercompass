# 🧭 CareerCompass AI — Career Recommendation + Action Plan CRUD

A **production-grade** career recommendation and career action-plan management system built with Python, Streamlit, and advanced OOP principles.

## ✨ Features

- **Multilevel Inheritance**: `User → SkillProfile → CareerEngine`
- **Complex Scoring Algorithm**: Weighted multi-factor matching (not simple if-else)
- **15+ Career Paths** with detailed requirements and metadata
- **50+ Skills** to choose from across programming, frameworks, and domains
- **Modern Dashboard UI** with dark theme, custom CSS, and Plotly charts
- **Input Validation** with real-time feedback
- **Export** recommendations as JSON or text
- **EAS/UAS CRUD Module** for creating, reading, updating, and deleting career action plans
- **Polymorphic Action Plans**: technical skill, soft skill, and portfolio project plans
- **Class Relationships**: inheritance, aggregation, composition, dependency, and association

## 🏗️ OOP Concepts Demonstrated

| Concept | Implementation |
|---------|---------------|
| **Encapsulation** | Protected attributes (`_name`, `_email`), `@property` decorators |
| **Inheritance** | Multilevel: `User → SkillProfile → CareerEngine` via `super()` |
| **Polymorphism** | `display_info()`, `get_plan_type()`, and `priority_score()` overridden in derived classes |
| **CRUD** | `CareerPlanManager` and `CareerPlanRepository` manage action-plan data |
| **Class Relationships** | Inheritance, aggregation, composition, dependency, association |
| **Abstraction** | Complex scoring hidden behind `generate_recommendations()` |

## 🚀 Quick Start

```bash
pip install -r requirements.txt
streamlit run career_system.py
```

## 📁 File Structure

```
ets-oop/
├── career_system.py                  # Main Streamlit application
├── LAPORAN_UTS_CAREERCOMPASS.md      # UTS documentation
├── LAPORAN_UAS_CAREER_ACTION_PLAN.md # UAS/EAS documentation
├── SCRIPT_VIDEO_DEMO_UAS.md          # UAS demo video script
├── requirements.txt                  # Dependencies
└── README.md                         # This file
```

## 🧠 Scoring Algorithm

```
SCORE = (Required Skills Match [0-40]
       + Preferred Skills Match [0-25]
       + Interest Field Bonus [0-15])
       × Skill Level Modifier
       × Work Preference Multiplier
       × (Career Popularity / 100)
```

## 📋 Dependencies

- `streamlit >= 1.28.0`
- `plotly >= 5.17.0`
- `pandas >= 2.0.0`
