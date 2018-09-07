class Piano:
    def __init__(self):
        self.leter = ""
        
    def enter_input(self):
        self.leter = input("Please enter string ")
      
    def print_details(self):
        x = self.leter[1::2]
        print (x)
        



p = Piano()
p.enter_input()
p.print_details()