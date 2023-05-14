import sys
import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        self.browser.setUrl(QUrl('http://www.gmail.com'))
        self.showMaximized()
    
        listener = sr.Recognizer() #collects the voice input
        engine = pyttsx3.init()

    # def talk(text):
    #     engine.say(text)
    #     engine.runAndWait()

        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Prev', self)
        back_btn.triggered.connect(self.browser.back) 
        navbar.addAction(back_btn)

        forward_btn = QAction('Next', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.Url_bar = QLineEdit()
        self.Url_bar.returnPressed.connect(self.navigate_to_Url)
        navbar.addWidget(self.Url_bar)

        self.browser.urlChanged.connect(self.update_Url)

    def navigate_home(self):
        # self.browser.setUrl(QUrl('www.gmail.com'))
        self.browser.setUrl(QUrl('http://www.gmail.com'))

    def navigate_to_Url(self):
        Url = self.Url_bar.text()
        self.browser.setUrl(QUrl(Url))

    def update_Url(self, Url):
        self.Url_bar.setText(Url.toString())
    
    
    def get_info():
        try:
            with sr.Microphone() as source:
                    print('listening...')
                    voice = listener.listen(source)
                    info = listener.recognize_google(voice)
                    print("Receiver : ", info)               # Check this print output and verify with the ones in 'email_list', this should clear your confusion.
                    return info.lower()
        except:
            pass

    def send_email(receiver, subject, message):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()                                            # providing your account's password allows the bot to automatically access your account
        server.login('meshkartelo12@gmail.com', 'BlackLivesMatter')  # Make sure to give app access in your Google account settings
                                                                    # that is, turn on less secure app access for the bot to automatically send emails for you.
        email = EmailMessage()
        email['From'] = 'sender_Email'
        email['To'] = receiver
        email['subject'] = subject
        email.set_content(message)
        server.send_message(email)
        #server.sendmail#('senders email address',
                    # 'receivers email address'
                    #'message to be sent'
                    #)

    email_list = {
        'mesh': 'pangasmeshack@gmail.com',
        'Esther': 'estherkataboi@gmail.com',
        'none': 'noahkataboi@gmail.com',
        'Maggy': 'alookataboi@gmail.com'
    }

    def talk(text):
        engine.say(text)
        engine.runAndWait()
    def get_email_info():
        talk('To whom do you want to send the email?')  #using pyttsx3. Text To Speech...
        name = get_info()
        receiver = email_list[name]
        print(receiver)
        talk('What is the subject of your email?')
        subject = get_info()
        talk('Tell me the text in your email.')
        message = get_info()
        send_email(receiver, subject, message)
        talk('Hey, lambistic shit, your email is sent successfully')
        talk('Would you like to send more email?')
        send_more = get_info()
        if 'yes' in send_more:
            get_email_info()
        # else:
            # return


        get_email_info()

app = QApplication(sys.argv)
QApplication.setApplicationName('Automail Bot')
window = MainWindow()
app.exec_()

    # quit(q)
