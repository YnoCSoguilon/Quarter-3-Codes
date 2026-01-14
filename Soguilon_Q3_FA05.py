import numpy as np

participants = ["Me", "Lia", "Jake"]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
daily_steps = [
    [4500, 5200, 4800, 5000, 5300],  # Me
    [4000, 4100, 3900, 4200, 4600],  # Lia  
    [6000, 5800, 5900, 6100, 6200]   # Jake
]

peak_steps = 0
highest_day = ""

def daily_total(array_2d, day_idx):
    data_matrix = np.array(array_2d)
    return data_matrix[:, day_idx].sum()

# Sum steps for each weekday across all participants
for day_num in range(len(weekdays)):
    day_total = daily_total(daily_steps, day_num)
    print(f"Total steps on {weekdays[day_num]}: {day_total}")
    
    if day_total > peak_steps:
        peak_steps = day_total
        highest_day = weekdays[day_num]

print(f"Busiest day: {highest_day} ({peak_steps} total steps)")
