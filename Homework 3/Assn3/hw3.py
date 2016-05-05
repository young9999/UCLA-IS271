# Yang Guo


from datetime import datetime
import os
import shutil
import uuid


class Item():

    quote = 'Enjoy!'

    def __init__(self, name):
        self.name = name
        self.uuid = uuid.uuid4().hex

    def __str__(self):
        return 'Item_' + self.name + '_' + self.uuid

    def manifest(self, folder):
        
        pass


class Chips(Item):
    super().__init__(self, name)
    pass


class Candy(Item):
    super().__init__(self, name)
    pass


class Gum(Item):
    super().__init__(self, name)
    pass


class Pastry(Item):
    super().__init__(self, name)
    pass


class Nuts(Item):
    super().__init__(self, name)
    pass


class Dispenser():

    def __init__(self):
        
        pass

    def load(self, item):
        
        pass

    def dispense(self, tray):
        pass

    def empty(self):
        pass


class VendingMachine():

    REPORT_DIR = 'Reports'
    ITEM_TRAY = 'Tray'

    def __init__(self):
        # create dispenser grid
        self.dispensers = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(Dispenser())
            self.dispensers.append(row)
        # create directories for output files
        for folder in [self.REPORT_DIR, self.ITEM_TRAY]:
            # delete it if it exists and recreate it from scratch
            if os.path.exists(folder):
                shutil.rmtree(folder)
            os.mkdir(folder)

    def __del__(self):
        # remove directories when closing
        for folder in [self.REPORT_DIR, self.ITEM_TRAY]:
            if os.path.exists(folder):
                shutil.rmtree(folder)

    def empty(self):
        pass

    def load(self, inventory):
        pass

    def vend(self, row, column):
        pass

    def count_items(self):
        pass

    def report(self):
        output = ''
        for rownum, row in enumerate(self.dispensers):
            for colnum, dispenser in enumerate(row):
                pair = '{}{}'.format(rownum, colnum)
                count = len(dispenser.items)
                output += 'Dispenser {}: {} items\n'.format(pair, count)
                output += '----------------------\n'
                lines = [str(item) for item in dispenser.items]
                output += '\n'.join(lines)
                output += '\n\n\n'
        output += 'Total Item Count: {}'.format(self.count_items())

        timestamp = datetime.now()
        file_name = 'Report_{}.txt'.format(timestamp)
        report_path = os.path.join(self.REPORT_DIR, file_name)
        with open(report_path, 'w') as report_file:
            report_file.write(output)
        return report_path

    def display_options(self):
        pass

    def run(self):
        pass


if __name__ == '__main__':
    vending_machine = VendingMachine()
    vending_machine.run()
