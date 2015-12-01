# This file is part of the stock_move_editable_list module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class StockMoveEditableListTestCase(ModuleTestCase):
    'Test Stock Move Editable List module'
    module = 'stock_move_editable_list'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        StockMoveEditableListTestCase))
    return suite