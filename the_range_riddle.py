# Task 1: Your Mood Today:
# Write a program that prints off diffrent moods fir each day of the week, Create a list of moods as 'Happy', ',Sad', 'Energetic', and 'Calm'
# Using the range() function, loop through every of the week and for each day, randomly select a mood from the list and print it.
# Ensure that your program includes the use of random module to select the mood 
# Example Outcom: An example output could be "On Wedensday, you wee feeling happy", "On Thursday you were feeling sad"

import random
week_days = ['Sunday', 'Monday', 'Tuesdtay', 'Wedensday', 'Thursday', 'Friday', 'saturday']
moods = ['Happy', 'Sad', 'Energetic', 'Calm']
mood_per_day = {day: random.choice(moods) for day in week_days}
for day in week_days:
    mood = mood_per_day[day]
    print(f"On {day} you were feeling {mood}")
    
