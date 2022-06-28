import main

enter = 0
while True:
    enter = int(input('\nPick a number 1 to 4, 5 is exit  '))
    if enter == 1:
        main.find_names()
    if enter == 2:
        main.find_emails()
    if enter == 3:
        main.find_file_names()
    if enter == 4:
        main.find_colors()
    if enter == 5:
        print(f'The end')
        break
