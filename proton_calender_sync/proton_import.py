import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv

def send_ics_to_proton(ics_file, proton_email, proton_import_email):
    """
    Send the .ics file to Proton Calender via email
    """
    try:
        # Load env variables
        load_dotenv()
        email_password = os.getenv("PROTON_EMAIL_PASSWORD")
        msg = MIMEMultipart()
        msg["From"] = proton_email
        msg["To"] = proton_import_email
        msg["Subject"] = "Calender Import"

        # attach .ics file
        with open(ics_file, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename={os.path.basename(ics_file)}"
            )
            msg.attach(part)
        
        with smtplib.SMTP("mail.proton.me", 587) as server:
            server.starttls()
            server.login(proton_email, email_password)
            server.send_message(msg)
        print(f"Calender sent to {proton_import_email}")
    except Exception as e:
        print(f"Error sending email: {e}")
        