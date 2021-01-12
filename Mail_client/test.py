import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

port = 587
login = "pythonsmtptesting911@gmail.com"
password = "python123$"

subject = "Test"
sender_email = "pythonsmtptesting911@gmail.com"
receiver_email = "anton.vosh@yandex.ru"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Add body to email
body = "This is an example of email with attachment"
message.attach(MIMEText(body, "plain"))

filename = "image.png"
# Open PDF file in binary mode

# We assume that the file is in the directory where you run your Python script from
with open(filename, "rb") as attachment:
    # The content type "application/octet-stream" means that a MIME attachment is a binary file
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode to base64
encoders.encode_base64(part)

# Add header
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to your message and convert it to string
message.attach(part)
text = message.as_string()

# send your email
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login(login, password)
s.sendmail(sender_email, receiver_email, text)

print('Sent')
