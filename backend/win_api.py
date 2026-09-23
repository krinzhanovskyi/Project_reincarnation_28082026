import os
import winreg
import uiautomation as auto

def get_windows_desktop_path():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders")
        desktop_path, _ = winreg.QueryValueEx(key, "Desktop")
        winreg.CloseKey(key)
        return os.path.expandvars(desktop_path)
    except Exception:
        return os.path.join(os.path.expanduser("~"), "Desktop")

def get_desktop_folder_under_cursor(x, y):
    try:
        control = auto.ControlFromPoint(x, y)
        
        if control.ControlType != auto.ControlType.ListItemControl:
            return None

        top_window = control.GetTopLevelControl()
        if top_window and top_window.ClassName not in ('Progman', 'WorkerW'):
            return None

        item_name = control.Name
        if not item_name:
            return None
            
        desktop_path = get_windows_desktop_path()
        full_path = os.path.join(desktop_path, item_name)
        
        if os.path.isdir(full_path):
            return full_path
            
    except Exception:
        pass
        
    return None