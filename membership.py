from tabulate import tabulate
from math import sqrt

class Membership:      
    
        data = {"Sumbul": "Platinum", "Ana" : "Gold", "Cahya": "Platinum"}
    
    
        def __init__(self, username):
            self.username = username
        
    
        def show_benefit(self):
            tables = [
                ["Platinum","15%","Benefit Gold + Silver + Voucher Liburan + Cashback 30%"],
                ["Gold", "10%", "Benefit Silver + Voucher Ojek Online"],
                ["Silver", "8%", "Voucher Makanan"]
                ]
                      
            headers = ["Membership","Discount","Another Benefit"]
            
            print("PacCommerce Membership Benefit")
            print("-"*86)
            print(tabulate(tables, headers, tablefmt='github', stralign="center")) 
        
            
        
        def show_requirements(self):
            tables = [
                ["Platinum", 8, 15],
                ["Gold", 6, 10],
                ["Silver", 5, 7]
                ]
            
            headers = ["Membership", "Monthly Expense (juta)", "Monthly Income (juta)"]
            
            print("PacCommerce Membership Requirements")
            print("-"*86)
            print(tabulate(tables, headers, tablefmt='github', stralign="center")) 
        
            
        
        def predict_membership(self, username, monthly_expense, monthly_income):
            
            res=[] 
            
            membership_parameter = [[8, 15], [6, 10], [5, 7]]
            
            
            for index, _ in enumerate(membership_parameter):
                
                tmp = round(sqrt((monthly_expense - membership_parameter[index][0])**2 + (monthly_income - membership_parameter[index][1])**2), 2)
                
            
                        
                res.append(tmp)
                
            res_dict = {
                "Platinum" : res[0],
                "Gold" : res[1],
                "Silver" : res[2]
                }
                
            print(f'Hasil perhitungan Euclidean Distance dari user {self.username} adalah {res_dict}')
            
            for member, distance in res_dict.items():
                if distance == min(res):
                    self.data[username] = member
                    return member
        
        
        def show_membership(self, username):
            if username in self.data:
                return self.data.get(username)
            
        
        def calculate_price(self, username, list_harga):
            try:
                if username in self.data:
                    membership = self.data.get(username)
                    if membership == "Platinum":
                        total_harga = (sum(list_harga)-(sum(list_harga)*0.15))
                        return total_harga
                    
                    elif membership == "Gold":
                        total_harga = (sum(list_harga)-(sum(list_harga)*0.10))
                        return total_harga
                    
                    elif membership == "Silver":
                        total_harga = (sum(list_harga)-(sum(list_harga)*0.08))
                        return total_harga
                    
                    else:
                        raise Exception("Membership doesn't exist")
                                            
                else:
                    raise Exception("Membership tidak ada di database")
                                    
            except:
                raise Exception("Invalid process")