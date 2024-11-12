# import qrcode  # ye qr code create krne ke liye module hota hai jisse main as ki help se qr name de diya name esay krne ke liye
# Qr_details = input("Enter Your Link / Text Here") # For taking user input
# img = qrcode.make(Qr_details) #yaha pr Qr_details hai ye ek variable hai jiske andr maine qr.make("") ka command run kiya hai yha double code ke andr mai qr ki jo details rkhne hi hai vo deta hu 
# img.save("Qr.png") #ye command qr ka name and format decide ke liye use hoti hai 

###Simple Qr Code Ends Here 👆

###Next Level Starts Here👇👇

import qrcode
from PIL import Image
import qrcode.constants

# Create a QRCode object with properties
Qr_Property = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Prompt user for QR data input
qrdata = input("Enter your link here: ")
Qr_Property.add_data(qrdata)
Qr_Property.make(fit=True)

# Generate image with customized colors
img = Qr_Property.make_image(fill_color="orange", back_color="white")
img.save("Adila.png")  # Save the QR code as Adila.png

#### Qr code for simple phone number
import qrcode

phone_number = input("Enter the phone number: ")
qr_data = f"tel:{phone_number}"  # Format for a direct phone link

img = qrcode.make(qr_data)
img.save("phone_contact.png")


#qr code for storing number , name , and other details 
import qrcode

# Gather contact information
name = input("Enter the contact's name: ")
phone_number = input("Enter the phone number: ")
email = input("Enter the email address (optional): ")

# vCard format string
vcard_data = f"""
BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone_number}
EMAIL:{email}
END:VCARD
"""

# Generate QR code
Qr_Property = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
Qr_Property.add_data(vcard_data)
Qr_Property.make(fit=True)

# Customize the image if desired
img = Qr_Property.make_image(fill_color="black", back_color="white")
img.save("contact_vcard.png")
