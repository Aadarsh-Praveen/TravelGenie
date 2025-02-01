import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def send_email(to_email, subject, body):
    try:
        # Fetch email credentials from environment variables
        sender_email = os.getenv("EMAIL")
        sender_password = os.getenv("SMTP_PASSWORD")

        # Validate email credentials
        if not sender_email or not sender_password:
            raise ValueError("Email credentials are not set in the .env file.")

        # Email server configuration
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        # Set up the email message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = to_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Debug log
        print("Connecting to SMTP server...")

        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        print("Logging in to SMTP server...")
        server.login(sender_email, sender_password)

        print("Sending email...")
        server.sendmail(sender_email, to_email, message.as_string())
        server.quit()

        print("Email sent successfully!")
        return True
    except smtplib.SMTPAuthenticationError:
        print("SMTP Authentication Error: Check your email credentials.")
        return False
    except smtplib.SMTPConnectError:
        print("SMTP Connection Error: Unable to connect to the SMTP server.")
        return False
    except smtplib.SMTPRecipientsRefused:
        print(f"Recipient Address Rejected: {to_email}")
        return False
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return False
