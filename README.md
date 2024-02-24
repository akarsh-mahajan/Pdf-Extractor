# Invoice Data Extraction Project Documentation
## 1. Introduction

### 1.1 Project Overview
Project aims to extract data from invoices and store them into a csv file, invoices can be provided in .pdf, .jpg, .png, .jpeg format

### 1.2 Technologies Used
For the purpose of this project I have used Django, HTML, CSS to create the App's frontend and backend
For performing ocr I have used **'easyocr'** library.
Data Extraction will take some time, but its speed can be increase by enabling GPU
Also our app is not designed to work for non-invoice files and handwritten invoices.

### 1.3 Instruction to Use
*Ensure that you have python version 3.10 installed*

1. Open any IDE of your choice, import the project code from github repository.
2. Create a virtual environment using command 'pipenv shell'
3. Install all dependencies using command 'pip install -r requirements.txt'
4. To run the web app run command 'python manage.py runserver'
