import easyocr
import csv
from spire.pdf.common import *
from spire.pdf import *

def extraction(file):
    html = ''
    if (file.lower().endswith('.jpg') or file.lower().endswith('.jpeg') or file.lower().endswith('.png')):
        ocr(file)
        csv_path = 'test.csv'
        temp = csv_to_html(csv_path)
        html += temp

    elif (file.lower().endswith('.pdf')):
        fileNames = pdf_to_image(file)
        
        for image in fileNames:
            ocr(image)
            csv_path = 'test.csv'
            temp = csv_to_html(csv_path)
            html += temp
        
    return html

def csv_to_html(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        html = '<table border="1">'
        
        for row in csv_reader:
            html += '<tr>'
            for cell in row:
                html += '<td>' + cell + '</td>'
            html += '</tr>'
        
        html += '</table>'
        return html



def pdf_to_image(fileName):
    doc = PdfDocument()

    doc.LoadFromFile(fileName)

    # print(doc.Pages.Count)
    fileNames = []
    for i in range(doc.Pages.Count):
      result = "img{}.png"
      with doc.SaveAsImage(i) as imageS:
        imageS.Save(result.format(i))
        fileNames.append(result.format(i))
    
    return fileNames


def ocr(image):
    reader = easyocr.Reader(['en'])
    ocr_text = reader.readtext(image)
    text_map = {}

    for entry in ocr_text:
        coordinates, text, confidence = entry
        y_coordinate = int((coordinates[0][1]/25))
        x_coordinate = int((coordinates[0][0]))
        if y_coordinate not in text_map:
            text_map[y_coordinate] = []
        
        text_map[y_coordinate].append((text, x_coordinate))
    
    for y_coordinate, text_list in text_map.items():
        text_map[y_coordinate] = sorted(text_list, key=lambda item: item[1])
    csv_map = {}
    for y_coordinate, text_list in text_map.items():
        csv_map[y_coordinate] = [text[0] for text in text_list]

    # print(csv_map)
    csv_file_path = "test.csv"

    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        for y_coordinate, texts in csv_map.items():
            csv_writer.writerow(texts)
                
    return