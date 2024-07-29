import csv
    
class avalprod:
    def add(self,n,m,q):
        self.n=n
        self.m=m
        self.q=q
        with open("store.csv","a",newline="") as file:
            a=csv.writer(file)
            a.writerow([self.n,self.m,self.q])
    def electronics(self):
        print("avaliable Electronics:")
        print("1.iphones""\n""2.macbook")
        sp=input("select product:")
        if sp=="1" or sp=="iphones":
            self.sp="iphone"
            print("Do you really want to purchase",self.sp,"if yes type 'yes'")
            sp=input()
            if(sp=="yes"):
                print("purchase of",self.sp,"successful")
            else:
                return o.electronics()
        elif sp=="2" or sp=="macbook":
            self.sp="macbook"
            print("Do you really want to purchase",self.sp,"if yes type 'yes'")
            sp=input()
            if(sp=="yes"):
                print("purchase of",self.sp,"successful")
            else:
                return o.electronics()
        else:
            print("Invalid choice")

    def fashion(self):
        print("avaliable Fashion")
        print("1.shirt""\n""2.Tshirt")
        sp=input("select product:")
        if sp=="1" or sp=="shirt":
            self.sp="shirt"
            print("Do you really want to purchase",self.sp,"if yes type 'yes'")
            sp=input()
            if(sp=="yes"):
                print("purchase of",self.sp,"successful")
            else:
                return o.fashion()
        elif sp=="2" or sp=="Tshirt":
            self.sp="Tshirt"
            print("Do you really want to purchase",self.sp,"if yes type 'yes'")
            sp=input()
            if(sp=="yes"):
                print("purchase of",self.sp,"successful")
            else:
                return o.fashion()
        else:
            print("Invalid choice")

    def stationary(self):
        print("avaliable stationary")
        print("1.book""\n""2.pen")
        sp=input("select product:")
        if sp=="1" or sp=="book":
            self.sp="book"
            print("avaliable",self.sp,":")
            print("Do you really want to purchase",self.sp,"if yes type 'yes'")
            sp=input()
            if(sp=="yes"):
                print("purchase of",self.sp,"successful")
            else:
                return o.stationary()
        elif sp=="2" or sp=="pen":
            self.sp="pen"
            print("Do you really want to purchase",self.sp,"if yes type 'yes'")
            sp=input()
            if(sp=="yes"):
                print("purchase of",self.sp,"successful")
            else:
                return o.stationary()
        else:
            print("Invalid choice")
o=avalprod()