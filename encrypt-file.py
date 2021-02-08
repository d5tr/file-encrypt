print ('''
 ______   _______ _________ _______ 
(  __  \ (  ____ \\__   __/(  ____ )
| (  \  )| (    \/   ) (   | (    )|
| |   ) || (____     | |   | (____)|
| |   | |(_____ \    | |   |     __)
| |   ) |      ) )   | |   | (\ (   
| (__/  )/\____) )   | |   | ) \ \__
(______/ \______/    )_(   |/   \__/
       # Thanks for use my tool #
''')
from PyPDF2 import PdfFileWriter , PdfFileReader
import py_compile
print ('''
[1] encrypt PYTHON file 
[2] encrypt PDF file
''')
dt = int(input('enter number :'))

if dt == 1:
    aa = input('enter name file :')

    ss =  py_compile.compile(aa)
    print("done !!")

elif dt == 2:

    def s_p (file, password):
        parser = PdfFileWriter()
        pdf = PdfFileReader(file)
        for page in range(pdf.numPages):
            parser.addPage(pdf.getPage(page))
        parser.encrypt(password)
        with open(f"encrypt_{file}", "wb") as f:
            parser.write(f)
            f.close()
        print(f"encrypted_{file} Created...")
    if __name__ == "__main__":
        file = input("enter file name :")
        password = input("enter passwor you went :")
        s_p(file, password)