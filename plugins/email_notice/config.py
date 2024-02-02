from magi.managers import SettingManager


@SettingManager.register
class Config:
    sender_email = "your_email@gmail.com"
    receiver_email = "recipient_email@example.com"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "your_email@gmail.com"
    smtp_password = "your_email_password"
