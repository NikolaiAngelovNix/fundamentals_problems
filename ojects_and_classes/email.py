class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


current_email = input()
emails_list = []

while current_email != "Stop":
    current_email = current_email.split(" ")
    sender = current_email[0]
    receiver = current_email[1]
    content = current_email[2]
    email = Email(sender, receiver, content)
    emails_list.append(email)
    current_email = input()

indexes = [int(x) for x in input().split(", ")]
for ind in range(len(emails_list)):
    if ind in indexes:
        emails_list[ind].send()

for email in emails_list:
    print(email.get_info())
