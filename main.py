
def encoder(number):
    list = []
    for i in number:
        var = int(i)
        new_num = var + 3
        fire = str(new_num)
        list.append(fire)
    new_list = ''.join(list)
    return new_list

# def decoder(digit):
#     list = []
#     for i in digit:
#         var = int(i)
#         new_num = var - 3
#         fire = str(new_num)
#         list.append(fire)
#     new_list = ''.join(list)
#     return new_list


program = True

while program == True:
    print(f'\nMenu\n------------\n1. Encode\n2. Decode\n3. Quit\n')
    menu_num = input(f"Please enter an option: ")
    if menu_num == str(1):
        password = input(f"Please enter your password to encode: ")
        encoded = encoder(password)
        print(f'Your password has been encoded and stored!')
    if menu_num == str(2):
        print(f"The encoded password is {encoded}, and the original password is {password}.")
    if menu_num == str(3):
            program = False

