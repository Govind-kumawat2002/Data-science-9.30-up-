import smtplib
 
server = smtplib.SMTP(host="smtp.gmail.com",port=587) #0.0.0.0 local host 
server.starttls() ### 0 to 656508
receiver_email= input("Enter your Email:- ")
sender_email  = "laveshgujar71@gmail.com"
sender_password = "pobk umvw xzow qfgc"
server.login(sender_email,sender_password)
Subject = input("what is your problem 🤔")
Body = input("Bhai toda detail me btaoo ")
message = f"subject:  {Subject}\n\n{Body}"
server.sendmail(sender_email,receiver_email,message)
print("aapki email send ho gyi 👍👍👍👍 ")
server.quit()
# except Exception:

    # print("bahi eseke ander char mt dal ")
    # print("vaps try kro bhaii ")
