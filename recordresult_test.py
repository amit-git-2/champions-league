import unittest
from viewstage import Stages

from recordresult import update_winner

class TestFindWinner(unittest.TestCase):

    def test_aggregates(self):
        g = {
            "winner": "TBD",
            "teams": [
                "ATM",
                "BAR"
            ],
            "L1": {
                "finished": True,
                "result": {
                    "goals": "2-5",
                    "penalties": ""
                }
            },
            "L2": {
                "finished": True,
                "result": {
                    "goals": "6-4",
                    "penalties": ""
                }
            }
        }
        update_winner(g, Stages.QF)
        self.assertEqual(g['winner'], "BAR")
    
    def test_penalties(self):
        g = {
            "winner": "TBD",
            "teams": [
                "NAP",
                "JUV"
            ],
            "L1": {
                "finished": True,
                "result": {
                    "goals": "2-5",
                    "penalties": ""
                }
            },
            "L2": {
                "finished": True,
                "result": {
                    "goals": "5-2",
                    "penalties": "3-4"
                }
            }
        }
        update_winner(g, Stages.SF)
        self.assertEqual(g['winner'], "JUV")


    def test_away_goals(self):
        g = {
            "winner": "TBD",
            "teams": [
                "PSG",
                "BAY"
            ],
            "L1": {
                "finished": True,
                "result": {
                    "goals": "2-5",
                    "penalties": ""
                }
            },
            "L2": {
                "finished": True,
                "result": {
                    "goals": "6-3",
                    "penalties": ""
                }
            }
        }
        update_winner(g, Stages.SF)
        self.assertEqual(g['winner'], "PSG")
    
    def test_penalties(self):
        g = {
            "winner": "TBD",
            "teams": [
                "NAP",
                "JUV"
            ],
            "L1": {
                "finished": True,
                "result": {
                    "goals": "2-5",
                    "penalties": ""
                }
            },
            "L2": {
                "finished": True,
                "result": {
                    "goals": "5-2",
                    "penalties": "3-4"
                }
            }
        }
        update_winner(g, Stages.SF)
        self.assertEqual(g['winner'], "JUV")

    def test_final(self):
        g = {
            "winner": "TBD",
            "teams": [
                "MUN",
                "JUV"
            ],
            "L1": {
                "finished": True,
                "result": {
                    "goals": "4-2",
                    "penalties": ""
                }
            }        
        }
        update_winner(g, Stages.Final)
        self.assertEqual(g['winner'], "MUN")

    def test_final_penalities(self):
        g = {
            "winner": "TBD",
            "teams": [
                "MUN",
                "JUV"
            ],
            "L1": {
                "finished": True,
                "result": {
                    "goals": "2-2",
                    "penalties": "3-4"
                }
            }        
        }
        update_winner(g, Stages.Final)
        self.assertEqual(g['winner'], "JUV")