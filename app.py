from flask import Flask, render_template, request, redirect
import os
from dotenv import load_dotenv
from twilio.rest import Client

app = Flask(__name__)
load_dotenv()

# WhatsApp Message Sender Function
def send_whatsapp_message(body):
    client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_TOKEN"))
    message = client.messages.create(
        from_=os.getenv("TWILIO_WHATSAPP"),
        body=body,
        to=os.getenv("RECEIVER_PHONE")
    )
    print("WhatsApp sent:", message.sid)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        address = request.form['address']
        mushroom_type = request.form['mushroom_type']
        quantity = request.form['quantity']

        message = f"\nNew Order Received!\nName: {name}\nPhone: {phone}\nAddress: {address}\nMushroom: {mushroom_type}\nQuantity: {quantity} kg"
        send_whatsapp_message(message)

        return render_template('success.html', name=name)
    return render_template('order.html')

if __name__ == '__main__':
    app.run(debug=True)

