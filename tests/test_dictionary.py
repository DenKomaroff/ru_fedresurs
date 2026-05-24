import unittest
from src.fedresurs.ibp import InterfaxBankruptcyPublications
from src.fedresurs.ibp.bankrupts import Bankrupt


class TestDictionary(unittest.TestCase):

    def test_message_types(self):
        with InterfaxBankruptcyPublications() as ipb:
            j = ipb.message_types()
            assert len(j) > 0
            for i in j:
                print(i)
                # print(f"case '{i.get('code')}': self.__class__ = Message")

    def test_court_decision_types(self):
        with InterfaxBankruptcyPublications() as ipb:
            j = ipb.court_decision_types()
            assert len(j) > 0
            for i in j:
                print(i)


if __name__ == "__main__":
    unittest.main()
