'''
Copy this file to secrets.py and fill in your own values.
    cp config/secrets.example.py config/secrets.py
'''


###################################################### CONFIGURE YOUR TOOLS HERE ######################################################


# Your LinkedIn login credentials
username = "your_linkedin_email@example.com"
password = "YourLinkedInPassword"


## Artificial Intelligence (optional)
use_AI = True                            # True or False (case-sensitive)

# "openai", "gemini", or "deepseek"
ai_provider = "gemini"

# Model name — e.g. "gemini-2.5-flash", "gpt-4o-mini"
llm_model = "gemini-2.5-flash"

# Your API key. Get a free Gemini key at https://aistudio.google.com/app/apikey
# The key starts with "AIzaSy..."
llm_api_key = "YOUR_GEMINI_API_KEY_HERE"

# Only used for OpenAI-compatible providers (Ollama, LM Studio, DeepSeek, etc.)
llm_api_url = "https://api.openai.com/v1/"

# Sampling temperature. Leave as None to use the model default.
llm_temperature = None


from config import _overrides as _o
_o.apply(__name__, globals())
