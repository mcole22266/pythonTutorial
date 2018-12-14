from pprint import pprint 

import objects 
import interface as i 

finance = objects.finances('data.pickle')

def main():
    global finance 

    layer1 = 'Main Menu' 
    layer2 = None 
    layer3 = None 
    layer4 = None
    layer5 = None
    layer6 = None 

    while layer2 != 'Quit':
        if layer1 == 'Main Menu':
            layer2 = i.MainMenu() if layer2 == None else layer2
            if layer2 == 'Banking':
                layer3 = i.BankingMenu() if layer3 == None else layer3
                if layer3 == 'Update Info':
                    i.updateInfo(finance)
                    layer3 = None
                elif layer3 == 'View':
                    finance.updateTotals()
                    layer4 = i.ViewMenu() 
                    if layer4 == 'Graph':
                        layer5 = i.GraphMenu() if layer5 == None else layer5 
                        if layer5 == 'Go Back':
                            layer5 = None 
                            layer4 = None 
                        elif layer5 == 'Select Data to Graph':
                            i.createGraph(finance) 
                            layer5 = None  
                    elif layer4 == 'Data':
                        layer5 = i.DataMenu(finance) if layer5 == None else layer5 
                        if layer5 == 'Go Back':
                            layer5 = None 
                            layer4 = None 
                        elif layer5 == 'Select Data to View':
                            layer5 = i.showData(finance)
                            i.showData(finance)
                            layer5 = None 
                    elif layer4 == 'Go Back':
                        layer4 = None 
                        layer3 = None 
                elif layer3 == 'Edit':
                    layer4 = i.EditMenu(finance) if layer4 == None else layer4
                    if layer4 == 'Add New Bank':
                        print('\n'*100)
                        bankName = input('Bank Name: ')
                        finance.createBank(bankName)
                        layer4 = bankName  # user wants to create accounts now
                    elif layer4 == 'Go Back':
                        layer4 = None 
                        layer3 = None 
                    else:    # Bank Name
                        bank = layer4 
                        layer5 = i.AccountsMenu(finance, bank) if layer5 == None else layer5
                        if layer5 == 'Add New Account':
                            print('\n'*100)
                            accountName = input('Account Name: ')
                            sign = i.accountSign() 
                            finance.createAccount(bank, accountName, sign) 
                            layer5 = None 
                        elif layer5 == 'Remove Bank':
                            finance.removeBank(bank) 
                            layer5 = None 
                            layer4 = None 
                            bank = None
                        elif layer5 == 'Edit Bank Name':
                            print('\n'*100)
                            newName = input(f'Old Name: {bank}\nNew Name: ')
                            finance.renameBank(bank, newName)
                            layer5 = None 
                            layer4 = None
                            bank = newName 
                        elif layer5 == 'Go Back':
                            layer5 = None 
                            layer4 = None 
                            bank = None 
                        else:
                            account = layer5
                            layer6 = i.AccountMenu(bank, account) if layer6 == None else layer6
                            if layer6 == 'Manually Add Entry':
                                value = input('Value: ')
                                finance.addEntry(bank, account, value)
                                layer6 = None 
                            elif layer6 == 'Remove Account':
                                finance.removeAccount(bank, account)
                                layer6 = None 
                                layer5 = None 
                                account = None 
                            elif layer6 == 'Edit Account Name':
                                print('\n'*100)
                                newName = input(f'{bank}\nOld Name: {account}\nNewName: ')
                                finance.renameAccount(bank, account, newName)
                                layer6 = None 
                                layer5 = None 
                                account = newName 
                            elif layer6 == 'Go Back':
                                layer6 = None 
                                layer5 = None 
                                account = None 
                elif layer3 == 'Go Back':
                    layer3 = None
                    layer2 = None 


if __name__ == "__main__":
    main()
    finance.saveDict('data.pickle')
    print('\n'*100)
