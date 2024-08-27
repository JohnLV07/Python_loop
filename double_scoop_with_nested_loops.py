# Task 1: your Mood Tracker
# Simulate a moood tracker that records your mood at three diffrent times of the day (morning, afternoon, evening) for each day of the week
# Use the nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate over the times of the day
# For each time, randomly select a mood from a predefined list and print it
# Use the random module again to randomly select the mood

import random
week_days = ['Sunday', 'Monday', 'Tuesday', 'Wedensday', 'Thursday', 'Friday', 'Saturday']
time_of_the_day = ['morning', 'afternoon', 'evening']
moods = ['sad', 'happy', 'thoughtful', 'joyful', 'angry', 'melancolic']

for day in week_days:
    time = random.choice(time_of_the_day)
    mood = random.choice(moods)
    print(f'On {day} in the {time}, You were feeling {mood}' )
