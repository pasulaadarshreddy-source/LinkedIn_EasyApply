'''
Copy this file to questions.py and fill in your own values.
    cp config/questions.example.py config/questions.py
'''


###################################################### APPLICATION INPUTS ######################################################


# Path to your resume PDF
default_resume_path = r"C:\Users\YourName\Downloads\Your_Resume.pdf"

# Years of total work/internship experience
years_of_experience = "1"

# Visa / work authorization
require_visa = "No"           # "Yes" or "No"
legally_authorized = "Yes"    # "Yes" or "No"

# Portfolio / LinkedIn
website = ""
linkedIn = "https://www.linkedin.com/in/your-profile-slug"

us_citizenship = "U.S. Citizen/Permanent Resident"

## Salary
desired_salary = 500000       # Expected CTC in INR (no quotes)
current_ctc = 0               # Current CTC in INR (0 if fresher)

## Notice period (in days)
notice_period = 0             # 0 = immediate joiner

# LinkedIn headline shown on your profile
linkedin_headline = "Your Headline | Skill1 · Skill2 | Open to Work"

# LinkedIn summary (shown when asked for a summary/bio)
linkedin_summary = """
Write your professional summary here.
Include your education, skills, and key achievements.
"""

# Cover letter template
cover_letter = """
Dear Hiring Manager,

Write your cover letter here. Mention your key skills and experience.

Regards,
Your Name
"""

# Full background info — the AI uses this to answer any application question
user_information_all = """
Name: Your Full Name
Phone: +91 XXXXXXXXXX
Location: Your City, India. Open to relocation.
Availability: Immediate joiner (0 days notice period).

Education:
- Your Degree, Your University (Year–Year)

Work Experience:
1. Your Role — Your Company (Month Year – Month Year)
   • Achievement 1
   • Achievement 2

Skills:
- Skill 1, Skill 2, Skill 3

Key Achievements:
- Achievement 1
- Achievement 2
"""

# Detailed answer for project/achievement questions
project_description = """
Describe your most impactful project here. Include:
- The problem you solved
- Tools/techniques you used
- The measurable result/impact
"""

# Answer for "what do you bring to this role" questions
value_proposition = """
Describe what makes you a strong candidate.
Focus on skills, achievements, and attitude.
"""

# Answer for "describe a challenge you faced" questions
challenge_answer = """
Describe a specific challenge from work/internship.
Explain how you identified the root cause and solved it.
"""

# Name of your most recent employer
recent_employer = "Your Most Recent Company"

# Confidence level 1-10 for technical questions
confidence_level = "7"

## Allow Manual Inputs
pause_before_submit = True
pause_at_failed_question = True
overwrite_previous_answers = False


from config import _overrides as _o
_o.apply(__name__, globals())
