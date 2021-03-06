# Brandon Henson
# 5/20/18
# Lesson 09 mailroom_5.py
# Fixing issues:Refactoring
# Pull Request
# !/usr/bin/env python3


class Donor():
    def __init__(self, name=None):
        self._name = name
        self._donations = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @property
    def donations(self):
        return self._donations

    @donations.setter
    def donations(self, val):
        self._donations = val

    @property
    def total(self):
        return sum(self.donations)


class DonorAll(dict):
    def __init__(self, donors):
        self._donors = donors

    @property
    def donors(self):
        return self._donors

    @donors.setter
    def donors(self, val):
        self._donors = val

    def add_donor(self, donor):
        self.donors[donor.name] = donor.donations

    def donate(self, name, donation):
        if name not in self.donors.keys():
            new_donor = Donor(name)
            self.add_donor(new_donor)
        else:
            self.donors[name].append(int(donation))

    def createfile(self, name):
        for key, values in donor_history.items():
            filename = str(key)+'.txt'
            with open(filename, 'w') as fileobj:
                total = sum(values)
                numgifts = len(values)
                fileobj.write("Dear {}\nThank you for your {} generous donations \
totaling ${}\nThe money will be put to good use.\n\n\
            Sincerely, \n                -The Team".format(key, numgifts, total))
            fileobj.close()

    def menu_2(self):
        try:
            print(f'{"Donor Name":18s} {"|  Total Given":12s} \
    {"|  Num Gifts  |":14s} {"Average Gift":18s}')
            print(f'{"-"*62}')
            [print(f'{name:18s} ${sum(self.donors[name]):10.2f} {len(self.donors[name]):8d}        \
    ${sum(self.donors[name])/len(self.donors[name]):10.2f}')
    for name in self.donors.keys()]
        except ZeroDivisionError:
            pass


def menu_1(donorhistory):
    while True:
        name = input("Enter a full name or 'list' to view all\n")
        if name.lower() == 'list':
            print(donorhistory.donors.keys())
        else:
            break

    success = False
    while not success:
        donation = int(input("Donation amount? \n"))
        try:
            donorhistory.donate(name, donation)
            success = True
        except Exception as e:
            print(e.args[0])
            success = False
    print("Dear {},\nThank you for your generous donation\
 of ${}\nIt will be put to good use.\n\n Sincerely,\n\
                -The Team".format(name, donation))


def report(donorhistory):
    donorhistory.menu_2()


def menu_1_all(donorhistory):
    [donorhistory.createfile(name) for name in donorhistory.donors.keys()]

if __name__ == '__main__':
    donor_history = {}
    donor_history['Brandon Henson'] = [1005.49, 3116.72, 5200]
    donor_history['Alicia Henson'] = [21.47, 1500]
    donor_history['Michael Green'] = [2400.54]
    donor_history['Brandon Henson Jr'] = [355.42, 579.31]
    donor_history['Kaiya Henson'] = [636.9, 850.13, 125.23]

    DonorDict = DonorAll(donor_history)

    response = input('\nSelect an option:\n'
             '[1] Send a Thank You\n'
             '[2] Create a Report\n'
             '[3] Send letters to everyone\n'
             '[4] Exit\n')
    try:
        int(response)
    except:
        while not response.isdigit():
            print("Enter 1,2,3, or 4.")
            print()
            response = input('\nSelect an option:\n'
                             '[1] Send a Thank You\n'
                             '[2] Create a Report\n'
                             '[3] Send letters to everyone\n'
                             '[4] Exit\n')
    arg_dict = {1: menu_1, 2: report, 3: menu_1_all}
    while int(response) != 4:
        try:
            arg_dict.get(int(response))(DonorDict)
        except (TypeError, ValueError):
            print('Enter 1,2,3, or 4')
            print()
            response = input('\nSelect an option:\n'
             '[1] Send a Thank You\n'
             '[2] Create a Report\n'
             '[3] Send letters to everyone\n'
             '[4] Exit\n')
        else:
            response = input('\nSelect an option:\n'
             '[1] Send a Thank You\n'
             '[2] Create a Report\n'
             '[3] Send letters to everyone\n'
             '[4] Exit\n')
