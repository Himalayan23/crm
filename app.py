from flask import Flask, render_template, request, send_file
import pdfkit
import os
config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")


app = Flask(__name__)

# Route to display the form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle PDF generation
@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    # Get form data
    package_title = request.form['package_title']
    itinerary = request.form['itinerary']
    hotel = request.form['hotel']
    vehicle = request.form['vehicle']

    # Render HTML template with form data
    rendered = render_template(
        'template.html', 
        package_title=package_title, 
        itinerary=itinerary, 
        hotel=hotel, 
        vehicle=vehicle
    )

    # Save rendered HTML to file
    html_path = os.path.join('temp', 'package.html')
    pdf_path = os.path.join('temp', 'package.pdf')
    with open(html_path, 'w') as f:
        f.write(rendered)
    
    # Generate PDF from HTML
    pdfkit.from_file(html_path, pdf_path)

    # Send the generated PDF to the user
    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
