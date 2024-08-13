from datetime import datetime

class MyMall():
    def __init__(self) -> None:
        '''initialize the dictionary of products as [Product : [item count, Price]]'''
        self.products = {
            "Air freshener": [10, 200],
            "Aluminum foil": [10, 100],
            "Batteries": [10, 300],
            "Bleach": [10, 250],
            "Coffee filters": [10, 150],
            "Dish soap": [10, 20],
            "Dishwasher detergent": [10, 30],
            "Fabric softener": [10, 50],
            "Floor cleaner": [10, 90],
            "Garbage bags": [10, 40],
            "Glass spray": [10, 60],
            "Laundry detergent": [10, 10]
        }

        print("*"*20, "WELCOME TO Mall", "*"*20)

    def addItem(self)->int:
        print('Available Products')
        print('Product\t\tItem Available\t\tPrice')
        #Print all availabe products by iterating on 
        for product in self.products:
            print(f"{product}\t\t{self.products[product][0]}\t\t{self.products[product][1]}")
        
        product_name = input('Enter the name of Product(Case Sensitive)') #accept product name from user
        if self.products[product_name]: #check whether it exists or not
            quantity = int(input('Enter How many item you want to add : ')) #if exits then accept quantity
            if self.products[product_name][0] >= quantity: #check availability of the product
                self.products[product_name][0] -= quantity  #update the quantity of problem 
                with open("bill.txt", "a+") as fp: #open the file 
                    fp.write(f"{product_name}\t{self.products[product_name][1]} X\t{quantity}\t=>{self.products[product_name][1] * quantity}\n") #write record
                return self.products[product_name][1] * quantity    #return the amount
            else:   
                #else return 0 and say product is out of stock
                print(f"Product out of stock!!")
                return 0
        else:
            print("No Product Matched !!")
            return 0
        
    def makeBill(self):
        custumer_name = input("Enter Customer Name : ") #accept customer name
        total_bill = 0 #initialize the variable = 0 to keep track of total amount
        with open("bill.txt", "w") as fp: #open file pointer and write defualt stats
            fp.write("===============================\n")
            fp.write(f"\t\tXYZ Super Market\n===============================\nBill to : {custumer_name}\n")
            fp.write(f"Date:{datetime.now()}\n")
            fp.write("===============================")
            fp.write('\nProduct\t\tItem Available\t\tPrice\n')
        while True: #loop to create menu
            choice = input("Do You want to continue? (y/n)")
            if choice == "n" or choice == "N":
                with open("bill.txt", "a+") as fp: #write all neccesary records
                    fp.write("===============================")
                    fp.write(f"\nTotal Bill : {total_bill}\n")
                    fp.write("===============================")
                    fp.write("\nThank You For Visiting Us !")
                break
            
            total_bill = self.addItem()
       
    def startSystem(self):
        '''This is function is used to start the system and vanishing last record file'''
        while True:
            choice = input("Do You want to continue? (y/n)")
            if choice == "n" or choice == "N":
                break
            self.makeBill()

#driver code
if __name__ == "__main__":
    user = MyMall() #create the object of the class 

    #call the member function to start the system
    user.startSystem()

'''
This code is uploaded on github.com/aniketArun
'''