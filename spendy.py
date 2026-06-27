import csv  
import os   
from datetime import datetime   
 
VERSION    = "1.0"   
DATA_FILE  = "expenses.csv"  
MAX_AMOUNT = 99999  
 
 #  welcome banner and command menu
def show_banner(): 
    title = f"SPENDY v{VERSION}"    
    print("------------------------------")
    print(f"|  {title:^26}|")
    print("|     Your spending tracker  |")
    print("------------------------------")
    print()    
    print("  add      - Add a new expense")
    print("  show     - View all expenses")
    print("  filter   - Filter by category")
    print("  delete   - Remove an expense")
    print("  help     - Show this menu")
    print("  done     - Exit the program")
    print("  count    - display the total expenses")
    print("  total    - display the total amount spent")
    print("  delete   - Remove an expense")
    print("  edit     - Modify an existing expense")
    print()   
    
#   Help menu function
def show_help():     
    print("\n Commands")
    print("  add      - Add a new expense")
    print("  show     - View all expenses")
    print("  filter   - Filter by category")
    print("  delete   - Remove an expense")
    print("  help     - Show this menu")
    print("  done     - Exit the program")
    print("  count    - display the total expenses")
    print("  total    - display the total amount spent")
    print("  delete   - Remove an expense")
    print("  edit     - Modify an existing expense")
    print("\n")
    
#   summary function to display all expenses in a formatted table
def show_summary(expenses): 
    if not expenses:  
        print("No expenses recorded yet.\n") 
        return 
    
    print("\n All Expenses")
    print(f"{'#':<4} {'Date':<16} {'Description':<20} {'Amount':>10} {'Category':<12}")  
    print("-" * 66)  
  
    for i, expense in enumerate(expenses, start=1):  
        raw_desc = expense["description"] 
        desc     = raw_desc[:18] + ".." if len(raw_desc) > 20 else raw_desc   
        amt      = expense["amount"]  
        cat      = expense["category"]  
        date     = expense["date"]    
        print(f"{i:<4} {date:<16} {desc:<20} ${amt:>9.2f} {cat:<12}")   
   
    total = sum(e["amount"] for e in expenses)   
    print("-" * 66)  
    print(f"{'Total:':<42} ${total:>9.2f}") 
    print("\n") 
    
#   filter function to show expenses by category in a formatted table.
def show_filter(expenses):   
    if not expenses:  
        print("No expenses recorded yet.\n")  
        return   
  
    target  = input("Filter by category: ").strip().lower()  
    matches = [e for e in expenses if e["category"].lower() == target] 
  
    if not matches: 
        print(f"No expenses found in category '{target}'.\n") 
        return  
 
    print(f"\n--- {target.title()} Expenses ---") 
    print(f"{'#':<4} {'Date':<16} {'Description':<20} {'Amount':>10}")  
    print("-" * 54)  
 
    for i, expense in enumerate(matches, start=1):  
        raw_desc = expense["description"]  
        desc     = raw_desc[:18] + ".." if len(raw_desc) > 20 else raw_desc  
        print(f"{i:<4} {expense['date']:<16} {desc:<20} ${expense['amount']:>9.2f}")  
 
    total = sum(e["amount"] for e in matches)   
    print("-" * 54)  
    print(f"{'Total:':<42} ${total:>9.2f}")  
    print("\n")
 
 
#   Expenses functions to load expenses in the CSV file.
def load_expenses(): 
    if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:  
        return [] 
    
    expenses = []  
    with open(DATA_FILE, "r", newline="") as f:  
        reader = csv.DictReader(f)  
  
        if reader.fieldnames is None or "description" not in reader.fieldnames:   
            print("Warning: expenses.csv has no valid header. Starting fresh.") 
            return []  
  
        for row in reader:    
            expenses.append({  
                "description": row["description"].strip(),  
                "amount":      float(row["amount"]), 
                "category":    row.get("category", "uncategorized").strip(), 
                "date":        row.get("date", "unknown").strip()  
            })   
    return expenses   
   
#   Expenses functions to save expenses in the CSV file.  
def save_expense(description, amount, category, timestamp):   
    file_exists = os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0   
    with open(DATA_FILE, "a", newline="") as f:  
        writer = csv.writer(f) 
        if not file_exists:  
            writer.writerow(["description", "amount", "category", "date"])  
        writer.writerow([description, amount, category, timestamp])   
  
#   Expenses funtion to rewrite expenses in the CSV file.
def rewrite_csv(expenses):  
    with open(DATA_FILE, "w", newline="") as f: 
        writer = csv.writer(f) 
        writer.writerow(["description", "amount", "category", "date"]) 
        for e in expenses: 
            writer.writerow([e["description"], e["amount"], e["category"], e["date"]])   
            
#   Delete function for user to remove an expense by its number after confirmation.
def delete_expense(expenses): 
    if not expenses:  
        print("No expenses to delete.\n") 
        return  
   
    show_summary(expenses)   
   
    try:   
        choice = int(input("Enter the number of the expense to delete: "))   
    except ValueError:  
        print("That's not a number - Cancelled.\n")
        return   
       
    if choice < 1 or choice > len(expenses):   
        print("That number is not in the list - Cancelled.\n")
        return  
   
    target  = expenses[choice - 1]  
    confirm = input(   
        f"Delete '{target['description']} — ${target['amount']:.2f}'? (y/n): "   
    ).strip().lower()  
  
    if confirm == "y":  
        removed = expenses.pop(choice - 1) 
        rewrite_csv(expenses) 
        print(f"Deleted: {removed['description']} — ${removed['amount']:.2f}\n")  
    else:  
        print("Cancelled - Nothing was deleted.\n")  

# Edit function for users to modify an existing expense by its number after confirmation.
def edit_expense(expenses):
    if not expenses:
        print("No expenses to edit.\n")
        return

    show_summary(expenses)

    try:
        choice = int(input("Enter the number of the expense to edit: "))
    except ValueError:
        print("That's not a number - Cancelled.\n")
        return

    if choice < 1 or choice > len(expenses):
        print("That number is not in the list - Cancelled.\n")
        return

    target = expenses[choice - 1]
    print(f"\nEditing '{target['description']} — ${target['amount']:.2f}'")
    print("Enter new details")
    
    new_description      = get_description()
    new_amount    = get_valid_amount()
    new_category  = get_category()
    new_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    expenses[choice - 1] = {
        "description": new_description,
        "amount":      new_amount,
        "category":    new_category,
        "date":        new_timestamp
    }
    
    rewrite_csv(expenses)
    print(f"Updated: {new_description} — ${new_amount:.2f}\n")  
          
#   Input function to promt the user for a non-blank description or command.
def get_description():  
    while True:   
        description = input("Description (or command): ").strip()  
        if description == "":  
            print("Description cannot be blank - Try again!.")
            continue  
        return description  
   
#   Prompt user for a valid posotive expense amount.
def get_valid_amount():  
    while True:  
        amount_input = input("Amount: $").strip()  
        try:  
            amount = float(amount_input)   
        except ValueError:   
            print("That's not a valid amount -try again.")
            continue   
        if amount <= 0:   
            print("Amount must be greater than zero - Try again.")
            continue      
        if amount > MAX_AMOUNT:   
            print(f"Amount is too large. Maximum allowed is ${MAX_AMOUNT:,}. Try again.")  
            continue  
  
        return amount   
   
#  Prompt user for a non-blank expense
def get_category():   
    while True:   
        category = input("Category (e.g. food, transport, medical, fun, etc): ").strip().lower()
        if category == "":   
            print("Category cannot be blank. Try again.")   
            continue  
        return category 
 
  
# Main loop function to load, add, save, show, filter, delete, and help.
   
def main():   
  
    expenses = load_expenses()  
    show_banner()   
    
    while True:   
        description = get_description()   
        command     = description.lower()   
   
        if command == "done":   
         break
   
        elif command == "show":   
            show_summary(expenses)   
   
        elif command == "filter":   
            show_filter(expenses)   
  
        elif command == "delete":   
            delete_expense(expenses)  
  
        elif command == "help":  
           show_help() 
        
        elif command == "count": 
            print(f"Total expenses: {len(expenses)}")
         
        elif command == "total":
            grand_total = sum(e["amount"] for e in expenses)
            print(f"Total spent: ${grand_total:.2f}\n")
            
        elif command == "edit":
            edit_expense(expenses)    
                 
        else:    
            amount    = get_valid_amount()   
            category  = get_category()     
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M") 
  
            expenses.append({ 
                "description": description, 
                "amount":      amount,  
                "category":    category,  
                "date":        timestamp   
            })   
            save_expense(description, amount, category, timestamp) 
            print(f"Added: {description} — ${amount:.2f} [{category}] on {timestamp}\n")  
   
    count         = len(expenses)  
    running_total = sum(e["amount"] for e in expenses)   
  
    if count == 0:   
        print("No expenses added.")   
    elif count == 1:  
        print(f"You added 1 expense totaling ${running_total:.2f}.")   
    else:   
        print(f"You added {count} expenses totaling ${running_total:.2f}.")   
  
  
if __name__ == "__main__":   
    main()   