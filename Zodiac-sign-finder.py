# create zodiac sign function:

def get_zodiac_sign(month,day):
    if month == 1 and day >= 20:
        return "Aquarius", "Traits: Humanitarian, Independent, Unconventional"
    elif month == 2 and day <= 18:
        return "Aquarius", "Traits: Humanitarian, Independent, Unconventional"
    elif month == 2 and day >= 19:
        return "Pisces", "Traits: Compassionate, Imaginative, Sensitive"
    elif month == 3 and day <= 20:
        return "Pisces", "Traits: Compassionate, Imaginative, Sensitive"
    elif month == 3 and day >= 21:
        return "Aries", "Traits: Adventurous, Confident, Determined"
    elif month == 4 and day <= 19:
        return "Aries", "Traits: Adventurous, Confident, Determined"
    elif month == 4 and day >= 20:
        return "Taurus", "Traits: Reliable, Practical, Sensuous"
    elif month == 5 and day <= 20:
        return "Taurus", "Traits: Reliable, Practical, Sensuous"
    elif month == 5 and day >= 21:
        return "Gemini", "Traits: Curious , Adaptable, Communicative"
    elif month == 6 and day <= 20:
        return "Gemini", "Traits: Curious , Adaptable, Communicative"
    elif month == 6 and day >= 21:
        return "Cancer", "Traits: Emotional, Nurturing, Protective"
    elif month == 7 and day <= 22:
        return "Cancer", "Traits: Emotional, Nurturing, Protective"
    elif month == 7 and day >= 23:
        return "Leo", "Traits: Passionate, Generous, Confident"
    elif month == 8 and day <= 22:
        return "Leo", "Traits: Passionate, Generous, Confident"
    elif month == 8 and day >= 23:
        return "Virgo", "Traits: Analytical, Pratical, Precise"
    elif month == 9 and day <= 22:
        return "Virgo", "Traits: Analytical, Pratical, Precise"
    elif month == 9 and day >= 23:
        return "Libra", "Traits: Diplomatic, Social, Balance"
    elif month == 10 and day <= 22:
        return "Libra", "Traits: Diplomatic, Social, Balance"
    elif month == 10 and day >= 23:
        return "Scorpio", "Traits: Passionate, Intense, Profound"
    elif month == 11 and day <= 21:
        return "Scorpio", "Traits: Passionate, Intense, Profound"
    elif month == 11 and day >= 22:
        return "Sagittarius", "Traits: Adventurous, Optimistic, freedom loving"
    elif month == 12 and day <= 21:
        return "Sagittarius", "Traits: Adventurous, Optimistic, freedom loving"
    elif month == 12 and day >= 22:
        return "Capricorn", "Traits: Disciplined, Responsible, Ambitious" 
    elif month == 1 and day <= 19:
        return "Capricorn", "Traits: Disciplined, Responsible, Ambitious" 
    else:
        return "Enter a valid 'month and day'"
    
    
# Display zodiac sign:

Z_signs = [
    "1. Aquarius",
    "Pisces",
    "Aries",
    "Taurus",
    "Gemini",
    "Cancer",
    "Leo",
    "Virgo",
    "Libra",
    "Scorpio",
    "Sagittarius",
    "Capricorn"
]

print("ZODIAC SIGNS")
for z in Z_signs:
    print(f"- {z}")
    
    

# Get month and day from user:

month = int(input("Enter your  birth 'month (1-12)': "))
day = int(input("Enter your birth 'day (1-31)': "))

#call the function:

Zodiac_sign = get_zodiac_sign(month,day)
print(f"Your Zodiac sign is: {Zodiac_sign}")



    
