from django.test import TestCase

from ...services.bonus_connection import BonusConnection
from ...services.bonus_programs.program_type import Programs


class BonusConnectionTestCase(TestCase):

    def test_all_programs_in_connection(self):
        for program in Programs:
            BonusConnection(program.name).get_connection()
