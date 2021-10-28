#Budget App in Python (practice with OOP)

#DEFINING SOME GENERAL FUNCTIONS TO BE USED

def truncate(n):
    multiplier = 10;
    return int(n * multiplier) / multiplier;

def getTotals(listOfCategories):
    total = 0;
    breakdown = [];
    for item in listOfCategories:
        total += item.get_withdrawals();
        breakdown.append(item.get_withdrawals());
    rounded = list(map(lambda x: truncate(x/total), breakdown));
    return rounded;

def create_spend_chart(listOfCategories):

    msg = "Percentage spent by category\n";
    i = 100;
    totals = getTotals(listOfCategories);
    while i >= 0:
        categorySpaces = " ";
        for total in totals:
            if total * 100 >= i:
                categorySpaces += "o  ";
            else:
                categorySpaces += "   ";
        msg += str(i).rjust(3) + "|" + categorySpaces + "\n";
        i -= 10;

    dashes = "-" + "---"*len(listOfCategories);
    names = [];
    xAxis = "";
    for category in listOfCategories:
        names.append(category.name);  

    maxi = max(names, key=len);

    for x in range(len(maxi)):
        nameString = "     ";
        for name in names:
            if x >= len(name):
                nameString += "   ";
            else:
                nameString += name[x] + "  ";
            
        if x != len(maxi) - 1:
            nameString += "\n";
        
        xAxis += nameString;

    msg += dashes.rjust(len(dashes) + 4) + "\n" + xAxis;

    return msg;



#CLASS: CATEGORY

class Category:

    def __init__(self, name):
        self.name = name;
        self.ledger = list();

    def __str__(self):
        title = f"{self.name:*^30}\n";
        items = "";
        total = 0;
        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n';

            total += item['amount'];
        
        output = title + items + "Total: " + str(total);
        return output;


    
    #DEFINING THE METHODS OF THE CLASS

    def deposit(self, amount, description=""):  
        self.ledger.append({"amount": amount, "description": description});
        
        
    def withdraw(self, amount, description=""):            
        if self.check_funds(amount):
            amount = -amount
            self.ledger.append({"amount": amount, "description": description});
            return True;
        else:
            return False;    
        

    def get_balance(self):
        ledgerTotal = 0;
        for thing in self.ledger:
            ledgerTotal += thing["amount"];
        return ledgerTotal;                    

    def transfer(self, amount, category):      
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.name);
            category.deposit(amount, "Transfer from " + self.name);
            return True;
        return False;                                

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True;
        else:
            return False;
        
    def get_withdrawals(self):
        total = 0;
        for item in self.ledger:
            if item["amount"] < 0:
                total += item["amount"];
        return total;


