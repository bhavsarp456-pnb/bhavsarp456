class Email:
    def __init__(self, to, cc, bcc, subject, message):
        self.to = to
        self.cc = cc
        self._bcc = bcc #private attribute
        self.subject = subject
        self.message = message
        self.sender = "Gmail"

    def print_email(self):
        print(f"To:{self.to}\nCC:{self.cc}\nSubject:{self.subject}\nMessage:{self.message}\nSender:{self.sender}")
    
    def get_bcc(self):
        return self._bcc

    def set_bcc(self, email):
        self._bcc = email
        print(self._bcc)

my_email = Email("bhavsarp456@gmail.com",
 None, "bhavsarp537@gmail.com", 
 "Welcome to RST Forum", 
 "You are heardly welcome to the placement cell!")

my_email.print_email()
my_email.get_bcc()
my_email.set_bcc("bpiyush1994@gmail.com")