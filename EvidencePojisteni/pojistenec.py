class Pojistenec:

    def __init__(self, jmeno, prijmeni, vek, telefonni_cislo):
        """
        Konstruktor pro vytvoření instance třídy Uživatel,
        povinné parametry jsou jméno, příjmení, věk, telefonní číslo.
        """
        self._jmeno = jmeno
        self._prijmeni = prijmeni
        self._vek = vek
        self._telefonni_cislo = telefonni_cislo

    def __str__(self):
        """
        Vrací textovou reprezentaci objektu.
        """
        return str("{} {},\nvěk: {}\nKontakt: {}".format(self._jmeno, self._prijmeni, self._vek, self._telefonni_cislo))
