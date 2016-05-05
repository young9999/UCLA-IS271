import os
import unittest

from hw3 import *


class TestItemProperties(unittest.TestCase):

    def setUp(self):
        self.item = Item("Generic Snack")

    def test_init(self):
        self.assertEqual(self.item.name, "Generic Snack")

    def test_class_quote(self):
        self.assertEqual(self.item.quote, "Enjoy!")

    def test_manifest(self):
        self.item.manifest('')
        filename = 'Item_%s_%s' % (self.item.name, self.item.uuid)
        self.assertTrue(os.path.exists(filename))
        try:
            with open(filename, 'r') as item_file:
                contents = item_file.read()
                self.assertEqual(contents, 'Enjoy!')
            os.remove('Item_%s_%s' % (self.item.name, self.item.uuid))
        except:
            pass


class TestItemSubclasses(unittest.TestCase):

    def setUp(self):
        self.subclasses = [
            (Chips, "I'm a salty snack"),
            (Candy, "I rot your teeth"),
            (Gum, "I freshen your breath"),
            (Pastry, "I make you fat"),
            (Nuts, "I'm a nutritious source of protein")
        ]
        self.items = []
        for num, pair in enumerate(self.subclasses):
            cls = pair[0]
            name = 'item%s' % num
            item = cls(name)
            self.items.append(item)

    def test_subclass_manifests(self):
        for num, item in enumerate(self.items):
            item.manifest('')
            filename = str(item)
            self.assertTrue(os.path.exists(filename))
            with open(filename, 'r') as item_file:
                contents = item_file.read()
                classname = str(self.subclasses[num][0])[12:-2]
                quote = self.subclasses[num][1]
                self.assertEqual(contents, quote)
            os.remove('%s_%s_%s' % (classname, item.name, item.uuid))


class TestDispenser(unittest.TestCase):

    def setUp(self):
        self.dispenser = Dispenser()

    def test_load_and_dispense(self):
        ids = []
        # first load it up
        for num in range(10):
            item = Item('item%s' % num)
            ids.append(item.uuid)
            self.dispenser.load(item)
            self.assertEqual(len(self.dispenser.items), num+1)
        # now pop one off and check it
        loaded_ids = [item.uuid for item in self.dispenser.items]
        self.assertEqual(loaded_ids, ids[::-1])
        self.dispenser.dispense('')
        self.assertEqual(len(self.dispenser.items), 9)
        filename = 'Item_item9_%s' % loaded_ids[0]
        self.assertTrue(os.path.exists(filename))
        os.remove(filename)

    def test_empty(self):
        for num in range(10):
            item = Item('item%s' % num)
            self.dispenser.load(item)
        self.assertEqual(len(self.dispenser.items), 10)
        self.dispenser.empty()
        self.assertEqual(len(self.dispenser.items), 0)

class TestVendingMachine(unittest.TestCase):

    def setUp(self):
        self.vendmac = VendingMachine()

    def test_matrix(self):
        self.assertEqual(len(self.vendmac.dispensers), 3)
        for num in range(3):
            self.assertEqual(len(self.vendmac.dispensers[num]), 3)

    def test_load(self):
        self.vendmac.load('test-inventory.txt')
        self.assertEqual(self.vendmac.count_items(), 90)

    def test_vend(self):
        self.vendmac.load('test-inventory.txt')
        self.assertEqual(self.vendmac.count_items(), 90)
        str1 = self.vendmac.vend(0,0)
        str2 = self.vendmac.vend(1,2)
        str3 = self.vendmac.vend(2,1)
        self.assertEqual(self.vendmac.count_items(), 87)

        d00items = self.vendmac.dispensers[0][0].items
        self.assertEqual(len(d00items), 9)
        self.assertTrue(os.path.exists(str1))
        os.remove(str1)
        
        d12items = self.vendmac.dispensers[1][2].items
        self.assertEqual(len(d12items), 9)
        self.assertTrue(os.path.exists(str2))
        os.remove(str2)
        
        d21items = self.vendmac.dispensers[2][1].items
        self.assertEqual(len(d21items), 9)
        self.assertTrue(os.path.exists(str3))
        os.remove(str3)

    def test_empty(self):
        self.vendmac.load('test-inventory.txt')
        self.assertEqual(self.vendmac.count_items(), 90)
        # run it a second time and check that it dumped the old items
        self.vendmac.load('test-inventory.txt')
        self.assertEqual(self.vendmac.count_items(), 90)

    def test_report(self):
        self.vendmac.load('test-inventory.txt')
        report_path = self.vendmac.report()
        with open(report_path, 'r') as report_file:
            with open('test-report_full.txt', 'r') as test_file:
                self.assertEqual(len(report_file.readlines()),
                    len(test_file.readlines()))
        pairs = [(0,0), (2,1), (2,0), (0,2)]
        for pair in pairs:
            self.vendmac.vend(pair[0], pair[1])
        report_path = self.vendmac.report()
        with open(report_path, 'r') as report_file:
            with open('test-report_partial.txt', 'r') as test_file:
                self.assertEqual(len(report_file.readlines()),
                    len(test_file.readlines()))


if __name__ == '__main__':
    unittest.main()