import csv
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib
import shutil
from tempfile import NamedTemporaryFile

from utils.templates import get_template, render_context

# file_item_path = os.path.join(os.getcwd(), "data.csv")
file_item_path = os.path.join(os.path.dirname(__file__), "data.csv")

host = "smtp.gmail.com"
port = 587
username = "chimgee.gal@gmail.com"
password = ""
from_email = username
to_list = ["chimgee.gal@gmail.com"]

# try:
#     email_conn = smtplib.SMTP(host, port)
#     email_conn.ehlo()
#     email_conn.starttls()
#     email_conn.login(username, password)
#     the_msg = MIMEMultipart("alternative")
#     the_msg['Subject'] = "Billing Update!"
#     the_msg["From"] = from_email
#     the_msg["To"]  = user_email
#     part_1 = MIMEText(user_message, 'plain')
#     the_msg.attach(part_1)
#     email_conn.sendmail(from_email, [user_email], the_msg.as_string())
#     email_conn.quit()
# except smtplib.SMTPException:
#     print("error sending message")

class UserManager():
    def render_message(self,user_data):
        file_ = 'templates/email_message.txt'
        file_html = 'templates/email_message.html'
        template = get_template(file_)
        template_html = get_template(file_html)
        if isinstance(user_data, dict):
            context = user_data
            plain_ = render_context(template, context)
            html_ = render_context(template_html, context)
            return (plain_, html_)
        return (None, None)
    def email_sent(self, user_id=None, email=None, sent=None):
        filename = file_item_path
        temp_file = NamedTemporaryFile(delete = False, newline='', mode='w')
        with open(filename, "r") as csvfile, temp_file:
            reader = csv.DictReader(csvfile)
            fieldnames = ['id', 'name', 'email', 'amount', 'sent', 'date']
            writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                if user_id is not None:
                    if int(row['id']) == int(user_id):
                        row['sent'] = sent
                elif email is not None and user_id is None:
                    if row['email'] == str(email):
                        row['sent'] = sent
                else:
                    pass
                writer.writerow(row)
            csvfile.close()
            temp_file.close()
            shutil.move(temp_file.name, filename)
            return True
        return False
    def get_sent_users(self):
        filename = file_item_path
        with open(filename, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            unknown_user_sent = None
            for row in reader:
                if bool(row["sent"]) == True:
                    return row
                else:
                    unknown_user_sent = "Command Failed"
            if unknown_user_sent is not None:
                print("User id {user_id} not found".format(user_id=user_id))
        return None
    def message_user(self, user_id=None, email=None,sent=True, subject="Billing Update!"):
        user = self.get_user_data(user_id=user_id, email=email)
        if user:
            plain_, html_ = self.render_message(user)
            print(plain_, html_)
            user_email = user.get("email", "chimgee.gal@gmail.com")
            to_list.append(user_email)
            try:
                email_conn = smtplib.SMTP(host, port)
                email_conn.ehlo()
                email_conn.starttls()
                email_conn.login(username, password)
                the_msg = MIMEMultipart("alternative")
                the_msg['Subject'] = subject
                the_msg["From"] = from_email
                the_msg["To"]  = user_email
                part_1 = MIMEText(plain_, 'plain')
                part_2 = MIMEText(html_, "html")
                the_msg.attach(part_1)
                the_msg.attach(part_2)
                email_conn.sendmail(from_email, to_list, the_msg.as_string())
                email_conn.quit()
            except smtplib.SMTPException:
                print("error sending message")
        self.email_sent(user_id=user_id, email=email, sent=sent)
        return self.get_sent_users()

    def get_user_data(self, user_id=None, email=None):
        filename = file_item_path
        with open(filename, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            item = []
            unknown_user_id = None
            unknown_email = None
            for row in reader:
                if user_id is not None:
                    if int(user_id) == int(row["id"]):
                        return row
                    else:
                        unknown_user_id = user_id
                if email is not None:
                    if email == row.get("email"):
                        return row
                    else:
                        unknown_email = email
            if unknown_user_id is not None:
                print("User id {user_id} not found".format(user_id=user_id))
            if unknown_email is not None:
                print("Email {email} not found".format(email=email))
        return None