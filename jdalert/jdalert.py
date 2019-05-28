#Import requests for the HTTP client lib
import requests
import json
import sys
#Convert the return json result to html
from json2html import *
#Import related parameters
import smtplib
from email import encoders 
from email.header import Header 
from email.mime.text import MIMEText 
from email.utils import parseaddr 
from email.utils import formataddr 

def format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, "utf-8").encode(), addr))

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

#Get the requested data by requests and api concact value
url = 'http://p.3.cn/prices/mgets?skuIds=' + ",".join(sys.argv[1:]) + '&type=1'
print(url)
re = requests.get(url)
jd = json.loads(re.text)
print(jd)
html = json2html.convert(json = jd)
print(html)

#setup the email sender, stmp_server, password and receiver
from_email = "xw6188@126.com"
from_email_pwd = "bentest2019"
to_email = "xw6188@163.com"
smtp_server = "smtp.126.com"

#format the message
msg = MIMEText(html, "html", "utf-8")
msg["From"] = format_addr("%s" %(from_email))
msg["To"] = format_addr("%s" %(to_email))
msg["Subject"] = Header("Price List JD for SKU id" + ",".join(sys.argv[1:]), "utf-8").encode()

#logon the server and sent email
try:
	server = smtplib.SMTP(smtp_server, 25)
	server.set_debuglevel(1)
	server.login(from_email, from_email_pwd)
	server.sendmail(from_email, [to_email], msg.as_string())
	server.quit()
	print ('Price List sent successfully')
except smtplib.SMTPException:
	print ('Error sent email')
	