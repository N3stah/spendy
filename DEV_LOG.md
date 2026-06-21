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