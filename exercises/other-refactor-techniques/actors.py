# by Kami Bigdely
# Extract class
actor_names = ['Elizabeth Debicki', 'Jim Carrey']
birth_year = [1990, 1962]
movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],\
     ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man']]
emails = ['deb@makeschool.com', 'jim@makeschool.com']

def send_hiring_email(email):
    print("email sent to: ", email)
    
def print_actor_movies():
    print(actor_names[i])
    print('Movies Played: ', end='')
    for m in movies[i]:
        print(m, end=', ')
    print()

for i, value in enumerate(emails):
    if birth_year[i] > 1985:
        print_actor_movies()
        send_hiring_email(value)