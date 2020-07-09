#/usr/bin/env python3
import csv
import PyPDF2 # pip3 install PyPDF2
import re

with open('Exercise_Files/find_the_link.csv', encoding='utf-8') as f:
    csv_file = csv.reader(f)
    csv_data = list(csv_file)
    google_drive_url = ''
    
    # Try/Except block
    # for line in csv_data:
    #     for item in line:
    #         try:
    #             int(item)
    #         except Exception as e:
    #             google_drive_url += item

    # Knowing that URL is diagonal
    for line in enumerate(csv_data):
        google_drive_url += line[1][line[0]]

print(google_drive_url)

with open('Exercise_Files/Find_the_Phone_Number.pdf', 'rb') as f:
    pdf = PyPDF2.PdfFileReader(f)
    pattern = r'\d{3}.\d{3}.\d{4}'
    phone_number = ''

    for page in range(pdf.numPages):

        page_text = pdf.getPage(page).extractText()

        if re.search(pattern, page_text):
            print('Phone number found on page: ' + str(page + 1))
            phone_number = re.search(pattern, page_text).group(0)

print(phone_number)