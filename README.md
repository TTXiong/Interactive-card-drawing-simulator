# Interactive-card-drawing-simulator
A interactive card drawing simulator, which contains GUI interface.

## 1.Use Qt designer to build a UI interface
### Install Qt Designer
Download Qt designer from https://build-system.fman.io/qt-designer-download

### Create a UI interface
https://www.cnblogs.com/linyfeng/p/11223707.html

Remember to change the objectName

### Transfer file.ui to file.py
Using 'pyuic5 -o fileName.py fileName.ui'

### Connect functions with buttons
Make sure the button names appeared in the code are the same as your defined in file.ui

### Pyinstaller to package .py to .exe
https://www.cnblogs.com/linyfeng/p/8207149.html

Open cmd, enter 'pip install pyinstaller', then Using 'where pyinstaller' to check whether successfully installed

Then use 'pyinstaller.exe -F call_login.py -w' to pack. **Do not pack .ipynb, it will fail**

After pack, the .exe will be stored in dict file
