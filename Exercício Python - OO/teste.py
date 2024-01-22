from keyboard import *
def get_input_masked(mask):
    input_data = ''
    current_index = 0
    while True:
        char = readkey()

        if char == key.ENTER and current_index == len(mask):
            break

        elif char == key.BACKSPACE:
            if current_index > 0:
                input_data = input_data[:-1]
                current_index -= 1
                print('\b \b', end="", flush=True)

        elif char.isdigit() and current_index < len(mask):
            if current_index < len(mask):
                special_character = None
                match mask[current_index]:
                    case '.':
                        special_character = '.'

                    case '-':
                        special_character = '-'

                    case '/':
                        special_character = '/'

                    case '(':
                        special_character = '('

                    case ')':
                        special_character = ')'

                if special_character:
                    print(special_character, end='', flush=True)
                    current_index += 1 

            input_data += char
            print(char, end='', flush=True)
            current_index += 1

    print()
    return input_data

# Adicionei a importação da biblioteca keyboard e definição de key para testar o código


masks = {'cpf':'###.###.###-##', 'cep':'#####-###', 'cnpj':'##.###.###/####-##', 'phone':'(##)#####-####'}
values = {'cpf':'', 'cep':'', 'cnpj':'', 'phone':''}

for k, mask in masks.items():
    print(f"Enter your {k}:")
    values[k] = get_input_masked(mask)
