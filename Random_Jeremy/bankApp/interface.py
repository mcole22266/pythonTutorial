import inquirer 
from datetime import datetime

import main 

def makeMenu(options:list, message:str):
    print('\n'*100)  # print 100 newlines to "clear screen"
    if message != 'Main Menu':
        options.append('Go Back')
    menu = [
        inquirer.List('selection',
                       message=message,
                       choices=options)]
    selection = inquirer.prompt(menu)['selection']
    return selection

def MainMenu():
    options = ['Banking', 'Quit']
    message = 'Main Menu'
    return makeMenu(options, message)

def BankingMenu():
    options = ['Update Info', 'View', 'Edit']
    message = 'Banking'
    return makeMenu(options, message)

def ViewMenu():
    options = ['Data', 'Graph']
    message = 'View'
    return makeMenu(options, message)

def GraphMenu():
    options = ['Select Data to Graph'] 
    message = 'Graph'
    return makeMenu(options, message)

def DataMenu(finance):
    options = ['Select Data to View'] 
    message = 'Data'
    return makeMenu(options, message) 

def EditMenu(finance):
    options = list(finance.data.keys())
    options.append('Add New Bank')
    options.remove('Total')
    message = 'Edit'
    return makeMenu(options, message) 

def AccountsMenu(finance, bank):
    options = list(finance.data[bank].keys())
    for option in ['Add New Account', 'Remove Bank', 'Edit Bank Name']:
        options.append(option)
    message = bank 
    return makeMenu(options, message) 

def AccountMenu(bank, account):
    options = ['Manually Add Entry', 'Remove Account', 'Edit Account Name']
    message = f'{bank} {account}'
    return makeMenu(options, message) 



def updateInfo(finance):
    print('\n'*100)
    banks = [bank for bank in finance.data.keys() if bank != 'Total']
    for bank in banks:
        print()
        print(f'---- {bank} ---- ')
        accounts = [account for account in finance.data[bank].keys() 
                    if account != 'Total']
        questions = []
        for account in accounts:
            questions.append(inquirer.Text(account, account))
        answers = inquirer.prompt(questions)
        for account,value in answers.items():
            if value != '':
                finance.addEntry(bank, account, round(float(value), 2))
            else:
                pass 
    finance.updateTotals()

def accountSign():
    print('\n'*100)
    options = ['No', 'Yes']
    message = 'Is this a line of credit? (negative value)'
    selection = makeMenu(options, message) 
    if selection == 'Yes':
        return '-'
    else:
        return '+'

def createGraph(finance):
    import matplotlib.pyplot as plt 
    from seaborn import set_style; set_style('whitegrid')

    print('\n'*100)
    print('- Right Arrow to Select\n- Enter to Confirm\n')
    options = list(finance.data.keys())
    questions = [
        inquirer.Checkbox('bankList',
                           message='Select Data to Graph',
                           choices=options),
    ] 
    bankList = inquirer.prompt(questions)['bankList']
    for bank in bankList:
        if bank == 'Total':
            data = finance.data[bank]
        else:
            data = finance.data[bank]['Total']
        x = [entry[0] for entry in data]
        y = [entry[1] for entry in data]
        plt.plot(x, y)
    plt.legend(bankList)
    plt.xlabel('Date'); plt.ylabel('USD')
    plt.title(datetime.now().ctime())
    plt.show()

def showData(finance):
    print('\n'*100)
    options = list(finance.data.keys())
    message = 'Select Data to View'
    bank = makeMenu(options, message)

    if bank != 'Go Back':
        if bank == 'Total':
            data = finance.data['Total'] 
            print('\n'*100)
            print(f'''
    ---- {bank} ----
    ''')
        else:
            print('\n'*100)
            options = list(finance.data[bank].keys())
            message = 'Select Data to View'
            account = makeMenu(options, message)
            if account == 'Go Back':
                return 'Select Data to View'
            elif account == 'Total':
                data = finance.data[bank][account]
            else:
                data = finance.data[bank][account]['entries']
            print('\n'*100)
            print(f'''
    ---- {bank} {account} ----
    ''')

        time = [entry[0].ctime() for entry in data]
        value = [entry[1] for entry in data]

        for time,value in data:
            ctime = time.ctime()
            print(f'{ctime}: ${value}') 
        print()
        done = input('Press Enter when finished')
        return None  