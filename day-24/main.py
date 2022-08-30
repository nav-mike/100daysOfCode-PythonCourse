with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    starting_letter = letter.read()

for name in names:
    with open(f"./Output/ReadyToSend/{name.strip()}.txt", "w") as output:
        output.write(starting_letter.replace("[name]", name.strip()))
