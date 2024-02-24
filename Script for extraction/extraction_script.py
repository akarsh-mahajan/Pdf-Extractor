import easyocr
import re
import csv

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

    print(csv_map)
    csv_file_path = "test.csv"

    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        for y_coordinate, texts in csv_map.items():
            csv_writer.writerow(texts)
                
    return

image_path = 'sample2.jpg'
ocr(image_path)
