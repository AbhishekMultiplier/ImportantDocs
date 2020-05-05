from bs4 import BeautifulSoup
import re,csv

file_output=open("aaabucket1.csv","w",newline="")
# field names 
fields = ['patient-id', 'note-content', 'note-type', 'event-date'] 
csvwriter = csv.writer(file_output) 
csvwriter.writerow(fields)


file_input = open("./aaabucket1.html","r")
file_content = file_input.read()
file_input.close()

file_soup = BeautifulSoup(file_content,"html.parser")
tds = file_soup.find_all("td")
contents=[]
complete_content=[]

def purifyText(str):
    return re.sub("[\n\t\s]","",str)

for td in range(0,len(tds)):
    # print(td)
    # print(tds[td].text)
    if(td !=0 and td%4==0):
        complete_content.append(contents)
        # print(contents)
        # input()
        # csvwriter.writerow(contents)
        contents=[]
        # print(complete_content)
    if(td % 4 ==1):
        # print(tds[td])
        soup = BeautifulSoup(tds[td].text,"html.parser")
        content = ""
        for i in soup.stripped_strings:
            for j in i:
                content = content + purifyText(j)
        contents.append(content)
        # print(contents)
            # input()
    else:
        contents.append(purifyText(tds[td].text))
        # print(contents)
    # print(contents)
print(complete_content)
csvwriter.writerows(complete_content)
file_output.close()
    # input()