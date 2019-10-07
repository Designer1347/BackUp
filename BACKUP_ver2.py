import os
import time

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['C:\\Documents', 'C:\Windows','C:\\Users']
# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.

# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'D:\\Backup' # Подставьте тот путь, который вы будете использовать.

# 3. Файлы помещаются в zip-архив.
# 4. Именем для zip-архива служит текущая дата и время.
today = target_dir + os.sep + time.strftime('%Y%m%d')

# Текущее время служит именем zip-архива
now = time.strftime('%H%M%S')

# Запрашиваем комментарий от пользователя
comment = input('Введите комментарий ')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' +\
        comment.replace(' ','_') + '.zip'
print('Комментарий успешно создан!',today)

# Создаём каталог, если его ещё нет
if not os.path.exists(today):
    os.mkdir(today) # Создание каталога
print('Каталог успешно создан!')

# Имя zip-файла
target = today + os.sep + now +'.zip'

# 5. Используем команду "zip" для помещения файлов в zip-архив
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

# Запускаем создание резервной копии
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание не удалось!!!')