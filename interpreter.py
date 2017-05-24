import re

from exception import ReadingException
from services import ResourceManager

SENTENCE_PATTERNS = {
    'synonym_unit_definition': r'(?P<galaxy_unit>[a-z]*) is (?P<corresponds_to>[M, D, C, L, X, V, I])',  # NOQA
    'resource_credit_defnition': r'(?P<galaxy_units>[a-z, ]*) (?P<resource>[A-Z][a-z]*) is (?P<credits>[0-9]*) Credits',  # NOQA
    'unit_question': r'how much is (?P<galaxy_units>[a-z, ]*) ?',
    'credits_question': r'how many Credits is (?P<galaxy_units>[a-z, ]*) (?P<resource>[A-Z][a-z]*) ?'  # NOQA
}


class Interpreter(object):
    """Interpreter class responsible for dealing with user's questions and actions

    Attributes:
        manager (ResourceManager): Instance of Resource Manager.
    """
    def __init__(self):
        super(Interpreter, self).__init__()
        self.manager = ResourceManager()

    def read(self, string):
        """Interprets a string matching to a known sentence.

        Args:
            string: string to be interpreted.

        Returns:
            Returns a well formed answer.

        Raises:
            ReadingException if no match found.
        """
        for key in SENTENCE_PATTERNS:
            match = re.search(SENTENCE_PATTERNS[key], string)
            if match:
                return self.answer(key, match.groupdict())

        raise ReadingException()

    def answer(self, key, data):
        """Formats a suitable answer depending on the the given parameters

        Args:
            key: Action/Question key
            data: Data to be used to answer a question or take an action

        Returns:
            Returns a well formed answer, if applicable.
        """
        if key == 'unit_question':
            answer = '{0} is {1}'
            units = self.manager.galaxy_unit.to_int(data['galaxy_units'])
            return answer.format(data['galaxy_units'].strip(), units)

        elif key == 'credits_question':
            answer = '{0} {1} is {2} Credits'
            credits = self.manager.get_resource_worth_in_credits(
                data['galaxy_units'], data['resource'])
            return answer.format(data['galaxy_units'], data['resource'], credits)

        elif key == 'synonym_unit_definition':
            return self.manager.galaxy_unit.set_synonym(
                data['galaxy_unit'], data['corresponds_to'])

        elif key == 'resource_credit_defnition':
            return self.manager.set_resource_credits(
                data['credits'], data['galaxy_units'], data['resource'])
