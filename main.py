PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt", mode="r")as names:
    names_list = names.readlines()

len_names_list = len(names_list)

for index in range(0,int(len_names_list)):
    with open("Input/Letters/starting_letter.docx", mode="r") as letter:
        txt = letter.read()
        replaced_name = txt.replace(PLACEHOLDER, names_list[index].strip())
        print(replaced_name)
    with open(f"Output/ReadyToSend/letter_for_{names_list[index]}", mode="w") as letter_to_send:
        letter_to_send.write(replaced_name)



