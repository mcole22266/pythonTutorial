# Bank App

This is my initial completed Bank App. Eventually, it would be cool to adapt it to some sort of 
personal web service but, for now, this should suffice. Mostly wanted to show it off but 
figured it might actually be useful if you're interested. 

Here are some 'features':
- Add/Remove/Edit Banks and Accounts 
- Automatically adds totals so you don't have to do any math 
- Easily view and save graphs of your financial changes over time. 
- Extremely Lightweight

## How To: 

Simply enter the `bankApp` folder and run `python main.py` (**HASN'T BEEN TESTED ON WINDOWS**).

### Help

Since it's a personal app, I didn't include any help or instructions or whatever. However, the 
basic workflow would be something like:

- Upon Initial-Startup 
 - The app has no saved data at this point so you need to create Banks and Accounts
    1. Go to `Banking`
    2. `Edit`
    3. `Add New Bank`
    4. Type the name of the Bank then begin adding accounts 
        - It will ask if the account is a credit line. This is so the backend mathematics of 
        adding up totals will be easier. Essentially, Total should be something like Checking + 
        Savings - Credit. So this determines whether something is added or subtracted to the overall 
        total. 

 - You bank and accounts 'tree' make look something like:
    - Bank1
        - Checking
        - Savings
        - Credit 
    - Bank2
        - Checking
        - Savings
        - Credit 
    - Stocks
        - Robinhood 
    - Cash
        - Person1
        - Person2 
    - Store Cards 
        - Kroger
        - Best Buy
        - Walmart 

- Adding Entries 
 - There are two ways to update values, individually or altogether 
    - To individually update values, you use the Edit command and select the bank, then account that 
    you want to manually update. 
    - Otherwise, simply go to `Banking > Update Info` to be taken to the altogether update. If you 
    want to skip a specific account simply press enter to leave it blank. 

- Viewing Data
 - You can view data in graph or text form.
    - Graph
        - Here, you will select which Banks to view on the graph. From there, you can resize, change the 
        colors, and save the graph. 
    - Data 
        - Here, you simply select which account you want to view and it will show you all of the entries. 

- Saving Changes 
 - The only way to save changes is to select `Quit` on the Main Menu. A keyboard interrupt **will not save 
 changes**. 
