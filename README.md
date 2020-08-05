
******************************************* HomeWork Tool **********************************************
Credits: Ankit Raj Mahapatra
One of my friend Ankit had already created the tool and is available on his GIT repo.
https://github.com/Ankit404butfound

I just tried a little from my side.

HomeWork Tool is a tool created using python for the purpose of converting the images containing
text into another image having the same text in hand-written text. This code is opensource and any
improvement is welcomed. 

I have inserted my own text into the tool.
If you want to have your own text build into the tool you can replace my images with your own images.

You will have to insert all the alphabets (Capital and Small) in it.
Dimensions for the Alphabets are fixed which you will have to resize.

___________________  SIZE OF ALPHABETS ___________________________
1) All capital letters must be of size: hor-50px, ver-66px
2) The letters ['b', 'd', 'f', 'h', 'k', 'l', 't', 'g', 'j', 'p', 'q', 'y'] should be of size: hor-30px, ver-66px
3) The letters ['a', 'c', 'e', 'i', 'm', 'n', 'o', 'r'] should be of size: hor-30px, ver-33px
-NOTE: You can resize the letters from default paint in windows.
![Paint Resize Image](/Images/Paint_Resize.jpg)
____________________________________________________________________________________

First of all you will have to install some libraries.
Here are the commands to install then through pip in cmd.

Open 'command prompt' and use these commands to install the modules

* `pip install pillow`
* `pip install PIL`
* `pip install pytesseract`
____________________________________________________________________________________
After installing the modules you will have to edit the script `Homework.py` and insert the location of your `pytesseract.exe` file in the current code.
So,

Go to `C:\Program Files\Tesseract-OCR` or whichever path you have installed pytesseract and edit the `Homework.py` script's *line no. 14* and paste your path for `tesseract.exe`.
As show in this image:
![Pytesseract Path](/Images/Tesseract_Path.jpg)

______________________________________________________________________________________
### THATS ALL ! YOU ARE READY TO GO
Run HomeworkGUI.py to run the tool and you will get an interface as shown below:
![GUI Interface](/Images/GUI_Tool.jpg)


I will include the code to improve the resizing of the letters on its own in later update.

____________________________________________________________________

Thank You !