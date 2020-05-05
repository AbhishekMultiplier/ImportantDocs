from bs4 import BeautifulSoup
import re
count = 0
ap = 0
contents=[]
complete_content=[]
def bringTextFromHtml(content):
    temp = BeautifulSoup(content,"html.parser")
    temp1 = temp.find("html").text
    temp1 = re.sub(r"\xa0","",temp1)
    temp1 = re.sub(r"\xa0...","",temp1)
    temp1 = re.sub("[ ]+"," ",temp1)
    content = re.sub("[\n\t]","",temp1) 
    return content

def getString(string,shouldParse):
    content = ''
    soup = BeautifulSoup(string,"html.parser")
    for j in soup.stripped_strings:
        for i in j:
            # print(repr(i))
            content += i
    if shouldParse:
        content = bringTextFromHtml(content)
    return content

with open("./testing.html") as infile:
    for line in infile:
        count=count+1
        if count > 6:
            if count%6 in [1,2,3,4]:
                content = getString(line,False)
                print(content)
                contents.append(content)
                print(contents)
                # input()
            elif count%6==5:
                # print(line)
                contents.append(getString(line,True))
                complete_content.append(contents)
                print(contents)
                contents = []
                # input()
            else:
                continue
print(complete_content)
with open('test.txt','w',encoding='utf-8') as f:
    content = f.write(str(complete_content))
f.close()

for i in complete_content:
    # print(i[0])
    sql = "INSERT INTO "