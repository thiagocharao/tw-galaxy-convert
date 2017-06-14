import unittest

from exception import ReadingException
from interpreter import Interpreter


class InterpreterTestCase(unittest.TestCase):

    def setUp(self):
        super(InterpreterTestCase, self).setUp()
        self.interpreter = Interpreter()

    def test_synonym_unit_definition(self):
        self.interpreter.read('glob is V')
        manager = self.interpreter.manager
        self.assertEquals(manager.galaxy_unit.numerals[5]['synonym'], 'glob')

    def test_resource_credit_defnition(self):
        self.interpreter.read('glob is I')
        self.interpreter.read('glob glob Silver is 34 Credits')
        manager = self.interpreter.manager
        self.assertEquals(
            manager.get_or_create_resource('Silver').credits_per_unit * 2,
            34)

    def test_unit_question(self):
        self.interpreter.read('glob is I')
        self.interpreter.read('pish is X')
        self.interpreter.read('tegj is L')
        answer = self.interpreter.read('how much is pish tegj glob glob ?')
        self.assertEqual(answer, 'pish tegj glob glob is 42')

    def test_credits_question(self):
        self.interpreter.read('glob is I')
        self.interpreter.read('prok is V')
        self.interpreter.read('pish is X')
        self.interpreter.read('pish pish Iron is 3910 Credits')
        answer = self.interpreter.read(
            'how many Credits is glob prok Iron ?')
        self.assertEqual(answer, 'glob prok Iron is 782 Credits')

    def test_unreadable_stuff(self):
        with self.assertRaises(ReadingException):
            self.interpreter.read('how much you wanna pay me?')

    def test_conversion_question(self):
        self.interpreter.read('glob is I')
        self.interpreter.read('prok is V')
        self.interpreter.read('glob Silver is 4 Credits')
        self.interpreter.read('glob glob Gold is 15 Credits')
        answer = self.interpreter.read(
            'how many Silver is glob prok Gold ?')
        self.assertEqual(answer, 'glob prok Gold is 7.5 Silver')
