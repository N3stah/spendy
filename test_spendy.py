from spendy import add_expense_logic, calculate_total
#from spendy import get_description

def test_math():
    assert 2 + 2 == 4
    
#stage 2
def test_calculate_total():
    #sample list of expenses.
    sample_expenses = [
        {"description": "Coffee", "amount": 4.50, "category": "food", "date": "2026-07-7 10:00"},
        {"description": "Bus fare", "amount": 2.50, "category": "transport", "date": "2026-07-7 10:30"},
        {"description": "Book", "amount": 15.00, "category": "fun", "date": "2026-07-7 11:00"}
    ]

    #total calculation
    total = sum(e["amount"] for e in sample_expenses)

    # total should be 22.00
    assert total == 22.00
    
# STAGE 3- Try to test the add command
#def test_add_expense_interactive():
    # Using get description function to call input and test the description or the command
 #   desc = get_description()
  #  assert desc == "Coffee"
  
 # STAGE 5- Testing edge cases on the pure functions
def test_calculate_total_empty():
    # Edge case that returns 0 if the expense list is empty
    empty_expenses = []
    assert calculate_total(empty_expenses) == 0.0

def test_add_expense_logic():
    # Test that our list updater correctly appends a new expense to the list and returns the updated list
    expenses = []
    updated = add_expense_logic(expenses, "Snack", 3.00, "food", "2026-07-24 22:30")
    
    assert len(updated) == 1
    assert updated[0]["description"] == "Snack"
    assert updated[0]["amount"] == 3.00
    
   # STAGE 5.1- Testing negative numbers in the pure function if someone gets a refund.
def test_calculate_total_negatives():
    #data simulating a purchase and a refund
    sample_expenses = [
        {"description": "Shirt", "amount": 50.00, "category": "clothes", "date": "2026-07-27 15:30"},
        {"description": "Refund", "amount": -20.00, "category": "clothes", "date": "2026-07-27 15:30"}
    ]
    
    #getting to run a total calculation on the data
    total = calculate_total(sample_expenses)
    
    # 3. ASSERTION: Demand that 50 + (-20) equals 30
    assert total == 30.00