#!/usr/bin/env python

import os
import docx # python -m pip install python-docx
import sys
#import textract

root = sys.argv[1]

student_files_doc = [doc for doc in os.listdir(root) if doc.endswith('.docx') or doc.endswith('.DOCX')]


for doc_file in student_files_doc:

    #if doc_file.endswith():
    #    text = textract.process('example.doc')
    #    print(text.decode('utf-8'))

    # Open the .docx file
    print('Reading: ' + doc_file)
    doc = docx.Document(f'{root}/{doc_file}')

    text = ''

    for para in doc.paragraphs:
        text += para.text

    with open(f'{root}/{doc_file}.txt', 'w', encoding='utf-8') as file:
        file.write(text)