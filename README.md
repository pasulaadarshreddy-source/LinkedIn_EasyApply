# LinkedIn Easy Apply Bot — Customized for Analyst & Operations Roles (India)

An automated LinkedIn Easy Apply bot customized for **Data Analyst, Business Analyst, MIS, Operations, and Reporting** roles in India. Built on top of [Auto_job_applier_linkedIn](https://github.com/GodsScion/Auto_job_applier_linkedIn) by GodsScion.

---

## What this bot does

- Automatically applies to Easy Apply jobs on LinkedIn
- Filters jobs by title — only applies to analyst/data/operations/MIS roles, skips Sales, BD, Marketing
- Answers application questions intelligently using your profile data + Gemini AI
- Anti-detection: slow clicks, mouse drift, randomized delays
- Switches from "Past 24 hours" to "Past 1 hour" filter automatically after 15 minutes
- Skips duplicate applications

---

## Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/pasulaadarshreddy-source/LinkedIn_EasyApply.git
cd LinkedIn_EasyApply
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure your details

Copy the three example config files and fill in your own information:

```bash
cp config/secrets.example.py config/secrets.py
cp config/personals.example.py config/personals.py
cp config/questions.example.py config/questions.py
```

**`config/secrets.py`** — Your LinkedIn login + Gemini AI key
- Get a free Gemini API key at https://aistudio.google.com/app/apikey

**`config/personals.py`** — Your name, phone, city, address

**`config/questions.py`** — Your resume path, LinkedIn URL, salary, skills, cover letter

### 4. Configure your job search

Edit `config/search.py` to set your preferred:
- Job titles to search
- Location
- Experience level
- Date posted filter

### 5. Run the bot

```bash
python app.py
```

Then open `http://localhost:5000` in your browser to use the control panel.

Or run directly:

```bash
python runAiBot.py
```

---

## Job roles it applies to

- Data Analyst / Business Analyst / MIS Analyst
- Operations Analyst / Operations Executive
- Reporting Analyst / MIS Reporting / MIS Executive
- Research Analyst / Financial Analyst
- Data Associate / Data Specialist / Data Entry

---

## Requirements

- Python 3.10+
- Google Chrome installed
- LinkedIn account
- Gemini API key (free tier works)

---

## Credits

Original project: [GodsScion/Auto_job_applier_linkedIn](https://github.com/GodsScion/Auto_job_applier_linkedIn)

Customizations by [Adarsh Reddy Pasula](https://www.linkedin.com/in/adarsh-reddy-pasula)
