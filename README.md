# Birthday WhatsApp Automation

This application automatically sends personalized birthday wishes with customized cake images via WhatsApp.

## Setup Instructions

1. Make sure you have Python 3.8 or higher installed
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Prepare your contacts list:
   - Use the provided `contacts.csv` file as a template
   - Format: name, phone number (with country code), birthday (MM-DD format)
   - Example: `John Doe,+1234567890,03-15`

4. Add a cake image:
   - Name it `cake_template.png`
   - Place it in the same directory as the script

## Building the Executable

To create the standalone executable:
```
pyinstaller --onefile --add-data "cake_template.png;." --add-data "contacts.csv;." birthday_automation.py
```

The executable will be created in the `dist` directory.

## Usage

1. Double-click the executable
2. The program will:
   - Check for birthdays on the current date
   - Create personalized cake images
   - Send WhatsApp messages automatically
3. First-time usage:
   - You'll need to scan the QR code to log into WhatsApp Web
   - Keep your phone connected to the internet

## Notes

- The program uses WhatsApp Web, so you need an internet connection
- Your phone must be connected to the internet while the program runs
- Messages are sent with a delay to avoid rate limiting
- The program will clean up temporary image files after sending 