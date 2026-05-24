from .api import BaseAPI
from datetime import datetime


class BankruptsAPI(BaseAPI):

    def __init__(self, url):
        super().__init__(url)
        self.url = f'{url}/v1/bankrupts'

    def execute(self, ses, **kwargs):
        self._prepare_params(**kwargs)
        response = ses.request(method='get', url=self.url, params=self.params, verify=False)
        result = response.json() if response.status_code == 200 else response
        return result


class Bankrupt:

    def __init__(self, data=None):
        self.guid = None
        self.type = None
        self.data = data
        self.name = None
        self.ogrn = None
        self.inn = None
        self.address = None
        self.first_name = None
        self.last_name = None
        self.middle_name = None
        self.inn = None
        self.snils = None
        self.birthplace = None
        self.birthdate = None
        self.name_history = None
        self.init_data()

    def init_data(self):
        if self.data is not None:
            self.guid = self.data.get('guid')
            self.type = self.data.get('type')
            match self.type:
                case "Company": self.__class__ = BankruptLegal
                case "Person": self.__class__ = BankruptPerson
            self.data = self.data.get('data')
            self.init_data()


class BankruptLegal(Bankrupt):

    def __init__(self, data):
        super().__init__(data)

    def __str__(self):
        return (f'<    {self.name}    >\n'
                f'  ИНН:             {self.inn}\n'
                f'  ОГРН:            {self.ogrn}\n'
                f'  адрес:           {self.address} \n'
                )

    def init_data(self):
        if self.data is not None:
            self.name = self.data.get('name')
            self.ogrn = self.data.get('ogrn')
            self.inn = self.data.get('inn')
            self.address = self.data.get('address')


class BankruptPerson(Bankrupt):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return (f'<    {self.last_name} {self.first_name} {self.middle_name}    >\n'
                f'  ИНН:             {self.inn if self.inn is not None else '-' }\n'
                f'  СНИЛС:           {self.snils if self.snils is not None else '-' }\n'
                f'  дата рождения:   {self.birthdate.strftime("%d.%m.%Y")}\n'
                f'  место рождения:  {self.birthplace}\n'
                f'  адрес:           {self.address} \n'
                )


    def init_data(self):
        if self.data is not None:
            self.first_name = self.data.get('firstName')
            self.last_name = self.data.get('lastName')
            self.middle_name = self.data.get('middleName')
            self.inn = self.data.get('inn')
            self.snils = self.data.get('snils')
            self.birthplace = self.data.get('birthplace')
            self.birthdate = datetime.strptime(self.data.get('birthdate')[0:10], '%Y-%m-%d')
            self.address = self.data.get('address')
            self.name_history = self.data.get('nameHistory')
