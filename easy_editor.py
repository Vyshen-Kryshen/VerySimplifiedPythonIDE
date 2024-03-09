import easygui


def easyeditor() -> None:
    while True:
        file_path = easygui.fileopenbox(f'', 'Файловое древо')
        file_name = str(file_path.split('\u005C')[-1])
        file_extension = file_name.split('.')[-1]
        if file_extension == 'py':
            with open(file_path, 'r', encoding='UTF-8') as f:
                read_file = f.read()
                redacted_content = easygui.codebox('Это простенький редактор кода, за авторством Рината Зейналова. Он '
                                                   'является сугубо моим эксперементом в использовании библиотеки: '
                                                   'EasyGUI - не более.',
                                                   file_name, f'{read_file}')
                if redacted_content != read_file:
                    question = easygui.boolbox('Хотите ли вы сохранить изменения?', 'Вопрос сохранения.', ['Да', 'Нет'])
                    if question and redacted_content:
                        with open(file_path, 'w', encoding='UTF-8') as f_w:
                            f_w.write(redacted_content)
                running = easygui.boolbox('Запустить код на исполнение?', 'Вопрос запуска.', ['Да', 'Нет'])
                if running:
                    with open(file_path, 'r', encoding='UTF-8') as f_r:
                        rd = f_r.read()
                        exec(str(rd))
        else:
            raise FileExistsError(f'Формат {file_extension}, файла: {file_name} - не поддерживается!\n'
                                  f'К просмотру доступны файлы формата .py')


if __name__ == '__main__':
    easyeditor()
