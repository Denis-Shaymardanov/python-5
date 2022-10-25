#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open('1_input.txt', "r", encoding="utf") as file:
    input_str = file.read().split()
    smb = "абв"
    output_str = ' '.join(list(filter(lambda word: smb not in word, input_str)))
    
with open("1_output.txt", "w", encoding="utf") as file:
    file.write(output_str)