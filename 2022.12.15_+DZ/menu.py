import view, phone_book as pb, data_base as db

def main_menu(choise: int):
    match choise:
        case 1: # Показать телефонную книгу
            phone_book = pb.get_phone_book()
            view.print_phone_book(phone_book)
        case 2: # Открыть файл
            db.load_data_base()
            view.load_success()
        case 3: # Сохранить файл
            db.save_data_base()
            view.save_success()
        case 4: # Добавить контакт
            contact = view.input_new_contact()
            pb.add_contact(contact)
        case 5: # Изменить контакт                       ++
            phone_book = pb.get_phone_book()
            view.print_phone_book(phone_book)
            id = view.input_change_contact()
            if pb.change_contact(id):
                view.change_success()
        case 6: # Удалить контакт
            phone_book = pb.get_phone_book()
            view.print_phone_book(phone_book)
            id = view.input_remove_contact()
            if pb.remove_contact(id):
                view.remove_success()
        case 7: # Найти контакт                          ++
            find_name = view.input_finding_contact()
            if pb.find_contact(find_name) == False:
                view.find_failed()
        case 0: # Выход
            return True

def start():
    while True:
        choise = view.main_menu()
        if main_menu(choise):
            view.log_off()
            break