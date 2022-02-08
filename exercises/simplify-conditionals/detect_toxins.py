# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).

def make_alert_sound():
    print('made alert sound.')
def make_accept_sound():
    print('made acceptance sound')

    badIngredients = ['sodium benzoate', 'sodium benzoate', 'sodium oxide']
    if badIngredients:
        make_alert_sound()
    else:
        make_accept_sound()
