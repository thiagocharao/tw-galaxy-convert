
INVALID_ROMANS = ['MMMMM', 'DD', 'CCCC', 'IIII', 'LL', 'XXXX', 'VV']


class GalaxyUnit(object):
    """Representation of a Galaxy base Unit

    Attributes:
        numerals (dict): Holds a set of Roman numerals, values and its synonyms.
                         A synonym is an abstraction to make possible to other
                         planets to make deals here.
    """
    def __init__(self):
        self.numerals = dict()
        self.numerals[1] = {'synonym': None, 'symbol': 'I'}
        self.numerals[4] = {'synonym': None, 'symbol': 'IV'}
        self.numerals[5] = {'synonym': None, 'symbol': 'V'}
        self.numerals[9] = {'synonym': None, 'symbol': 'IX'}
        self.numerals[10] = {'synonym': None, 'symbol': 'X'}
        self.numerals[50] = {'synonym': None, 'symbol': 'L'}
        self.numerals[40] = {'synonym': None, 'symbol': 'XL'}
        self.numerals[90] = {'synonym': None, 'symbol': 'XC'}
        self.numerals[100] = {'synonym': None, 'symbol': 'C'}
        self.numerals[400] = {'synonym': None, 'symbol': 'CD'}
        self.numerals[900] = {'synonym': None, 'symbol': 'CM'}
        self.numerals[500] = {'synonym': None, 'symbol': 'D'}
        self.numerals[1000] = {'synonym': None, 'symbol': 'M'}

    def to_roman(self, number):
        """Converts a number into roman numerals

        Args:
            number (int): Number to be converted.

        Returns:
            A string with the numbers representation
        """
        def rep_and_rest(number):
            for value in reversed(sorted(self.numerals.keys())):
                info = self.numerals[value]
                quotient = number // value
                if quotient > 0:
                    rest = number - (value * quotient)
                    rep = quotient * info['symbol']
                    return rep, rest

        result = ''
        while number > 0:
            rep, number = rep_and_rest(number)
            result += rep

        return result

    def to_int(self, roman):
        """Converts a set of roman numerals (or synonyms) into integer

        Args:
            roman (str): Set of roman symbols.

        Returns:
            The number! o/
        """
        roman = self.roman_is_valid(roman)
        symbols_dict = {self.numerals[i]['symbol']: i for i in self.numerals}
        roman = self.convert_synonyms(roman)
        doubles_first = ['CM', 'CD', 'XC', 'XL', 'IX', 'IV',
                         'M', 'D', 'C', 'L', 'X', 'V', 'I']
        for symbol in doubles_first:
            if symbol in roman:
                roman = roman.replace(
                    symbol, ' {}'.format(symbols_dict[symbol]))
        return sum(int(num) for num in roman.split())

    def roman_is_valid(self, roman):
        """Validates a set of roman numerals (or synonyms)

        Args:
            roman (str): Set of roman symbols.

        Returns:
            True if valid otherwise False
        """
        if any(invalid in roman.upper() for invalid in INVALID_ROMANS):
            raise ValueError('I can\'t understand: {}'.format(roman))
        return roman

    def set_synonym(self, synonym, roman):
        """Defines a synonym to a roman symbol

        Args:
            synonym (str): Synonym string to be used
            roman (str): A single roman symble.
        """
        for numeral in self.numerals:
            if self.numerals[numeral]['symbol'] == roman:
                self.numerals[numeral]['synonym'] = synonym

    def convert_synonyms(self, string):
        """Converts a set of synonyms into roman numerals

        Args:
            string (str): String with synonyms.

        Returns:
            Hopefully a beatiful cleaned roman set of symbols.
        """
        for i in self.numerals:
            synomym = self.numerals[i]['synonym']
            if synomym and synomym in string:
                string = string.replace(
                    self.numerals[i]['synonym'], ' {}'.format(
                        self.numerals[i]['symbol']))
        return ''.join(string.split())
