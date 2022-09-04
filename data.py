# KorQuAD Dataset을 가지고 'context' key만 뽑아내어 pdf 파일로 변환

import json
import pdfkit

config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
file_path = './KorQuAD_Dataset'

with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    input_data = json.load(f, strict=False)["data"]

options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
}
count = 1
tmp_document = ""

# KorQuAD 1.0
for idx, article in enumerate(input_data):
    for paragraph in article['paragraphs']:
        context_raw = paragraph['context']
        tmp_document += "\n" + context_raw

        pdfkit.from_string(tmp_document, './Output/KorQuAD_v1.0_Output_{}.pdf'.format(count), options=options, configuration=config)
        print("successfully saved")
        tmp_document = ""

    count+=1
    if count%1001==0:
        break

# KorQuAD 2.0
for idx,para in enumerate(input_data):
    context_raw = para["context"]
    tmp_document += "\n" + context_raw

    if count%5==0:
        pdfkit.from_string(tmp_document, './Output/KorQuAD_v1.0_Output_{}.pdf'.format(count), options=options, configuration=config)
        print("successfully saved")
        tmp_document = ""
    count+=1
