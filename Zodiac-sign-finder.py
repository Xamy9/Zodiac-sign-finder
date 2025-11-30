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
    
    


# Months in a year list:
Months =  ["1. January", "2. February", "3. March", "4. April", "5. May", "6. June"
           , "7. July", "8. August", "9. September", "10. October", "11. November", "12. December"
           ]



# Loop through months and display them:
print("MONTHS IN A YEAR")
for m in Months:
    print(m)
    
    
    
# Zodiac signs lists:
Zodiac_signs = ["Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", 
           "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn"
           ]


# Loop through zodiac signs and display them:
print("ZODIAC SIGNS")
for z in Zodiac_signs:
    print(f"- {z}")
       
    
    

# Get month and day from user:
month = int(input("Enter your  birth 'month (1-12)': "))
day = int(input("Enter your birth 'day (1-31)': "))


#call the function:
Zodiac_sign = get_zodiac_sign(month,day)
print(f"Your Zodiac sign is: {Zodiac_sign}")




    
