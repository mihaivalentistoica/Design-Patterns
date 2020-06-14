"""
Firma ACME Inc dezvolta o soluție software pentru o banca având in vedere
următoarele specificații. Toate instanțele aplicației folosesc un unic obiect care are
rolul de a gestiona datele băncii (denumire, adresa, contor număr curent cont) dar si
de a genera unul din cele 2 tipuri diferite de conturi pe care banca le administrează
(Cont de Credit si Cont de Debit). Generarea conturilor se face in funcție de tipul
contului, transmis printr-un parametru de tip string. Cele doua conturi ale băncii
implementează interfața ContBancar ce definește 2 metode obligatorii:
transfer(ContBancar destinație, float suma) si depune(float suma).
In momentul de fata, banca se afla in discuții privind o eventuala fuziune cu o alta
banca. Un criteriu al fuziunii este interconectarea celor 2 sisteme informatice astfel
încât operațiunile bancare (transfer si depunere) sa se poată desfășura prin aplicațiile
celor 2 bănci. Firma ACME Inc trebuie sa ofere o soluție de proba, având in vedere ca
in banca partenera conturile implementează interfața BankAccount ce definește
metoda accountTransfer(BankAccount account, float amount). Să se identifice cele
3 pattern-uri care corespund problemelor prezentate și care oferă soluțiile optime. Pe
baza lor să se implementeze soluția
"""


class ContBancar:
    def transfer(self, destinatie, suma):
        raise NotImplementedError

    def depunere(self, suma):
        raise NotImplementedError


class ContBancarPartener:
    def accountTransfer(self, account, amount):
        raise NotImplementedError


class ContDebit(ContBancar):
    def __init__(self, detinator, balance=0):
        self.__detinator = detinator
        self.__balance = balance

    def transfer(self, destinatie, suma):
        if suma > 0 and suma < self.__balance:
            destinatie.depunere(suma)
            self.__balance -= suma
        else:
            print("Invalid transfer amount")

    def depunere(self, suma):
        if (suma > 0):
            self.__balance += suma
        else:
            print('Invalid amount')

    def __str__(self):
        return f'Contul lui {self.__detinator} are {self.__balance} lei'


class ContCredit(ContBancar):
    def __init__(self, detinator, balance=0):
        self.__detinator = detinator
        self.__balance = balance

    def transfer(self, destinatie, suma):
        if suma > 0 and suma < self.__balance:
            destinatie.depunere(suma)
            self.__balance -= suma
        else:
            print("Invalid transfer amount")

    def depunere(self, suma):
        if (suma > 0):
            self.__balance += suma
        else:
            print('Invalid amount')

    def __str__(self):
        return f'Contul lui {self.__detinator} are {self.__balance} lei'


class ContPartener(ContBancarPartener):
    def __init__(self, detinator, balance=0):
        self.__detinator = detinator
        self.__balance = balance

    def accountTransfer(self, account: ContBancarPartener, amount):
        self.__balance += amount

    def __str__(self):
        return f'Contul lui {self.__detinator} are {self.__balance} lei'


class AdapterAcount(ContBancar, ContPartener):
    def transfer(self, destinatie, suma):
        return self.accountTransfer(destinatie, -abs(suma))

    def depunere(self, suma):
        return self.accountTransfer(self, abs(suma))


class Bank:
    _instance = None
    __tipuri_cont = {'debit': ContDebit, 'credit': ContCredit}

    def __init__(self, name, address):
        self.__name = name
        self.__address = address
        self.__counter_account = 0

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)

        return cls._instance

    def creareCont(self, tip, detinator, balnace=0):
        return self.__tipuri_cont[tip](detinator, balnace)


banca = Bank('Banca Taraneasca I.C.', "Splaiul Uniri, nr 213")

cont_debit = banca.creareCont('debit', 'Ion')
cont_credit = banca.creareCont('credit', 'Popescu', 1000)
cont_partener = ContPartener('Raicu', 2134)

adaptor = AdapterAcount(cont_partener)

cont_debit.depunere(1230)
print("Contul de debit a fost alimentat: ", str(cont_debit))
cont_credit.transfer(cont_debit, 500)
print("Transfer din: ", str(cont_credit), " in: ", str(cont_debit))

adaptor.transfer(cont_debit, 130)
print("Transfer din: ", str(cont_partener), " in: ", str(cont_debit))
