from bs4 import BeautifulSoup
import os
import datetime
import getpass, os, imaplib, email
import re
import mysql.connector


def filterString(str):
    str= str.strip()
    return re.sub("[\n\r' ]*","",str)
# method to get the content from a given string
def getContentFromString(mailbody):
    # msg_key = mailbody.values()[mailbody.keys().index("Message-ID")]
    # print(msg_key)
    name=''
    email=''
    phone=''
    message=''
    url=''
    emailDate=''
    emailTo=''
    emailFrom=''
    tempDate = mailbody.values()[mailbody.keys().index("Date")]
    emailDate = datetime.datetime.strptime(tempDate, "%a, %d %b %Y %H:%M:%S %z").strftime('%Y-%m-%d %H:%M:%S')
    
    emailTo = mailbody.values()[mailbody.keys().index("To")]
    # print(emailTo)
    emailFrom = mailbody.values()[mailbody.keys().index("From")]
    # print(emailFrom)
    splitstring = mailbody.keys()[-1]+": "+mailbody.values()[-1]
    content_str= str(mailbody).split(splitstring)[1]
    content_html = BeautifulSoup(content_str,"html.parser")
    content = (content_html.findAll("td"))
    # print(content_html)
    for i in range(0,len(content)):
        content_value = content[i].text
        if(content_value == "Name:"):
            name = content[i+1].text
        elif(content_value == "Email:"):
            email = content[i+1].text
        elif(content_value == "Phone:"):
            phone = content[i+1].text
        elif(content_value == "Message:"):    
            message = content[i+1].text
        elif(content_value == "URL:"):
            url = content[i+1].text;
    # print(name)
    # print(email)
    # print(phone)
    # print(message)
    # print(url)
    sql = (
        "INSERT INTO leads1 (name, email, phone, message, url,emaildate,emailto,emailfrom) VALUES ('"
        + filterString(name)
        + "','"
        + filterString(email)
        + "','"
        + filterString(phone)
        + "','"
        + filterString(message)
        + "','"
        + filterString(url)
        + "','"
        + filterString(str(emailDate))
        + "','"
        + filterString(emailTo)
        + "','"
        + filterString(emailFrom)
        + "')"
    )
    print(sql)
    try:
        if(url!=''):
            sqlcursor.execute(sql)
            mydb.commit()
        else:
            print(content)
            with open("emptyurls2.csv","a+")as f:
                f.write(str(content_str)+",\n")
            f.close()
            # exit()
    except Exception as e:
        print(e)
        exit()

# getting messages from the mail
def getMessages():
    typ, messages = conn.search(None, '(FROM "MHB" SUBJECT "%s")' % subject)
    for i in messages[0].split():
        type1, message = conn.fetch(i, "RFC822")
        m = email.message_from_bytes(message[0][1])
        try:
            status = getContentFromString(m)
            # input()
        except Exception as e:
            print("in excepion")
            print(e)


# ===================================================
# creating the mysql db connetion to record contents of mails
mydb = mysql.connector.connect(
    host="localhost", user="root", passwd="", database="manipalgmail"
)
sqlcursor = mydb.cursor(dictionary=True)
# ======================================================
# credentials of  server
servername = "imap.gmail.com"
usernm = "mounika@multipliersolutions.in"
passwd = "9030146678"
subject = "Manipal"
# establishing connection using imap
conn = imaplib.IMAP4_SSL(servername)
conn.login(usernm, passwd)
conn.select("Inbox")
getMessages()
