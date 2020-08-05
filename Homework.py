from PIL import Image
import pytesseract
import os.path

class Homework:

    def __init__(self):
        pass

    def toText(self, img):

        script_dir = os.path.dirname(os.path.abspath(__file__))
        folder_path = os.path.join(script_dir, "Tesseract-OCR\\tesseract.exe")
        pytesseract.pytesseract.tesseract_cmd = folder_path
        result = pytesseract.image_to_string(img)
        return result

    def doHomework(self, img, location):

        script_dir = os.path.dirname(os.path.abspath(__file__))
        folder_path = os.path.join(script_dir, "Letters\\")
        special = """¬`!£$%^&*()-_+={["]}:;'@?/\\<,.>|"""
        upp = ['b', 'd', 'f', 'h', 'k', 'l', 't']
        # ITT = ImgToTextApi()

        a = 70
        b = 100

        paper = Image.open(folder_path + "Background.png")
        paper_width, paper_height = paper.size
        string = self.toText(img)

        # string = ITT.ocr_space_file(img_loc)
        # string = string[187:]
        # string -= string[460:]
        # print(string)

        for each in string:
            
            #............................. Check For New Line .................................
            if (a+70) > paper_width:
                a = 70
                b += 100

            if each not in special:
                if each.isupper():
                    image_path = folder_path + each + ".png"
                elif each.islower():
                    image_path = folder_path + each + each + ".png"
                elif each.isspace():
                    image_path = folder_path + "space.png"
            else:
                image_path = None

            if image_path != None:
                letter = Image.open(image_path)
                x,y = letter.size

                if each.isupper():
                    b -= 33
                elif each in upp:
                    b -= 33

                paper.paste(letter, (a,b,a+x,b+y))
                if each.isupper():
                    b += 33
                elif each in upp:
                    b += 33
                a += x
        location += "\\HomeworkDone.png"
        paper.save(location)
        saved = Image.open(location)
        saved.show()