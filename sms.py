import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sms_gateway = ""
email = ""
sender = "me"
smtp = ""
port = 0

user = input("host or guest?: ")

if user == "host":
    email = "techguy530@gmail.com"
    pas = input("Enter your password: ")
    sms_gateway = "8572614730@mymetropcs.com"
    sender = "me"
    smtp = "smtp.gmail.com"
    port = 587

else:
    email = input("Enter your email: ")
    pas = input("Enter your password: ")
    sms = input("\nCarriers:\nAT&T(a)\nSprint(s)\nT-Mobile(tm)\nVerizon(vz)\nBoost Mobile(bm)\nCricket(c)\nMetro PCS(m)\nTracfone(t)\nU.S. Cellular(us)\nVirgin Mobile(vm)\nEnter letter beside your carrier: ")
    cell = input("Enter your number: ")

    # determine sms carrier
    if sms == "a":
        sms_gateway = "%s@txt.att.net" % (cell)

    elif sms == "s":
        sms_gateway = "%s@messaging.sprintpcs.com" % (cell)

    elif sms == "tm":
        sms_gateway = "%s@tmomail.net" % (cell)

    elif sms == "vz":
        sms_gateway = "%s@vtext.com" % (cell)

    elif sms == "bm":
        sms_gateway = "%s@myboostmobile.com" % (cell)

    elif sms == "c":
        sms_gateway = "%s@sms.mycricket.com" % (cell)

    elif sms == "m":
        sms_gateway = "%s@mymetropcs.com" % (cell)

    elif sms == "t":
        sms_gateway = "%s@mmst5.tracfone.com" % (cell)

    elif sms == "us":
        sms_gateway = "%s@email.uscc.net" % (cell)

    elif sms == "vm":
        sms_gateway = "%s@vmobl.com" % (cell)  

    # The server we use to send emails in our case it will be gmail but every email provider has a different smtp 
    # and port is also provided by the email provider.
    s= email.partition("@")[2]

    if s == "gmail.com":
        smtp = "smtp.gmail.com" 
        port = 587
    
    elif s == "outlook.com":
        smtp = "smtp.live.com" 
        port = 587
    
    elif s == "office365.com":
        smtp = "smtp.office365.com" 
        port = 587

    elif s == "yahoo.com":
        smtp = "smtp.mail.yahoo.com" 
        port = 465
    
    elif s == "aol.com":
        smtp = "smtp.aol.com" 
        port = 587
    
    elif s == "hotmail.com":
        smtp = "smtp.live.com" 
        port = 465

    elif s == "mail.com":
        smtp = "smtp.mail.com" 
        port = 587

    else:
        print("Email server not supported!")

while True:
    # This will start our email server
    server = smtplib.SMTP(smtp, port)
    # Starting the server
    server.starttls()
    # Now we need to login
    server.login(email, pas)

    # Now we use the MIME module to structure our message.
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = sms_gateway
    # Make sure you add a new line in the subject
    sub = input("\nSubject: ")
    text = input("Text: ")
    subj =  "%s\n" % (sub)
    msg['Subject'] = subj

    # Make sure you also add new lines to your body
    body = "\n\n%s\n" % (text)
    # and then attach that body furthermore you can also send html content.
    msg.attach(MIMEText(body, 'plain'))

    sms = msg.as_string()

    print("Sending text...")
    server.sendmail(email, sms_gateway, sms)
    print("Sent.")
    print("\n******************************************************************************************************************************************************\n")

# lastly quit the server
server.quit()
print("\nQuitting.")