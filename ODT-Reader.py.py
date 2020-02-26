import sys
import os
from bs4 import BeautifulSoup
if sys.version_info >= (3, 6):
    import zipfile
else:
    import zipfile36 as zipfile

        # reading the content of the file in respective xml formats
        # print(myfile.read(s.orig_filename))
        # input()
myfile = zipfile.ZipFile("./A C SUBRAMANIAM 353970 74608 SWAROOP.odt")
fileContent=''
for s in myfile.infolist():
    if s.orig_filename.split(".")[-1] == "xml" and s.orig_filename in ['content.xml','styles.xml']:
        print(s.orig_filename)
        # print(myfile.read(s.orig_filename))
        source = BeautifulSoup(myfile.read(s.orig_filename),'xml')
        if s.orig_filename == "content.xml":
            texts = source.find_all("text")
        else:
            texts = source.find_all("text:p")
            texts += source.find_all("text:span")
        for text in texts:
            print(text.text)
            fileContent +=text.text


print(fileContent)
