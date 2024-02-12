# file = open('quotes.txt', 'w', encoding = 'utf-8')
# print(file.writable())
# file.write('Собака гуляла рядом с домом')
# file.close()

# with open('quotes.txt', 'a', encoding = 'utf-8') as file:
#     file.write('\nМальчик играл на гитаре')
fail = input('Название файла: ')
while True:

    try: 



        with open(fail, 'r', encoding = 'utf-8') as file:
            data = file.read()
            print(data)

        # res = input('Введите цитаты автора')
        # with open('quotes.txt', 'a', encoding = 'utf-8') as file:
        #     file.write(f'\n({res})')

        while input('Хотите добавить еще одну цитату?') == 'да':
            res2 = input('Введите еще одну цитату: ')
            res3 = input('Введите автора: ')
            with open(fail, 'a', encoding = 'utf-8') as file:
                file.write(f'\n{res2}\n{res3}')
        with open(fail, 'r', encoding = 'utf-8') as file:
            data = file.read()
            print(data)
        break
    except IOError:
        fail = input('Неверное название файла, попробуйте еще раз: ')


    
