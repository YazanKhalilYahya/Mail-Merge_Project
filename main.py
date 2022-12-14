#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("starting_letter.txt", "r") as f:
    l1 = f.read().replace("[", "")
    l2 = l1.replace("]", "")

with open("invited_names.txt", "r") as file:
    for line in file:
        new_letter = l2.replace("name", line)
        if len(line) >= 4:
            name = line[0:len(line)-1]
        else:
            name = line[0:len(line)]
        with open(f"../day24/ReadyToSend/letter_for_{name}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)


