from pywinauto import Application
from time import sleep

import pywinauto
app = Application()
app.start("notepad.exe")
app.UntitledNotepad.menu_select("Help->About")
sleep(1)
app.AboutNotepad.OK.click()
app.UntitledNotepad.Edit.type_keys("You have been hacked", with_spaces = True)
sleep(1)
app.kill()
print(dir(pywinauto))