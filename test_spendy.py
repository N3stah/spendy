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