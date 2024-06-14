import multiprocessing
from multiprocessing import Process
from typing import Optional
from ctypes import c_bool
import time
import keyboard
import pyperclip 
import win32clipboard
import base64

def getText():
    win32clipboard.OpenClipboard()
    text = ''
    try:
        text = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)     
    except Exception as e:
        try:
            data = win32clipboard.GetClipboardData(win32clipboard.CF_HDROP)
            path = data[0]
            with open(path, 'rb') as file:
                file_content = file.read()
                file_base64 = base64.b64encode(file_content)
                text = file_base64.decode('utf-8')
        except Exception as e:
            print(e)
    win32clipboard.CloseClipboard()
    return text

def target(start_flag: multiprocessing.Value):
    text = getText()
    # print(text)  
    keyboard.write(text.replace('\t', '    '))
    start_flag.value = False


if __name__ == '__main__':

    start_flag = multiprocessing.Value(c_bool, False)
    exec_proc: Optional[Process] = None

    def start():
        global exec_proc
        if start_flag.value == False:
            print('start')
            start_flag.value = True
            exec_proc = Process(target=target, args=(start_flag,))
            exec_proc.start()

    def stop():
        global exec_proc
        if start_flag.value == True:
            print('end')
            if exec_proc:
                exec_proc.terminate()
                start_flag.value = False
                exec_proc = None

    keyboard.add_hotkey('ctrl+alt+[', start)
    keyboard.add_hotkey('ctrl+alt+]', stop)
    while True:
        time.sleep(0.01)
        