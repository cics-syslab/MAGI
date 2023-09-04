import smtplib
from . import Config


def send_email(subject: str = "", email_body: str = ""):
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    message = MIMEMultipart()
    message["From"] = Config.sender_email
    message["To"] = Config.receiver_email

    message["Subject"] = "Email Notification" if subject is None or len(subject)==0 else subject

    email_body = "This is a sample email notification from Python."
    message.attach(MIMEText(email_body, "plain"))

    # collect student information



    try:
        server = smtplib.SMTP(Config.smtp_server, Config.smtp_port)
        server.starttls()
        server.login(Config.smtp_username, Config.smtp_password)

        # Send the email
        server.sendmail(Config.sender_email, Config.receiver_email, message.as_string())
        print("Email sent successfully!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        # Close the SMTP server connection
        server.quit()
