# LinkedIn Easy Apply Bot

Automates LinkedIn Easy Apply job applications — fills forms, answers questions, and submits — so you can focus on interviews instead of clicking.

---

## The Problem It Solves

Applying to 20–30 jobs a day on LinkedIn means repeating the same steps hundreds of times:
- Open job → Click Easy Apply → Fill name, phone, salary, experience → Answer 5–10 questions → Submit → Repeat

This bot handles that entire loop automatically for every job that matches your criteria.

---

## How It Works

```
Start bot
   │
   ├── Search LinkedIn for your target job titles + location
   │
   ├── For each job listing:
   │     ├── Check job title → skip if it's Sales / BD / Marketing (configurable)
   │     ├── Open Easy Apply form
   │     ├── Fill every field from your config (name, phone, salary, resume...)
   │     ├── Answer yes/no and dropdown questions using built-in logic
   │     ├── Answer open text questions using Gemini AI
   │     └── Submit application
   │
   └── Log all applications to a CSV file
```

Anti-detection is built in — random mouse movement, 3-second delays between actions, and an automatic filter switch from "Past 24 hours" to "Past 1 hour" after 15 minutes of running.

---

## Setup

### Requirements
- Python 3.10 or higher
- Google Chrome (latest)
- A LinkedIn account
- A free Gemini API key — get one at https://aistudio.google.com/app/apikey

### 1. Clone the repository

```bash
git clone https://github.com/pasulaadarshreddy-source/LinkedIn_EasyApply.git
cd LinkedIn_EasyApply
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create your config files

The repo ships example files with placeholders. Copy and rename them:

```bash
cp config/secrets.example.py config/secrets.py
cp config/personals.example.py config/personals.py
cp config/questions.example.py config/questions.py
```

Each file has comments explaining every field. Fill in your own values:

| File | What goes in it |
|---|---|
| `config/secrets.py` | LinkedIn login credentials + Gemini API key |
| `config/personals.py` | Name, phone number, city, address |
| `config/questions.py` | Resume path, LinkedIn URL, expected salary, cover letter, skills summary |

### 4. Configure your job search

Open `config/search.py`. The key settings are:

```python
search_terms = ["Data Analyst", "MIS Analyst", "Operations Analyst"]   # what to search
search_location = "India"                                               # where
experience_level = ["Entry level"]                                      # filter
allowed_title_keywords = ["analyst", "data", "mis", "operations"]       # apply to these
blocked_title_keywords = ["sales", "recruiter", "telecaller"]           # always skip these
```

### 5. Run

```bash
python app.py
```

Open `http://localhost:5000` in your browser to use the control panel, or run headlessly:

```bash
python runAiBot.py
```

---

## Changing the Target Domain

The bot works for any job field. Edit `config/search.py` — no other file needs to change.

**Software Engineering**
```python
search_terms = ["Software Engineer", "Backend Developer", "SDE"]
allowed_title_keywords = ["engineer", "developer", "software", "backend", "frontend", "sde", "devops"]
```

**Finance & Accounting**
```python
search_terms = ["Finance Analyst", "Accountant", "Audit Associate"]
allowed_title_keywords = ["finance", "financial", "accountant", "audit", "tax", "banking"]
```

**Marketing**
```python
search_terms = ["Marketing Analyst", "Growth Analyst", "Digital Marketing"]
allowed_title_keywords = ["marketing", "brand", "growth", "content", "seo", "campaign"]
```

**HR**
```python
search_terms = ["HR Analyst", "HR Executive", "Talent Acquisition"]
allowed_title_keywords = ["hr", "human resources", "talent", "recruitment", "hrbp", "people"]
```

---

## Question Answering Logic

The bot answers application questions in this order of priority:

1. **Direct match** — if the question matches a known field (salary, notice period, experience), it uses your config value
2. **Smart Yes/No** — for yes/no questions it applies rules:
   - Willing to relocate / travel / work shifts → **Yes**
   - Do you hold CA / CFA / PhD / MBBS → **No**
   - Previously employed at military / government → **No**
   - Unknown → **No** (safe default)
3. **Gemini AI** — for open-ended text questions it generates a contextual answer using your profile
4. **Context fallback** — if AI is unavailable, it picks the most relevant fallback answer based on question keywords (improvement questions, weakness questions, strength questions, etc.)

---

## Output

All applications are logged automatically to:
```
all excels/all_applied_applications_history.csv
all excels/all_failed_applications_history.csv
```

Each row records the job title, company, location, date applied, and any questions that needed manual review.

---

## Recommended Usage

- Run for **20–25 minutes per day** maximum to stay under LinkedIn's detection threshold
- Keep `pause_before_submit = True` in `config/questions.py` while testing — it pauses before each submit so you can review
- Set it to `False` once you're confident in your config for fully automatic operation
