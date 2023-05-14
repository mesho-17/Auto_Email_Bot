AUTOMAIL BOT

This is a Python program that uses voice recognition to send emails.

REQUIREMENTS

The following libraries must be installed to run this program:

smtplib
speech_recognition
pyttsx3
email
PyQt5

USAGE

Run the program in your command line: python AutomailBot.py
The Gmail login page will open in a maximized window.
The program will prompt you to say the name of the person you want to send the email to.
Once you say the name, the program will retrieve the email address associated with that name.
You will then be prompted to say the subject of the email and then the content.
The email will be sent to the recipient.
The program will ask if you want to send more emails. If you say "yes", the program will repeat the process from step 3.
Note: Make sure that you have given app access in your Google account settings and turn on less secure app access for the bot to automatically send emails for you.

FUNCTIONALITY

The program consists of the following functionalities:

Voice recognition: The program uses the speech_recognition library to retrieve the name of the person to send the email to, the subject of the email, and the content of the email.
Text-to-speech: The program uses the pyttsx3 library to read out prompts and confirmation messages.
Sending email: The program uses the smtplib and email libraries to send emails.
GUI: The program uses the PyQt5 library to create a simple GUI with navigation buttons, a URL bar, and a central web view for the Gmail login page.
