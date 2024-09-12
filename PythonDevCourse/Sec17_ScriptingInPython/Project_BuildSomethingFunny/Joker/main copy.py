import tkinter as tk
import pyjokes
import smtplib
from email.message import EmailMessage
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, PHONE_NUMBER, TO_EMAIL, TWILIO_NUMBER  # type: ignore
from twilio.rest import Client


current_joke = ''


def get_new_joke():
    global current_joke
    current_joke = pyjokes.get_joke('en', 'all')
    joke_label.config(text=current_joke)


def share_via_email():
    email = EmailMessage()
    email['from'] = 'Eto Svn'
    email['to'] = TO_EMAIL
    email['subject'] = 'Jokes collection'
    email.set_content(current_joke)
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()  # tls: encryption mechanism
        smtp.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        smtp.send_message(email)
        tk.Label(root, text="Joke has been sent to your email",
                 font=('calibri', 12))


def share_via_sms():
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_=TWILIO_NUMBER,
        body=current_joke,
        to=PHONE_NUMBER
    )


root = tk.Tk()
root.title('Joker')

# Set window size (Optional)
root.geometry("500x400")  # Width x Height

# Set background color for the entire window
# Light blue background color for the whole screen
root.configure(bg="#ADD8E6")

joke_label = tk.Label(root, text="", wraplength=400, font=('calibri', 20), bg="#ADD8E6",  # Light Blue background to match window
                      fg="blue")
joke_label.pack(pady=40)
next_button = tk.Button(root, text='Next Joke',
                        # Darker Green when button is pressed
                        command=get_new_joke, font=('calibri', 12),
                        bg="#90EE90",  # Light Green background
                        fg="black",    # Black text color
                        activebackground="#32CD32",  # Darker Green when button is pressed
                        activeforeground="white"     # White text color when button is pressed
                        )
next_button.pack(pady=5)
quit_button = tk.Button(
    root, text='Quit', command=root.destroy, font=('calibri', 12),
    bg="red",  # Light Pink background
    fg="black",    # Black text color
    activebackground="#FF69B4",  # Darker Pink when button is pressed
    activeforeground="white"     # White text color when button is pressed
)
quit_button.pack(pady=5)

share_via_email_button = tk.Button(
    root, text='Share via Email', command=share_via_email, font=('calibri', 12),
    bg="#FFB6C1",  # Light Pink background
    fg="black",    # Black text color
    activebackground="#FF69B4",  # Darker Pink when button is pressed
    activeforeground="white"     # White text color when button is pressed
)
share_via_email_button.pack(pady=5)
share_via_sms_button = tk.Button(
    root, text='Share via SMS', command=share_via_sms, font=('calibri', 12),
    bg="#FFB6C1",  # Light Pink background
    fg="black",    # Black text color
    activebackground="#FF69B4",  # Darker Pink when button is pressed
    activeforeground="white"     # White text color when button is pressed
)
share_via_sms_button.pack(pady=5)
# tk.Button(frm, text='Share via Email',
#           command=send_email).grid(column=0, row=2)
# tk.Button(frm, text='Share via SMS', command=send_sms).grid(column=2, row=2)
get_new_joke()
root.mainloop()
