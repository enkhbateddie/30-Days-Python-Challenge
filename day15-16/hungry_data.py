import datetime
import os
import csv
import shutil
from tempfile import NamedTemporaryFile

def get_length(file_path):
    with open("data.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        return len(reader_list)

def append_data(file_path, name, email, amount):
    fieldnames = ['id', 'name', 'email', 'amount', 'sent', 'date']
    #the number of rows?
    next_id = get_length(file_path)
    with open(file_path, "a", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({
                "id": next_id,
                "name": name,
                "email": email,
                "sent": "",
                "amount": amount,
                "date": datetime.datetime.now()
            })

# append_data("data.csv", "Justin", "hello@teamcfe.com", 123.22)

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

edit_data(email='hello@teamcfe.com', amount=123.32, sent='')