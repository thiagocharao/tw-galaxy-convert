import unittest

from units import GalaxyUnit


class GalaxyUnitTestCase(unittest.TestCase):

    def setUp(self):
        super(GalaxyUnitTestCase, self).setUp()
        self.unit = GalaxyUnit()

    def test_convert_to_roman_numerals(self):
        self.assertEqual(self.unit.to_roman(4999), 'MMMMCMXCIX')
        self.assertEqual(self.unit.to_roman(912), 'CMXII')
        self.assertEqual(self.unit.to_roman(1), 'I')
        self.assertEqual(self.unit.to_roman(3), 'III')
        self.assertEqual(self.unit.to_roman(6), 'VI')

    def test_roman_is_valid(self):
        with self.assertRaises(ValueError):
            self.unit.roman_is_valid('DD')
            self.unit.roman_is_valid('MMMMM')

    def test_convert_to_int(self):
        self.assertEqual(self.unit.to_int('MMMMCMXCIX'), 4999)
        self.assertEqual(self.unit.to_int('CMXII'), 912)
        self.assertEqual(self.unit.to_int('I'), 1)
        self.assertEqual(self.unit.to_int('III'), 3)
        self.assertEqual(self.unit.to_int('VI'), 6)

    def test_set_synonym(self):
        self.unit.set_synonym('glob', 'I')
        self.assertEqual(self.unit.numerals[1]['synonym'], 'glob')

    def test_convert_to_int_using_synonyms(self):
        self.unit.set_synonym('glob', 'I')
        self.unit.set_synonym('prok', 'V')
        self.assertEqual(self.unit.to_int('glob glob glob'), 3)
        self.assertEqual(self.unit.to_int('glob prok'), 4)
        self.assertEqual(self.unit.to_int('prok glob'), 6)

    def test_tw_extension_test_case(self):
        self.unit.set_synonym('hnga', 'C')
        self.unit.set_synonym('mpor', 'D')
        self.unit.set_synonym('atre', 'M')
        self.assertEqual(self.unit.to_int('hnga '), 100)
        self.assertEqual(self.unit.to_int('mpor hnga'), 600)
        self.assertEqual(self.unit.to_int('hnga mpor'), 400)


