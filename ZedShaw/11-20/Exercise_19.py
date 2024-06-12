# ZedShaw Python Exercise #19
# Continued use of FUNCTIONS, I went above nad beyond and made a class

class CookieBox:
    def __init__(self, CookieAmount: int):
        self.CookieAmount = CookieAmount

    def get_cookies(self):
        print(f"There are {self.CookieAmount} cookies in the box")
        return self.CookieAmount

# Creating an instance of the CookieBox class
box = CookieBox(3)

# Calling the get_cookies method
box.get_cookies()
