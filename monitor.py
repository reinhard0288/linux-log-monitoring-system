import smtplib
from email.message import EmailMessage
def send_alert():
    sender_email = "kingreinhard8877@gmail.com"
    app_password = "enbbzdongjtpzvyp"
    receiver_email = "siripakasaikumar02@gmail.com"
    msg = EmailMessage()
    msg["Subject"] = "Security Alert: Suspicious Login Activity"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content("Alert! Multiple failed login attempts detcted on the server.")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email,app_password)
        smtp.send_message(msg)
    print("REAL EMAIL ALERT SENT TO ADMIN")
print("Linux Server LOG MONITORING STARTED")
log_file = "sample_log.txt"
with open (log_file,"r") as file:
    lines = file.readlines()
failed_attempts = 0
for line in lines:
    if "Failed password" in line:
        failed_attempts += 1
    print(f"Total Failed Login Attempts: {failed_attempts}")
    if failed_attempts > 2:
        print("ALERT: Suspicious Activity Detected!")
        send_alert()
    with open("report.txt", "w") as report:
        report.write(f"Failed Login Attempts: {failed_attempts}\n")
        if failed_attempts > 2:
            report.write("ALERT: Suspicious Activity Detected!\n")
    print("Report saved in report.txt")