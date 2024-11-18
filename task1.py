class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage  
        self.battery_life = battery_life  

    def make_call(self, contact):
        print(f"{self.brand} {self.model} is making a call to {contact}.")

    def send_message(self, contact, message):
        print(f"{self.brand} {self.model} is sending a message to {contact}: '{message}'")

    def check_battery(self):
        print(f"{self.brand} {self.model} has {self.battery_life} hours of battery life left.")

class AndroidPhone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, android_version):
        super().__init__(brand, model, storage, battery_life)
        self.__android_version = android_version  

    
    def get_android_version(self):
        return self.__android_version

    def make_call(self, contact):
        print(f"{self.brand} {self.model} (Android) is making a call with advanced call settings to {contact}.")

    def install_app(self, app_name):
        print(f"Installing {app_name} on {self.brand} {self.model} running Android {self.__android_version}.")

class iPhone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, ios_version):
        super().__init__(brand, model, storage, battery_life)
        self.__ios_version = ios_version  # Private attribute

    def get_ios_version(self):
        return self.__ios_version

    def make_call(self, contact):
        print(f"{self.brand} {self.model} (iOS) is making a FaceTime call to {contact}.")

    def install_app(self, app_name):
        print(f"Installing {app_name} on {self.brand} {self.model} running iOS {self.__ios_version}.")


samsung_phone = AndroidPhone("Samsung", "Galaxy S21", 128, 24, "11.0")
apple_phone = iPhone("Apple", "iPhone 13", 256, 20, "15.2")

samsung_phone.make_call("Alice")
apple_phone.make_call("Bob")

samsung_phone.install_app("WhatsApp")
apple_phone.install_app("Instagram")

print(f"Android Version: {samsung_phone.get_android_version()}")
print(f"iOS Version: {apple_phone.get_ios_version()}")
