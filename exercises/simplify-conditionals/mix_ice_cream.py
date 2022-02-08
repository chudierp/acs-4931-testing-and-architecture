# by Kami Bigdely
# Consolidate duplicate conditional fragments

def add(mix, something):
    mix.append(something)
    return mix

def mixer_ice_with_cream():
    print('mixed ice with cream.')
    return ['ice', 'cream']

def make_drink(drink, addons):
    if 'coffee' in drink:
        add()
    if 'strawberry milkshake' in drink:
        mixer_ice_with_cream(addons)
    return drink

final_drink = make_drink('strawberry milkshake', ['milk','sugar'])
print(final_drink)
