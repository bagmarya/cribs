# скрипт формирует файл .xls или .xlsx из одного или нескольких
# файлов .csv в текущей папке

from pyexcel.cookbook import merge_all_to_a_book
import shutil, os, random, string, glob

# получаем список .csv файлов в директории
file_names = glob.glob("*.csv")
# генерируем случайное имя директории для временных файлов и создаем ее
name_of_tempdir = ''.join(random.choice(string.ascii_lowercase) for i in range(7))
os.mkdir(name_of_tempdir)
# поскольку максимальная дли на имени листа для xls - 31символ, обрезаем имена файлов
sheet_names = [name_of_tempdir + '/' + x[:27] + '.csv' if len(x)>27
               else name_of_tempdir + '/' + x + '.csv'
               for x in [x[:-4] for x in file_names] ]
# копируем файлы с подходящим именем во временную директорию
for file_name, sheet_name in zip(file_names, sheet_names):
    shutil.copy(file_name, sheet_name)
# файлы из временной директории конвертируем в листы книги и сохраняем файл
# формат сохраняемого файла .xls или .xlsx определяется по расширению в имени
merge_all_to_a_book(sheet_names, "output.xls")
# удаляем временные файлы
for f in sheet_names: os.remove(f)
os.rmdir(name_of_tempdir)