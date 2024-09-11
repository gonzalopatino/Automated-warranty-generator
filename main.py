from flask import Flask, render_template, request, send_file, session, redirect, url_for
from docx import Document
from datetime import datetime, timedelta
from reportlab.pdfgen import canvas

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

@app.route('/', methods=['GET', 'POST'])
def hello():
    print("Hello")
    if request.method == 'POST':
        date = request.form['date']
        order_number = request.form['order_number']
        serial_numbers = request.form['serial_numbers']
        print(f"Hello first time Date is {date}")

        # Save values to session
        session['date'] = date
        session['order_number'] = order_number
        session['serial_numbers'] = serial_numbers

        save_to_file(f"Date: {date}, Order Number: {order_number}, Serial Numbers: {serial_numbers}")


    return render_template('index.html')

@app.route('/process_word', methods=['GET', 'POST'])
def process_word():
    if request.method == 'POST':
        date = request.form['date']
        order_number = request.form['order_number']
        serial_numbers = request.form['serial_numbers']
        product = request.form['product']
        warranty = request.form['Warranty']


    print(f"Download first time Date is {date}, order number is {order_number}, serial number are {serial_numbers}, warranty is {warranty}")

    generate_report(date, order_number, serial_numbers, product, warranty)
    # Redirect to the download route after generating the report
    print("entered download_word")
    # Specify the path to your Word file
    word_file_path = 'modified_document.docx'

    # Set the filename that the user will see
    filename = f"SO{order_number}|{date}|Report.docx"

    # Send the file to the user's browser for download
    print("about to download")
    return send_file(word_file_path, as_attachment=True, download_name=filename)

def save_to_file(data):
    file_path = 'C:\\Users\\gonzalo.patino\\user_input.txt'
    print(f"From hello route, session data is {data}")
    with open(file_path, 'a') as file:
        file.write(data + '\n')

def replace_placeholder(doc, placeholder, replacement):
    for paragraph in doc.paragraphs:
        if placeholder in paragraph.text:
            paragraph.text = paragraph.text.replace(placeholder, replacement)

def generate_report(dateParam, salesOrderNumParam, serialNumParams, product, warranty):

    print(f"params are {dateParam}, sales order param {salesOrderNumParam}, serial number {serialNumParams}")
    doc = Document("static/WarrantyStatic.docx")
    if product == 'C7400-ER-C':
        ProductPartNumber = '07-740-1100'
    elif product == 'C7200-C':
        ProductPartNumber = '07-720-0100'
    elif product == 'C7400 C':
        ProductPartNumber = '07-740-0100'
    else:
        ProductPartNumber = 'Could not detect part number'

    warrantyNumberInYears = int(warranty)

    #Calculate End date
    newDateParam = add_years_to_date(dateParam, warrantyNumberInYears)
    print(f'The new date param is: {newDateParam} from {dateParam}') #For debugging purposes

    #Calculate warranty period
    if warrantyNumberInYears == 2:
        warrantyPeriod = 'Standard- 2 years'
    elif warrantyNumberInYears == 4:
        warrantyPeriod = 'Extended- 4 years'
    else:
        warrantyPeriod = 'Error in processing warranty period'

    replace_placeholder(doc, "{dateToday}", dateParam)
    replace_placeholder(doc, "{salesOrderID}", salesOrderNumParam)
    replace_placeholder(doc, "{Product}", product)
    replace_placeholder(doc, "{ProductPartNumber}", ProductPartNumber)
    replace_placeholder(doc, "{SerialNumberInput}", serialNumParams)
    replace_placeholder(doc, "{SerialNumberInput}", serialNumParams)
    replace_placeholder(doc, "{WarrantyOutput}", warrantyPeriod) #Warranty period
    replace_placeholder(doc, "{dateWarrantyOutput}", newDateParam)



    doc.save("modified_document.docx")
    print("saved generated report")

    return doc


def add_years_to_date(input_date, years_to_add):
    # Convert the input date string to a datetime object
    date_object = datetime.strptime(input_date, "%m/%d/%Y")

    # Add the specified number of years to the date
    result_date = date_object + timedelta(days=365 * years_to_add)

    # Format the result date as a string in the original format
    result_date_str = result_date.strftime("%m/%d/%Y")

    return result_date_str



if __name__ == '__main__':
    app.run(host='CDXWS-GONZALO', port=2023, debug=True)
