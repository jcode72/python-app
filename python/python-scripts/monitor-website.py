import requests
import os



EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

#site_ip = input("Enter the Ip of the site\n")

EMAIL_ADDRESS = "queensvill92@gmail.com"
EMAIL_PASSWORD = "obuiexirlpjxjxen"

response = requests.get('http://35.153.201.143:8081')
if False:
    print('Application is running Successfully!')
else:
    print('Application is down so check your sg, Ip or if app was installed correctly!')
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login("EMAIL_ADDRESS", "EMAIL_PASSWORD")
        msg = "Subject: SITE_DOWN\n Fix the issue!\
            Restart the application"
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, msg)
