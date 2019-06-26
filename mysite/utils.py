import threading
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

class BaseEmailSender:
    from_email = "info@bnk.support"
    compliance_email_list = [
        'sellis@goldfieldsmoney.com.au',
        "warren.cheng@goldfieldsmoney.com.au",

    ]
    subject = ""
    template_path = ""
    def __init__(self, receiver_list, to_compliance = False,  **kwargs):

        self.receiver_list = receiver_list
        self.to_compliance = to_compliance
        self.kwargs = kwargs
    def get_context(self):
        #descendant class to overwrite this method
        return
    def send(self):
        htmly = get_template(self.template_path)
        text_content = ""
        html_content = htmly.render(self.get_context())


        cc = self.compliance_email_list if self.to_compliance else []
        msg = EmailMultiAlternatives(self.subject, text_content, self.from_email, self.receiver_list, cc = cc)
        msg.attach_alternative(html_content, "text/html")
        result = msg.send()
        if result == 1:
            print("Email Sent Successfully")
        else:
            print("Email Failed to Deliver")
    def async_send(self):
        thread = threading.Thread(target = self.send)
        thread.start()
        return
