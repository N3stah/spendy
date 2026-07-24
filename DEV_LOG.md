# Step 1 — Add a Single Expense
What I did:Created spendy.py with a config block, 3 functions with docstrings, and an if __name__ guard. The program asks for a description and amount then prints them back formatted.
What confused me: wasn't sure why we needed if __name__ == "__main__" since the program seemed to work without it. 
# Step 2 — Keep Adding Until Done
What I did: Added a while loop that keeps asking for expenses until I type "done". Each expense gets saved into a list as a dictionary.  
# Step 3 — Handle Bad Input   
What I did: Wrapped the amount input in a try/except block inside a while loop so the program no longer crashes on bad input.   
What confused me:I didn't understand the difference between try and except and when each one runs.
How I figured it out: I realised try runs the normal code and except only runs when something goes wrong — like when someone types abc instead of a number.  
# Step 4 — Remember Between Runs
What I did: Added functions to load expenses from a file when the program starts and save each new expense to the file right away.  
What confused me: I wasn't sure why we needed to check if the file exists first — wouldn't it always be there?  
How I figured it out: I realised the file only exists after you add your first expense, so on the very first run the program would crash without that check.  
# Step 5 — Show a Summary
What I did: Added a "show" command that prints all saved expenses in a numbered list with a total at the bottom.  
What confused me: I wasn't sure how to make the program show the list without quitting the loop.  
How I figured it out: I used `continue` to go back to the start of the loop after showing the list, so the user can keep adding expenses.  
# Step 6 — Categories  
What I did: Added a category field to every expense and a "filter" command that shows only expenses from one category with their total.   
What confused me: I wasn't sure how to handle my old expenses.csv that didn't have categories in it.  
How I figured it out: I made the loading code check if the category exists, and if not it uses "uncategorized" so the old data doesn't break anything.  
# ADD 01 — Timestamps on Every Expense 
What I did: Added a timestamp to every new expense using datetime, and updated the load and display functions to show the date.  
What confused me: I wasn't sure how to get the current date and time in Python.   
How I figured it out: I imported datetime and used strftime to format it nicely, then passed it into the save function like any other field.  
# ADD 02 — Delete an Expense  
What I did: Added a delete command that shows the numbered list, asks which one to remove, and confirms before deleting. I also made a rewrite function that saves the whole list back to the file.  
What confused me: I didn't know how to remove something from the middle of a CSV file.   
How I figured it out: I learned you can't easily delete from the middle, so instead I rewrite the whole file from the updated list after removing the item.  
# ADD 03 — Use CSV Properly With Python's csv Module  
What I did: Replaced manual string writing with Python's csv module so commas inside descriptions don't break the file. I also added a header row to the CSV file. 
What confused me: I didn't know why we needed `newline=""` when opening the file.  
# ADD 04 — Input Validation Beyond Numbers
What I did: Added checks for blank descriptions, blank categories, negative amounts, zero amounts, and amounts over $99,999. I also made sure all text inputs get stripped of extra spaces.  
# ADD 05 — Command Help Menu
What I did Added a welcome banner that shows when the program starts and a help command that reprints the menu anytime. I also updated the input prompt to hint that commands are available.  
What confused me: I wasn't sure if the banner should print every time the loop runs or just once at the start.  
# Part 3 — Polish
What I did: Cleaned up the display functions so expenses show in a neat table with aligned columns and headers. I also reviewed all the messages to make sure they sound friendly and consistent.  
What confused me: I wasn't sure how to make the columns line up when descriptions are different lengths.  
How I figured it out: I used Python's string formatting with width numbers like `<20` and `>10` so each column has a fixed width no matter what the content is.  
# Bug Fix — load_expenses() KeyError
What happened: The old expenses.csv had no header row so csv.DictReader could not find the "description" column and crashed.  
How I fixed it: Deleted the old file so spendy.py could create a fresh one with the correct header. Also added a header check in load_expenses() so it never crashes on a bad file again.
# Reflection
Hardest step: Step 04 — Remember Between Runs. I didn't know how to read and write files at all, and the csv module was completely new to me.  
Easiest step: Step 02 — Keep Adding Until Done. Once I understood while loops the logic clicked quickly and it felt satisfying to see it working.  
What I'd improve with more time: I'd add a way to edit an expense after adding it, not just delete it, and also I would add a search command to find expenses by keyword, and maybe a monthly summary that groups expenses by month instead of just by category  

# Add a count command  - update
What I did: Added a count command to display the total expenses inside the main function with in the While true loop 
           Also update the welcome banner to have the count command
I wasnt confussed in this step, I figured out that the load_expenses function loads expenses CSV file data, and since the csv load the data into a list variable i used a len() funtion to be able to get the total number of item insie the expense.csv file.
# additional fix for the count command
I had forgot to update the help menu funtion to also include the count function

# Add a total command
What I did I: I added a totat command to display the a grand total for all my expenses recoded in the expense.csv file insie the main function.
             Also update the welcome bunner and the help menu function to have the total command
I wasnt confused in this step, I used the same logic I had used in show summary funtion an used a sum() function plus a generator expression > sum(e["amount"] for e in expenses)

# # Edit function for users to modify an existing expense by its number after confirmation.
def edit_expense(expenses):

elif command == "edit":
            edit_expense(expenses) 
What I did: I created an edit command that allows users to modify an existing expense by selsecting the expense using the list number, by one can input hiss new values from discription amount and category of his/her choice.
    I did this by adding edit function before the main loop function and also added a edit command in thje main loop function.
>IN THE EDIT FUNNTION
1. In the edit function I Used a <if not expenses> this helps to check if the list is empty. if it find the list in the csv file empty i t prints a message No expenses to edit.
2. added a display option that prints the formatte table do that one can be able to see the number of their recorded expenses.
3. added a try and expect ValueError this converts a user inptut into a whole number and if one accientally type a word it identify the error and print "That's not a number - Cancelled.
4. added a validating range using <if choice < 1 or choice > len(expenses)> this prints a erroe message <That number is not in the list - Cancelled> if the number type is not in the list.
5. target = expenses[choice - 1] introduced a targeting index that grabs ath dictonary that the user wants to change using -1 to start counting fro 1 since python uses usualy start tomcount from 0 
6. I used the same helper funtion that I already had used to ask the user for updates details. 
7. expenses[choice - 1] this help in updating the list in my csv file this is able to pick the exact same spot an it overwrites the old dictionary with a bland new one containing the upated values
8. rewrite_csv(expenses) this helpsby saving the newly updated list and it overwrites my enter csv file.

### Task 003
## Stage 1 - Pytest Setup
What I did: first- Installed pytest in the virtual environment.       
            sencond- created `test_spendy.py` file in spendy folder, and wrote a basic math assertion to test my setup.
What confused me: I was running the pyton script directly insted of using pytest.
How I figured it out: Ran `pytest` in the terminal and confirmed it automatically detected `test_spendy.py` and returned "1 passed".
## Stage 2 - Testing 
What I did: Wrote a test function that builds a sample list of expenses and asserts that the sum of their amounts matches $22.00.
What confused me: How generator expressions `sum(e["amount"] for e in sample_expenses)` work in isolation inside a test.
How I figured it out: Created sample data matching Spendy's dictionary structure and verified that pytest checked the sum against my expected total.
## 3 - trying to test the add command 
   Ran into a error trying to run pytest in the the terminal,
   Error  OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.
   I tried writing the automated test that call `input()` directly and I realized that using input() freeze the program to wait for a human typing at a keyboard. This might have happend because my data logic is tangled inside the input function and I cannot test the underlying data without triggering a terminal prompt using my keyboard.
## Stage 4 - Separating Logic from I/O
What I did: I refactored Spendy to separate user interaction (`input`/`print`) from data processing by creating pure functions `add_expense_logic` and `calculate_total` in spendy.py inside the main loop function.
Bug encountered: When running `pytest` after the refactor, I encountered a   persistent failure: `OSError: reading from stdin while output is captured`. Additionally, manual testing showed a `KeyboardInterrupt` traceback when exiting the terminal app with `Ctrl+C` insted of using the `DONE` command in the terminal.
How I figured it out: I realized the pytest error was caused by a leftover interactive test (`test_add_expense_interactive`) from Stage 3 that was still sitting in my `test_spendy.py` file, trying to read from standard input. Once I deleted that lingering test, pytest passed successfully.