PLACEHOLDER = "[name]"

with open("d24_mail_project/input/Names/invited_names.txt") as names_file:
    names = [line.strip() for line in names_file]
    
with open("d24_mail_project/input/letters/starting_letter.txt", "r") as letters_file:
    letter_contents = letters_file.read()
    for name in names:
        new_letter = letter_contents.replace(PLACEHOLDER, name)
        with open(f"d24_mail_project/output/readytosend/letter_for_{name}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)