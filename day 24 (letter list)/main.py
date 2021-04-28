PLACEHOLDER = "[name]"

with open("invited_names.txt") as names_from_file:
    names = names_from_file.readlines()
    print(names)

with open("starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"{stripped_name}_letter.txt", mode="w") as letter:
            letter.write(new_letter)

