class Car:
    def __init__(self, model):
        self.model = model

class Driver:
    def __init__(self, name):
        self.name = name

    # The association happens here: passing the car into a method
    def drive(self, car_object):
        print(f"{self.name} is driving a {car_object.model}.")

# 1. Create two totally separate things
my_car = Car("Tesla Model 3")
me = Driver("Alex")

# 2. They interact (Association)
del my_car
print(my_car.model)
me.drive(my_car)  
del me
print(my_car.model)
# Output: Alex is driving a Tesla Model 3.


#----------------------------------------------------
#coupling - tightly and loosely coupling


class GmailService:
    def send(self, message):
        print(f"Sending Email via Gmail: {message}")

class NotificationManager:
    def __init__(self):
        # ❌ TIGHTLY COUPLED: This class is locked into GmailService.
        # If we switch to Outlook tomorrow, we must rewrite this class.
        self.email_service = GmailService() 

    def send_alert(self, text):
        self.email_service.send(text)


class NotificationManager:
    #  LOOSELY COUPLED: We inject the service from the outside.
    # This class doesn't care WHAT service it is, as long as it has a .send() method.
    def __init__(self, any_email_service):
        self.email_service = any_email_service 

    def send_alert(self, text):
        self.email_service.send(text)

# Now you can easily plug in ANYTHING you want!
gmail = GmailService()
manager = NotificationManager(gmail) # Plugs in Gmail smoothly

