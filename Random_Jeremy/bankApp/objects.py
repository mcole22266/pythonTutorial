import pickle
from datetime import datetime


class finances:  # TODO: is doing that weird data.data.data thing
    def __init__(self, dataFile='data.pickle'):
        try:
            self.data = self.loadDict(dataFile)
        except:
            self.data = {'Total': []}

    def loadDict(self, filename):
        with open(filename, 'rb') as f:
            data = pickle.load(f)
        return data

    def saveDict(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.data, file, protocol=pickle.HIGHEST_PROTOCOL)

    def createBank(self, bankName):
        self.data[bankName] = {}

    def createAccount(self, bankName, accountName, sign='+'):
        self.data[bankName][accountName] = {'sign': sign,
                                            'entries': []}

    def removeBank(self, bankName):
        self.data.pop(bankName)

    def removeAccount(self, bankName, accountName):
        self.data[bankName].pop(accountName)

    def renameBank(self, bankName, newName):
        self.data[newName] = self.data[bankName]
        self.data.pop(bankName)

    def renameAccount(self, bankName, accountName, newName):
        self.data[bankName][newName] = self.data[bankName][accountName]
        self.data[bankName].pop(accountName)

    def addEntry(self, bankName, accountName, value):
        date = datetime.now()
        value = round(float(value), 2)
        self.data[bankName][accountName]['entries'].append((date, value))

    def updateTotals(self):
        date = datetime.now()
        total = 0
        if 'Total' not in self.data.keys():
            self.data['Total'] = [] 
        for bank in self.data.keys():
            if bank == 'Total':  # Skip Total Category
                continue
            if 'Total' not in self.data[bank].keys():
                self.data[bank]['Total'] = []
            bankTotal = 0
            for account in self.data[bank].keys():
                if account == 'Total':   # Skip Total Category
                    continue
                accountTotal = 0
                if self.data[bank][account]['sign'] == '+':
                         # add value
                    accountTotal += self.data[bank][account]['entries'][-1][-1]
                elif self.data[bank][account]['sign'] == '-':
                         # subtract value
                    accountTotal -= self.data[bank][account]['entries'][-1][-1]
                bankTotal += accountTotal        # add account totals to bank total
            self.data[bank]['Total'].append((date, bankTotal))  # add Total entry to bank 
            total += bankTotal                    # add bank totals to overall total 
        self.data['Total'].append((date, total))
