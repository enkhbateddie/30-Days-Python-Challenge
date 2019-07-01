import datetime
import csv
import shutil
from tempfile import NamedTemporaryFile

def read_data(user_id=None, email=None):
    filename = "data.csv"
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
            return "User id {user_id} not found".format(user_id=user_id)
        if unknown_email is not None:
            return "Email {email} not found".format(email=email)
    return None

def get_length(file_path):
    with open("data.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        return len(reader_list)

def append_data(file_path, name, email, amount, sent):
    fieldnames = ['id', 'name', 'email', 'amount', 'sent', 'date']
    #the number of rows?
    next_id = get_length(file_path)
    with open(file_path, "a", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({
                "id": next_id,
                "name": name,
                "email": email,
                "sent": False,
                "amount": amount,
                "date": datetime.datetime.now()
            })

append_data("data.csv", "Enkhbat", "chimgee.gal@gmail.com", 123.22, False)

def edit_data(edit_id=None, email=None, amount=None, sent=None):
    filename = "data.csv"
    temp_file = NamedTemporaryFile(delete = False, newline='', mode='w')
    with open(filename, "r") as csvfile, temp_file:
        reader = csv.DictReader(csvfile)
        fieldnames = ['id', 'name', 'email', 'amount', 'sent', 'date']
        writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            if edit_id is not None:
                if int(row['id']) == int(edit_id):
                    row['amount'] = amount
                    row['sent'] = sent
            elif email is not None and edit_id is None:
                if row['email'] == str(email):
                    row['amount'] = amount
                    row['sent'] = sent
            else:
                pass
            writer.writerow(row)
        csvfile.close()
        temp_file.close()
        shutil.move(temp_file.name, filename)
        return True
    return False

#edit_data(email='hello@teamcfe.com', amount=99.99, sent='')

def delete_data(delete_id=None, email=None, amount=None, sent=None):
    filename = "data.csv"
    temp_file = NamedTemporaryFile(delete = False, newline='', mode='w')
    with open(filename, "r") as csvfile, temp_file:
        reader = csv.DictReader(csvfile)
        fieldnames = ['id', 'name', 'email', 'amount', 'sent', 'date']
        writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            if delete_id is not None:
                if int(row['id']) == int(delete_id):
                    continue
            else:
                pass
            writer.writerow(row)
        csvfile.close()
        temp_file.close()
        shutil.move(temp_file.name, filename)
        return True
    return False