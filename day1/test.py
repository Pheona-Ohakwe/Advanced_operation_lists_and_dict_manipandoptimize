from unittest import TestCase

from whiteboard import solution


class MatchTestCase(TestCase):
    def test_empty(self):
        self.assertEqual(solution(""),"")
    def test_all_lower_case(self):
        self.assertEqual(solution("ready_for_testing"),"readyForTesting")
    def test_pascal(self):
        self.assertEqual(solution("I_Love_Nap_Time"),"ILoveNapTime")
    def test_pythonic(self):
        self.assertEqual(solution("lets_go_team"),"letsGoTeam")