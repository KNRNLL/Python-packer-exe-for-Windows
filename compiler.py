# -*- coding: utf-8 -*-
"""
Python compiler for Windows

@author:  Кирилл safezone.cc
"""
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk
import os as os
import PyInstaller.__main__

checkbuttons_id = int()


class Buttons():
    '''
        Класс отвечает за создание и работу кнопок
        переключателей и прочих управляющих элементов
    '''
    def __init__(self, root='root'):
        # Корневой фрейм
        self.root = root
        # Флаг checkbutton
        self.flag_check = tk.BooleanVar()
        self.flag_check.set(0)
        # Координаты расположения checkbutton
        self.axle_x = int(300)
        self.axle_y = int(20)

    def checkbuttons(self, *kwargz):
        '''
            На вход принимаем параметры checkbutton
            Упаковываем и задаем рабочие параметры
        '''
        # Счетчик checkbutton
        global checkbuttons_id
        checkbuttons_id += 1
        self.object, self.text = kwargz[0], kwargz[1]
        self.object = tk.Checkbutton(text=self.text,
                                     variable=self.flag_check,
                                     onvalue=1, offvalue=0,
                                     command=self.check_select)
        self.object.place(x=self.axle_x, y=(self.axle_y * checkbuttons_id))

    def check_select(self):
        if self.flag_check.get():
            print(self.text)
        else:
            print('Отменено: ' + self.text)


root = tk.Tk()

# Checkbutton - экземпляры класса
check_admin = Buttons(root)
check_noconsole = Buttons(root)
check_onefile = Buttons(root)
check_clean = Buttons(root)
list_check = [
              check_noconsole.checkbuttons('check_noconsole',
                                           'Отключить запуск терминала'),
              check_onefile.checkbuttons('check_onefile',
                                         'Сборка в один файл'),
              check_clean.checkbuttons('check_clean',
                                       'Очистить временные файлы')]
# check_admin.checkbuttons('check_admin', 'Требовать права Админитратора'),


def bt_open_func()-> 'open folder':
    '''
        Кнопка открыть рабочий каталог
        Функция проверяет наличие пути, указанного в поле ввода
        Если адрес недоступен - создает каталог в полном соответствии
        с введенными данными в текстовом поле
    '''

    if os.path.isdir(save_patch_file.get()):
        os.system('explorer %s' % os.path.abspath(save_patch_file.get()))
    else:
        os.mkdir(save_patch_file.get())
        os.system('explorer %s' % os.path.abspath(save_patch_file.get()))


def file_setting():
    '''
        Диалоговое окно выбора скрипта Python для компилляции
        Проверяет, действительно ли выбран файл с расширением .py

        ---> Если да, удаляем содержимое текстового поля (input_patch_file),
             если не пустое. Затем записываем туда путь до файла
             В поле с именем файла (input_name_file) -
                                     автомтически пишем имя выбранного файла
             Далее активируем кнопку компилляции (bt_run)

        ---> Если выбран файл не с расширением .py, то выводим соответствующее
             сообщение, а так же деактивируем кнопки, если активны
    '''
    file_name = fd.askopenfilename()
    if file_name.endswith('.py'):
        if input_patch_file.get() != '':
            input_patch_file.delete(0, 'end')
        input_patch_file.insert(0, file_name)
        if input_name_file.get() == '':
            input_name_file.insert(0, os.path.basename(file_name))
        if len(bt_run.place_info()) < 1:
            bt_run.place(x=20, y=125, height=25)
        return file_name
    else:
        if input_patch_file.get() != '':
            input_patch_file.delete(0, 'end')
        input_patch_file.insert(0, 'Выберите файл с расширением \'.py\'')
        if len(bt_run.place_info()) > 0:
            bt_run.place_forget()


# Функция компилляций файла
def file_compilled():

    py_compiled_list = ['--name=%s' % input_name_file.get()]
    if check_onefile.flag_check.get():
        py_compiled_list.append('-F')
    if check_noconsole.flag_check.get():
        py_compiled_list.append('-w')
    py_compiled_list.append(os.path.abspath(input_patch_file.get()))
    if check_clean.flag_check.get():
        py_compiled_list.append('--clean')
    PyInstaller.__main__.run(py_compiled_list)


# Поле ввода - имя файла и путь к нему
input_patch_file = tk.Entry()
input_patch_file.place(x=20,  y=25,
                       width=240, height=25)

name_patch_file = tk.Label(text='Укажите путь к вашему файлу')
name_patch_file.place(x=20, y=3, width=180)

# Кнопка диалога выбора файла, который будем компиллировать
bt_patch = tk.Button(text='...', command=file_setting)
bt_patch.place(x=260, y=25, height=25)

# Поле ввода - имя для компиллируемого проекта
input_name_file = tk.Entry()
input_name_file.place(x=20, y=75,
                      width=240, height=25)


# Кнопка компиллировать файл
bt_run = tk.Button(text='Запустить сборку!', command=file_compilled)

# Lbel name file
name_your_file = tk.Label(text='Как вы назовете ваш проект?')
name_your_file.place(x=20, y=50, width=180)

###################################################################
# информация о каталоге, в котором будет сохранен проект:
# label, Enty, Button
save_patch_info = tk.Label(text='Проект будет сохранен по адресу:')
save_patch_info.place(x=20, y=175, height=25)
# Текстовое поле с адресом рабочего каталога
save_patch_file = tk.Entry()
save_patch_file.insert(0, os.getcwd() + '\\dist\\')
save_patch_file.configure(state='disable')
save_patch_file.place(x=20,  y=200, width=400, height=25)
# Кнопка Open - откорыть рабочий каталог
bt_open = tk.Button(text='open', command=bt_open_func)
bt_open.place(x=425, y=200)
####################################################################


if __name__ == '__main__':
    root.title("Упаковщик скриптов Python в .exe")
    root.geometry('600x400')
    root.resizable(0, 0)
    root.mainloop()
