from pojistenec import Pojistenec


class Databaze:
    dalsi_uzivatel = 1
    volba = 0

    def __init__(self):
        """
        Konstruktor pro vytvoření evidence pojištěných.
        """
        self.evidence = []

    def zvol_operaci(self):
        """
        Vrací číselnou hodnotu, která spustí další operaci dle nabídky dostupných akcí.
        """
        while self.volba != 4:
            try:
                print("Dostupné akce: "
                      "\n 1 - Přidat nového pojištěnce "
                      "\n 2 - Zobrazit seznam všech pojištěnců "
                      "\n 3 - Vyhledat pojištěnce "
                      "\n 4 - Konec\n")
                self.volba = int(input("Zvolte číslo operace: \n"))
                if self.volba == 1:
                    return self.pridej_pojistence()
                elif self.volba == 2:
                    self.zobraz_seznam()
                elif self.volba == 3:
                    self.hledej_uzivatele()
                elif self.volba == 4:
                    print("\nDěkujeme za použití programu.")
                else:
                    print("\nDostupné operace: 1 - 4\n")
            except ValueError:
                print("\nZadejte platnou operaci!\n")

    def nacti_vek(self, text_zadani, text_chyba):
        """
        :param text_zadani: Text vyzve uživatele k zadání hodnoty.
        :param text_chyba: Zobrazí se v případě výjimky ValueError.
        :return: Vrací číselnou hodnotu věk v rozmezí 0-120.
        """
        spatne_zadani = True
        while spatne_zadani:
            try:
                zadany_vek = int(input(text_zadani))
                if zadany_vek < 0 or zadany_vek > 120:
                    print("\nZadané číslo musí být v rozmezí 0 - 120!\n")
                    continue
                spatne_zadani = False
            except ValueError:
                print(text_chyba)
            else:
                return zadany_vek

    def nacti_telefon(self, text_zadani, text_chyba):
        """
        :param text_zadani: Text vyzve uživatele k zadání hodnoty.
        :param text_chyba: Zobrazí se v případě výjimky ValueError.
        :return: Vrací devíticifernou číselnou hodnotu pro telefonní číslo.
        """
        spatne_zadani = True
        while spatne_zadani:
            try:
                zadane_cislo = int(input(text_zadani))
                if len(str(zadane_cislo)) != 9:
                    print("\nZadejte platný počet znaků (9).\n")
                    continue
                spatne_zadani = False
            except ValueError:
                print(text_chyba)
            else:
                return zadane_cislo

    def nacti_text(self, text_zadani, text_chyba):
        """
        :param text_zadani: Text vyzve uživatele k zadání hodnoty.
        :param text_chyba: Zobrazí se v případě zadání jiné hodnoty než alfabetických znaků.
        :return: Vrací textovou hodnotu v rozmezí 2-25 znaků.
        """
        spatne_zadani = True
        while spatne_zadani:
            zadany_text = str(input(text_zadani))
            if len(str(zadany_text)) < 2 or len(str(zadany_text)) > 25:
                print("\nZadejte platný počet znaků (2 - 25).\n")
            elif zadany_text.isalpha() != True:
                print(text_chyba)
            else:
                return zadany_text

    def pridej_pojistence(self):
        """
        Funkce přidá uživatele do evidence pojištěných.
        Parametry jsou jméno, příjmení, věk, telefonní číslo.
        :return:
        """

        jmeno = self.nacti_text("Zadejte jméno nového uživatele: ",
                                "\nZadávejte pouze alfabetické znaky.\n").capitalize()
        prijmeni = self.nacti_text("Zadejte příjmení nového uživatele: ",
                                   "\nZadávejte pouze alfabetické znaky.\n").capitalize()
        vek = self.nacti_vek("Zadejte věk uživatele:", "Zadávejte pouze numerické znaky.")
        telefonni_cislo = self.nacti_telefon("Zadejte telefonní číslo uživatele ve formátu XXXXXXXXX:",
                                             "\nZadávejte pouze numerické znaky.\n")

        self.evidence.append(Pojistenec(jmeno, prijmeni, vek, telefonni_cislo))
        self.dalsi_uzivatel += 1
        zprava = input("\nUživatel byl uložen do databáze.\nPokračujte libovolnou klávesou...\n")
        self.nastav_zpravu(zprava)

        self.zvol_operaci()

    def zobraz_seznam(self):
        """
        Vrací aktuální výpis všech uživatelů v evidenci a jejich součet.
        """
        print("Seznam všech uživatelů:\n")
        for pojisteny in self.evidence:
            print(str("{} {} - Věk: {}, Kontakt: {}".format
                      (pojisteny._jmeno, pojisteny._prijmeni, pojisteny._vek, pojisteny._telefonni_cislo)))
        print("Počet uživatelů v databázi: {}".format(self.dalsi_uzivatel - 1))
        if len(self.evidence) < 1:
            print("Databáze neobsahuje žádné uživatele.")
        zprava = input("\nPokračujte libovolnou klávesou...")
        self.nastav_zpravu(zprava)
        self.zvol_operaci()

    def hledej_uzivatele(self):
        """
        Vrací uživatele ze seznamu dle zadaných parametrů (jméno + příjmení).
        """

        jmeno = str(input("Zadejte jméno hledaného uživatele: \n").capitalize())
        prijmeni = str(input("Zadejte příjmení hledaného uživatele: \n").capitalize())
        hledani_uzivatele = [uzivatel for uzivatel in self.evidence if
                             uzivatel._jmeno == jmeno
                             and uzivatel._prijmeni == prijmeni]
        for uzivatel in hledani_uzivatele:
                print("\nVýsledek hledání:")
                print(str("{} {} - Věk: {}, Kontakt: {}\n".format(uzivatel._jmeno, uzivatel._prijmeni,
                                                            uzivatel._vek, uzivatel._telefonni_cislo)))
        if len(hledani_uzivatele) < 1:
            print("\nUživatel nenalezen\n.")

    def nastav_zpravu(self, zprava):
        print(zprava)
