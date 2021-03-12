# -*- coding: utf-8 -*-
"""
Python packer for Windows.

@author:  Кирилл safezone.cc
"""
import tkinter as tk
from tkinter import filedialog as fd
import os as os
import PyInstaller.__main__

root = tk.Tk()
checkbuttons_id = int()
object_id = int()


class Buttons():
    """Класс отвечает за создание и работу кнопок, переключателей и прочих \
    управляющих элементов."""

    def __init__(self, root='root'):
        # Корневой фрейм
        self.root = root
        # Флаг checkbutton
        self.flag_check = tk.BooleanVar()
        self.flag_check.set(0)
        # Координаты расположения checkbutton
        self.axle_x = int(350)
        self.axle_y = int(25)

    def checkbuttons(self, *kwargz):
        """На вход принимаем параметры checkbutton. \
        Упаковываем и задаем рабочие параметры."""
        global checkbuttons_id, object_id

        self.object, self.text = kwargz
        if self.object.endswith('text'):
            object_id += 1
            self.object = tk.Entry()
            self.object.insert(0, self.text)
            self.object.place(x=20, y=(380 - object_id*self.axle_y),
                              width=400, height=25)

            self.object_bt = tk.Button()
            self.object_bt.place(x=425, y=(380 - object_id*self.axle_y))

        elif self.object.endswith('label'):
            object_id += 1
            self.object = tk.Label(text=self.text)
            self.object.place(x=20, y=(380 - object_id*self.axle_y))
        else:
            checkbuttons_id += 1
            self.object = tk.Checkbutton(text=self.text,
                                         variable=self.flag_check,
                                         onvalue=1, offvalue=0,
                                         command=self.check_select)
            self.object.place(x=self.axle_x, y=(self.axle_y * checkbuttons_id))

    def check_select(self):
        """Event select scheckbox."""
        if self.flag_check.get():
            print(self.text)
            if check_onefile.flag_check.get():
                check_onefolder.flag_check.set(0)
        else:
            print('Отменено: ' + self.text)
        if check_icon.flag_check.get():
            if not icon_patch_text.object.get().lower().endswith('.ico'):
                if icon_patch_text.object.get() != '':
                    icon_patch_text.object.delete(0, 'end')
                icon_patch_text.object.insert(
                    0, 'Выберите файл с расширением \'.ico\'')
                print('Выберите файл с расширением \'.ico\'')
                check_icon.flag_check.set(0)

    def objects_id(self, *kwargz):
        """
        На вход принимаем параметры object - прочие элементы на форме.

        Упаковываем и задаем рабочие параметры
        """
        global object_id
        object_id += 1
        self.object, self.text = kwargz
        self.object = tk.Entry(text=self.text)
        self.object.place(x=self.axle_x, y=300-20*object_id)


#############################################################################
# Функция сборки пректа
def file_compilled():
    """Параметры Pyinstaller в порядке их выполнения."""
    py_compiled_list = ['--name=%s' % input_name_file.get()]
    if check_clean.flag_check.get():
        py_compiled_list.insert(0, '--clean')
    if check_onefile.flag_check.get():
        py_compiled_list.append('-F')
    if check_onefolder.flag_check.get():
        py_compiled_list.append('-D')
    if check_noconsole.flag_check.get():
        py_compiled_list.append('-w')
    if check_icon.flag_check.get():
        py_compiled_list.append('-i=%s' % icon_patch_text.object.get())
    if check_admin.flag_check.get():
        py_compiled_list.append('--uac-admin')
    py_compiled_list.append(os.path.abspath(input_patch_file.get()))
    PyInstaller.__main__.run(py_compiled_list)
#############################################################################


# Checkbutton - экземпляры класса
# Требовать права Администратора
check_admin = Buttons(root)
# Отключить запуск консоли
check_noconsole = Buttons(root)
# Сборка в один файл
check_onefile = Buttons(root)
# Сборка в одну папку
check_onefolder = Buttons(root)
# очистить временные файлы
check_clean = Buttons(root)
# задать иконку к сборке файла
check_icon = Buttons(root)
# label с адресом иконки проекта
icon_patch_label = Buttons(root)
# текстовое поле с адресом места иконки
icon_patch_text = Buttons(root)
# текстовое поле с адресом места сборки
pack_patch_file_text = Buttons(root)
# label с адресом места сборки
pack_patch_file_label = Buttons(root)
list_check = [
    check_noconsole.checkbuttons('check_noconsole',
                                 'Отключить запуск терминала'),
    check_onefile.checkbuttons('check_onefile', 'Сборка в один файл'),
    check_onefolder.checkbuttons('check_onefolder', 'Сборка в одну папку'),
    check_clean.checkbuttons('check_clean', 'Очистить временные файлы'),
    check_icon.checkbuttons('check_icon', 'Задать иконку к файлу'),
    icon_patch_text.checkbuttons('icon_patch_text', '.....'),
    icon_patch_label.checkbuttons('icon_text_label',
                                  'Задать иконку для проекта:'),
    pack_patch_file_text.checkbuttons('pack_patch_file_text',
                                      os.getcwd() + "\\dist\\"),
    pack_patch_file_label.checkbuttons('pack_patch_file_label',
                                       'Проект будет сохранен по адресу:'),
    check_admin.checkbuttons('check_admin', 'Требовать права Админитратора'), ]


def bt_open_func():
    """
    Кнопка открыть рабочий каталог.

    Функция проверяет наличие пути, указанного в поле ввода
    Если адрес недоступен - создает каталог в полном соответствии
    с введенными данными в текстовом поле
    """
    if os.path.isdir(pack_patch_file_text.object.get()):
        os.system('explorer %s' % os.path.abspath(
            pack_patch_file_text.object.get()))
    else:
        os.mkdir(pack_patch_file_text.object.get())
        os.system('explorer %s' % os.path.abspath(
            pack_patch_file_text.object.get()))


def file_setting():
    """
    Диалоговое окно выбора скрипта Python для сборки.

    Проверяет, действительно ли выбран файл с расширением .py
        ---> Если да, удаляем содержимое текстового поля (input_patch_file),
             если не пустое. Затем записываем туда путь до файла
             В поле с именем файла (input_name_file) -
                                    автомтически пишем имя выбранного файла
             Далее активируем кнопку компилляции (bt_run)
        ---> Если выбран файл не с расширением .py, то выводим соответствующее
             сообщение, а так же деактивируем кнопки, если активны
    """
    file_name = fd.askopenfilename(title='Выберите файл для сборки',
                                   filetypes=[('Python File', '.py'),
                                              ('Python File', '.pyw')])
    if file_name:
        input_patch_file.delete(0, 'end')
        input_patch_file.insert(0, file_name)
        if not input_name_file.get():
            input_name_file.insert(0, os.path.splitext(
                                   os.path.basename(file_name))[0])
        bt_run.place(x=20, y=125, height=25)
        return file_name


def icon_patch_open():
    """Функция - иконка проекта. Проверка и обработка."""
    icon_name = fd.askopenfilename(title='Выберите файл иконки',
                                   filetypes=[('images', '*.ico')])
    if icon_name.lower().endswith('.ico'):
        icon_patch_text.object.delete(0, 'end')
        icon_patch_text.object.insert(0, icon_name)
        return icon_name


if __name__ == '__main__':

    # ###################################################################### #
    # Поле ввода - имя файла и путь к нему
    input_patch_file = tk.Entry()
    input_patch_file.place(x=20,  y=25, width=240, height=25)

    name_patch_file = tk.Label(text='Укажите путь к вашему файлу')
    name_patch_file.place(x=20, y=3, width=180)

    # Кнопка диалога выбора файла, который будем компиллировать
    bt_patch = tk.Button(text='...', command=file_setting)
    bt_patch.place(x=260, y=25, height=25)

    # Поле ввода - имя для проекта
    input_name_file = tk.Entry()
    input_name_file.place(x=20, y=75, width=240, height=25)

    # Кнопка "Запустить сборку"
    bt_run = tk.Button(text='Запустить сборку!', command=file_compilled)

    # Lbel name file
    name_your_file = tk.Label(text='Как вы назовете ваш проект?')
    name_your_file.place(x=20, y=50, width=180)

    # ###################################################################### #

    # Указываем параметры отдельных объектов, если нужно.
    # Деактивируем текстовое поле указания рабочего каталога
    pack_patch_file_text.object.configure(state='disable')
    # Кнопка открытия рабочего каталога
    pack_patch_file_text.object_bt.configure(text='open', command=bt_open_func)
    # Кнопка пути к иконке...
    icon_patch_text.object_bt.configure(text='open', command=icon_patch_open)
    root.title("Упаковщик скриптов Python в .exe")
    root.geometry('600x400')
    root.resizable(0, 0)
    root.mainloop()
    root.mainloop()
