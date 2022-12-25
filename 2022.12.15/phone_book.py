phone_book = []

def get_phone_book():
    global phone_book
    return phone_book

def set_phone_book(new_phone_book):
    global phone_book
    phone_book = new_phone_book

def add_contact(contact: list):
    global phone_book
    phone_book.append(contact)

def remove_contact(id):
    global phone_book
    name = phone_book[id-1][0]
    confirm = input(f'Вы действительно хотите удалить контакт {name}? (y/n)')
    if confirm.lower() == 'y':
        phone_book.pop(id-1)
        return True
    return False

def change_contact(id): #                                                               ++
    global phone_book
    name = phone_book[id-1][0]
    phone = phone_book[id-1][1]
    comment = phone_book[id-1][2]
    confirm = input(f'Вы действительно хотите изменить контакт {name}? (y/n)')
    if confirm.lower() == 'y':
        phone_book[id-1][0] = input(f'Текущее имя: {name}. Введите новое: ')
        phone_book[id-1][1] = input(f'Текущий номер телефона: {phone}. Введите новый: ')
        phone_book[id-1][2] = input(f'Текущий комментарий к контакту: {comment}. Введите новый: ')
        return True
    return False

def find_contact(find_name): #                                         ++ реализовал только поиск по полному сооответсвию имени (скромно)
    global phone_book
    for i in range(len(phone_book)):
        if phone_book[i][0] == find_name:
            print(f'Контакт найден!')
            print(*phone_book[i])
            return True
            break
    return False