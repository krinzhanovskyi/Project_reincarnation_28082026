import os
import winreg
import uiautomation as auto

def get_windows_desktop_path():
    # Надежный способ найти Рабочий стол (учитывает, если он сдвинут в OneDrive)
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders")
        desktop_path, _ = winreg.QueryValueEx(key, "Desktop")
        winreg.CloseKey(key)
        # Раскрываем переменные вроде %USERPROFILE%
        return os.path.expandvars(desktop_path)
    except Exception:
        # Резервный вариант, если реестр недоступен
        return os.path.join(os.path.expanduser("~"), "Desktop")

def get_desktop_folder_under_cursor(x, y):
    try:
        # 1. Получаем элемент интерфейса под мышью
        control = auto.ControlFromPoint(x, y)
        
        # 2. Проверяем, что это элемент списка (так система видит иконки)
        if control.ControlType != auto.ControlType.ListItemControl:
            return None
            
        # 3. Проверяем, что мы именно на рабочем столе 
        # (Класс окна рабочего стола в Windows - Progman или WorkerW)
        top_window = control.GetTopLevelControl()
        if top_window and top_window.ClassName not in ('Progman', 'WorkerW'):
            return None

        # Получаем имя иконки
        item_name = control.Name
        if not item_name:
            return None
            
        # 4. Собираем полный путь и проверяем, папка ли это
        desktop_path = get_windows_desktop_path()
        full_path = os.path.join(desktop_path, item_name)
        
        if os.path.isdir(full_path):
            return full_path
            
    except Exception:
        # Игнорируем ошибки (например, если курсор над системным окном с правами админа)
        pass
        
    return None