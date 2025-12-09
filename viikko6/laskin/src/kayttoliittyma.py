from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4

class Komentotehdas:
    def __init__(self, sovelluslogiikka, io):

        self.komennot = {
            "summa": Summa(sovelluslogiikka, io),
            "erotus": Erotus(sovelluslogiikka, io),
            "nollaus": Nollaus(sovelluslogiikka, io),
            "kumoa": Kumoa(sovelluslogiikka, io)
        }

    def hae(self, komento):
        return self.komennot.get(komento, Tuntematon())

class GuiIO:
    def __init__(self, syote_kentta):
        self._syote_kentta = syote_kentta

    def lue_luku(self):
        try:
            return int(self._syote_kentta.get())
        except ValueError:
            return 0

class Summa:
    def __init__(self, sovelluslogiikka, io):
        self._logiikka = sovelluslogiikka
        self._io = io

    def suorita(self):
        arvo = self._io.lue_luku()
        self._logiikka.plus(arvo)

class Erotus:
    def __init__(self, sovelluslogiikka, io):
        self._logiikka = sovelluslogiikka
        self._io = io

    def suorita(self):
        arvo = self._io.lue_luku()
        self._logiikka.miinus(arvo)

class Nollaus:
    def __init__(self, sovelluslogiikka, io=None):
        self._logiikka = sovelluslogiikka

    def suorita(self):
        self._logiikka.nollaa()

class Kumoa:
    def __init__(self, sovelluslogiikka, io= None):
        self._logiikka = sovelluslogiikka

    def suorita(self):
        self._logiikka.kumoa()

class Tuntematon:
    def suorita(self):
        print("Tuntematon komento")



class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._logiikka = sovelluslogiikka
        self._root = root

    def kaynnista(self):
        self._arvo_var = StringVar()
        self._arvo_var.set(self._logiikka.arvo())

        self._syote_kentta = ttk.Entry(master=self._root)
        self._io = GuiIO(self._syote_kentta)

        self._komentotehdas = Komentotehdas(self._logiikka, self._io)

        ttk.Label(textvariable=self._arvo_var).grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento("summa")
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento("erotus")
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento("nollaus")
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento("kumoa")
        )
        
        tulos_teksti = ttk.Label(master=self._root, textvariable=self._arvo_var)
        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _suorita_komento(self, komento_nimi):
        komento = self._komentotehdas.hae(komento_nimi)
        komento.suorita()

        self._arvo_var.set(self._logiikka.arvo())
        self._syote_kentta.delete(0, constants.END)

        self._kumoa_painike["state"] = constants.NORMAL
        self._nollaus_painike["state"] = constants.NORMAL if self._logiikka.arvo() != 0 else constants.DISABLED
