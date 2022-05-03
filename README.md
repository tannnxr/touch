# touch
Adds the 'touch' command to Windows via Python


You will have to convert this file into an executable if you would like to run this script.

## Step 1
Converting the file into an executable.

**Make sure you are in the directory in which touch.py is contained!**

First install PyInstaller
`pip install pyinstaller`

Next run the command to generate an executable via PyInstaller
`pyinstaller --onefile touch.py`

## Step 2
Adding the executable file to path.

First go into the `/dist/` directory, this contains your Python executable.

You should see `touch.exe` inside.

Now open your file explorer and navigate to your `/Documents/` directory (or any directory you prefer).

I created a "python scripts" folder in my `/Documents/` directory.

Open the folder, and move the `touch.exe` file there.

Copy the **ABSOLUTE PATH** of the folder. Ex: `C:\Users\[user]\Documents\python scripts`

Now hit the windows button on your keyboard, and type in "path" and hit enter,
navigate to the bottom of the GUI and click on "Enviroment Variables"

Edit your `PATH` variable in users, and create a new path, put the path you copied into there.


Now if you restart your command line you should be able to run `touch [filename].[ext]` and it should create a new file.
