import unittest
from src.fedresurs.ibp import InterfaxBankruptcyPublications
from src.fedresurs.ibp.bankrupts import Bankrupt
from src.fedresurs.ibp.messages import Message


class TestMessages(unittest.TestCase):

    def test_bankrupts(self):
        with InterfaxBankruptcyPublications() as ipb:
            j = ipb.messages(datePublishBegin='gte:2024-02-01', datePublishEnd='lte:2024-03-01', offset=0, limit=50)
            assert j['total'] > 0
            j = j['pageData']
            for i in j:
                i1 = ipb.bankrupts(guid=i['bankruptGuid'], offset=0, limit=50)
                i2 = i1['pageData'][0]
                b1 = Bankrupt(i2)
                print(b1)
                # print(b1.birthdate)

    def test_messages(self):
        with InterfaxBankruptcyPublications() as ipb:
            j = ipb.messages(datePublishBegin='gte:2024-03-01', datePublishEnd='lte:2024-03-27', offset=0, limit=50)
            assert j['total'] > 0
            j = j['pageData']
            for i in j:
                i1 = ipb.message(guid=i['guid'])
                # print(i1['content'])
                m1 = Message(i1)
                print(m1.bankrupt_guid)
                i2 = ipb.bankrupts(guid=m1.bankrupt_guid, offset=0, limit=1)
                print(Bankrupt(i2['pageData'][0]))
                print(m1.number)
                print(m1.type)
                print(m1.bankruptcy_case_number)
                print(m1.publisher)
                print(m1.message_info)
                print(m1.text)
                # mt1 = m1.content.get('MessageData').get('MessageInfo').get('@MessageType')
                # print(m1.content.get('MessageData').get('MessageInfo').get(mt1).get('Text'))
                print('\n---\n')

            # j2 = ipb.message(j['pageData'][0]['guid'])
            # j3 = ipb.bankrupts(guid=j2['bankruptGuid'], offset=0, limit=50)
            # assert j3['total'] > 0
            # print(j3)

    def test_trade_messages(self):
        with InterfaxBankruptcyPublications() as ipb:
            j = ipb.trade_messages(datePublishBegin='gte:2024-02-01', datePublishEnd='lte:2024-02-27', offset=0, limit=50)
            assert j['total'] > 0
            j2 = ipb.trade_message(j['pageData'][0]['guid'])
            j3 = ipb.bankrupts(guid=j2['tradePlaceGuid'], offset=0, limit=50)
            # assert j3['total'] > 0
            print(j2)
            print(j3)


if __name__ == "__main__":
    unittest.main()
