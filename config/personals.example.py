'''
Copy this file to personals.py and fill in your own values.
    cp config/personals.example.py config/personals.py
'''


###################################################### CONFIGURE YOUR TOOLS HERE ######################################################


# Your legal name
first_name = "Your"
middle_name = ""
last_name = "Name"

# Phone number (10 digits, no country code)
phone_number = "9876543210"

# Current city
current_city = "Hyderabad"   # e.g. Mumbai, Delhi, Bengaluru

# Address (used by some applications)
street = "Your City, Your State"
state = "Your State"
zipcode = "500001"
country = "India"

## US Equal Opportunity questions (leave as "Decline" if not applying to US jobs)
ethnicity = "Decline"
gender = "Decline"
disability_status = "Decline"
veteran_status = "Decline"


from config import _overrides as _o
_o.apply(__name__, globals())
