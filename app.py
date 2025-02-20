from flask import Flask, render_template, send_from_directory

app = Flask(__name__, subdomain_matching=True)

app.config['SERVER_NAME'] = 'localhost:5000'  # Tell Flask about your local subdomain

# Root Route
@app.route('/')
def home():
    return render_template('index.html')  # Homepage

# Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')  # Contact page

# Serve blank.html from the root folder
@app.route('/blank.html')
def serve_blank():
    return send_from_directory('.', 'blank.html')  # Serve blank.html from the root folder

# Handle Subdomain Route (hidden subdomain)
@app.route('/', defaults={'subdomain': None})
@app.route('/', subdomain='<subdomain>')
def handle_subdomain(subdomain):
    if subdomain == 'hidden':
        return render_template("subdomain.html")  # Serve hidden subdomain page
    return "This subdomain does not exist.", 404  # Return 404 for any other subdomain

if __name__ == '__main__':
    app.run(debug=True)
