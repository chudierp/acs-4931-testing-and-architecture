# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
Well_done = 900000
Medium = 600000
Cooked_constant = 0.05

def is_cooked_criteria_satisfied(time, temperature, pressure, desired_state):
    current_state = time * temperature * pressure * Cooked_constant
    if desired_state == 'weel-done' and current_state >= Well_done:
        return True
    if desired_state == 'medium' and current_state >= Medium:
        return True
    return False