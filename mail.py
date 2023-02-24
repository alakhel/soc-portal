import smtplib
import ssl
import logging
import sys
from json import loads
from email.message import EmailMessage
from getpass import getpass
from xmlrpc.client import Boolean


logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')


class Emails():

    def __init__(self, smtp_server="smtp.gmail.com", smtp_port=587):
        self.username = input("Email: ")
        self.password = getpass("Mot de passe: ")

        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def authenticate(self) -> Boolean:
        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)

            context=ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
            context.set_ciphers('DEFAULT@SECLEVEL=1')

            server.starttls(context=context)

            server.ehlo()
            server.login(self.username, self.password)

            logging.info("[+] Authentication succeeded")
        except Exception as e:
            logging.error(f"[-] Error occured: {e}")
            return False

        self.server = server

        return True

    def parse_config_file(self, path: str) -> Boolean:
        try:
            with open(path, "r") as f:
                self.etudiants = loads(f.read())["images"]
        except Exception as e:
            logging.error(f'[-] Error occured: {e}')
            return False
        
        return True

    def send_mails(self, etudiants:list=None):
        subject = "[PROJET SOC] Identifiants de la plateforme"
        sent_to = self.etudiants if not etudiants else etudiants

        for etudiant in sent_to:
            to = etudiant['etudiant']
            mdp = etudiant['mdp']

            body = """
            Bonjour,

            Merci d'utiliser ces identifiants pour faire le login

            Email: %s
            Mot de passe tmp: %s

            Cordialement,
            Groupe Pentest

            """ % (to, mdp)

            msg = EmailMessage()
            msg.set_content(body)

            msg['Subject'] = subject
            msg['From'] = self.sent_from
            msg['To'] = to            

            try:
                self.server.send_message(msg)

                logging.info(f"[+] Mail to {to} sent")
            except Exception as e:
                logging.error(f"[-] Error occured when sending mail: {e}")
                exit(0)

    def close(self):
        self.server.close()


if __name__ == "__main__":
    emails = Emails()

    
    if emails.authenticate():  # and emails.parse_config_file(sys.argv[1]):
        emails.send_mails(etudiants=[{"etudiant": "jordan.laires.78@gmail.com", "mdp": "test"}])
        emails.close()