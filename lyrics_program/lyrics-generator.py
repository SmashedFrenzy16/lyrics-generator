import sys


again = True

print("Welcome to NFT Media Library! Type in the number of the song that you want to generate its lyrics.")
print("Please choose a list of songs below: ")

print("1. Sorry by Justin Bieber")
print("2. Hello by Adele")
print("3. Hey Jude by John Lennon and Paul McCartney")
print("4. Chasing Pavements by Adele")
print("5. Never Say Never by Justin Bieber")

songArtist = {

    "1": "Sorry by Justin Bieber",
    "2": "Hello by Adele",
    "3": "Hey Jude by John Lennon and Paul McCartney",
    "4": "Chasing Pavements by Adele",
    "5": "Never Say Never by Justin Bieber"

}

song = input("Enter the number of the song you want: ")

if song == "1":

    print("\nYou have chosen:", songArtist.get("1"))

    file_sorry = open("sorry_bieber.txt", "r")
    print(file_sorry.read())

elif song == "2":

    print("\nYou have chosen:", songArtist.get("2"))

    file_hello = open("hello_adele.txt", "r")
    print(file_hello.read())

elif song == "3":

    print("\nYou have chosen:", songArtist.get("3"))

    file_hey_jude = open("hey_jude_j_p.txt", "r")
    print(file_hey_jude.read())

elif song == "4":

    print("\nYou have chosen:", songArtist.get("4"))

    file_chasing_pavements = open("chasing_pavements_adele.txt", "r")
    print(file_chasing_pavements.read())

elif song == "5":

    print("\nYou have chosen:", songArtist.get("5"))

    file_never_say_never = open("never_say_never_bieber.txt", "r")
    print(file_never_say_never.read())

else:
    print("\nError 404: Song not found!")

print("\nPress any button to choose again")


def replay():
    play_again = input("Press any button to choose again")
    if play_again.casefold() == "*":
        return True
    else:
        return False
        sys.exit()

replay()

while again:

    print("Welcome to NFT Media Library! Type in the number of the song that you want to generate its lyrics.")
    print("Please choose a list of songs below: ")

    print("1. Sorry by Justin Bieber")
    print("2. Hello by Adele")
    print("3. Hey Jude by John Lennon and Paul McCartney")
    print("4. Chasing Pavements by Adele")
    print("5. Never Say Never by Justin Bieber")

    song = input("Enter the number of the song you want: ")

    if song == "1":

        print("\nYou have chosen:", songArtist.get("1"))

        file_sorry = open("sorry_bieber.txt", "r")
        print(file_sorry.read())

    elif song == "2":

        print("\nYou have chosen:", songArtist.get("2"))

        file_hello = open("hello_adele.txt", "r")
        print(file_hello.read())

    elif song == "3":

        print("\nYou have chosen:", songArtist.get("3"))

        file_hey_jude = open("hey_jude_j_p.txt", "r")
        print(file_hey_jude.read())

    elif song == "4":

        print("\nYou have chosen:", songArtist.get("4"))

        file_chasing_pavements = open("chasing_pavements_adele.txt", "r")
        print(file_chasing_pavements.read())

    elif song == "5":

        print("\nYou have chosen:", songArtist.get("5"))

        file_never_say_never = open("never_say_never_bieber.txt", "r")
        print(file_never_say_never.read())

    else:
        print("\nError 404: Song not found!")
    
    replay()
