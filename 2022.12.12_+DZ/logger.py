path = 'calc_log.txt'

def save_data_base(log_text):
    with open(path, 'a', encoding='UTF-8') as file:
        file.writelines(log_text)
        file.writelines('\n')