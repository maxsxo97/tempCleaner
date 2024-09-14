import os
import shutil
temp_path = r"C:\Users\1\AppData\Local\Temp"
content = os.listdir(temp_path)
for item in content:
    full_name = os.path.join(temp_path, item)
    try:
        if os.path.isdir(full_name):
            shutil.rmtree(full_name)
        else:
            os.remove(full_name)
    except:
        print("не удалось удалить файл", full_name)
