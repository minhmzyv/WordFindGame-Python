name = input("Adınızı Daxil Edin: ")
print("Salam " + name + " əvvəlcədən təyin olunmuş sözü tapın...")

secret_word = "developer"

guess_string = ""

lives = 10

while lives > 0:

    character_left = 0

    for character in secret_word:

        if character in guess_string:

            print(character)

        else:

            print("-")
            character_left += 1

    if character_left == 0:
            print(name + "Siz Qazandınız...")
            break
    

    guess = input("Bir Hərf Təxmin Et: ")
    guess_string += guess
    
    if guess not in secret_word:
            lives -= 1
            print("Səhv Hərf !!!")
            print(f"Sənin + {lives} + Canın Qaldı")
    if lives == 0:
            print(name + " Siz Uduzdunuz")