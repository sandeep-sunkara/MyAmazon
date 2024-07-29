import csv
class register:
    def reg(self):
        f=open("custdata.csv","a",newline="")
        a=csv.writer(f)
        print("enter your details:")
        self.uname=input("enter username:")
        self.phno=int(input("enter phone number:"))
        self.adress=input("enter address:")
        self.pin=input("Enter your area Pin:")
        self.password=input("Enter your password:")
        a.writerow([self.uname,self.phno,self.adress,self.pin,self.password])
        print("Registration successful")
        return "hai"

    def login(self, uname, password):
        with open("custdata.csv", "r", newline="") as file:
            read = csv.reader(file)
            header = next(read)  # Read header row
            for row in read:
                if row[0] == uname and row[4] == password:  # Adjust indices based on CSV structure
                    return True
        return False   




