# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
Well_done = 900000
Medium = 600000
Cooked_constant = 0.05

def is_cookeding_criteria_satisfied(time, temperature, pressure, desired_state):
    if desired_state == 'well-done' and cook_state(time, temperature, pressure) >= Well_done: 
        return True
    if desired_state == 'medium' and cook_state(time, temperature, pressure) >= Medium:
        return True
    return False

def cook_state(time, temperature, pressure):
    return time * temperature * pressure * Cooked_constant  