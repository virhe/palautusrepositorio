KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("kapasiteetti2")  # heitin vaan jotain :D

        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko

        self.lukujono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, numero):
        return numero in self.lukujono

    def lisaa(self, numero):
        if self.kuuluu(numero):
            return False

        if self.alkioiden_lkm == 0:
            self.lukujono[0] = numero
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            return True

        self.lukujono[self.alkioiden_lkm] = numero
        self.alkioiden_lkm = self.alkioiden_lkm + 1

        # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
        if self.alkioiden_lkm % len(self.lukujono) == 0:
            taulukko_old = self.lukujono
            self.kopioi_lista(self.lukujono, taulukko_old)
            self.lukujono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
            self.kopioi_lista(taulukko_old, self.lukujono)

        return True


    def poista(self, numero):
        kohta = -1
        apu = 0

        for indeksi in range(0, self.alkioiden_lkm):
            if numero == self.lukujono[indeksi]:
                kohta = indeksi  # siis luku löytyy tuosta kohdasta :D
                self.lukujono[kohta] = 0
                break

        if kohta != -1:
            for indeksi2 in range(kohta, self.alkioiden_lkm - 1):
                apu = self.lukujono[indeksi2]
                self.lukujono[indeksi2] = self.lukujono[indeksi2 + 1]
                self.lukujono[indeksi2 + 1] = apu

            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True

        return False

    def kopioi_lista(self, alkuperainen, kopio):
        for indeksi in range(0, len(alkuperainen)):
            kopio[indeksi] = alkuperainen[indeksi]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for indeksi in range(0, len(taulu)):
            taulu[indeksi] = self.lukujono[indeksi]

        return taulu

    @staticmethod
    def yhdiste(alkuperainen, kopio):
        x = IntJoukko()
        alkuperainen_taulu = alkuperainen.to_int_list()
        kopio_taulu = kopio.to_int_list()

        for indeksi in range(0, len(alkuperainen_taulu)):
            x.lisaa(alkuperainen_taulu[indeksi])

        for indeksi in range(0, len(kopio_taulu)):
            x.lisaa(kopio_taulu[indeksi])

        return x

    @staticmethod
    def leikkaus(alkuperainen, kopio):
        y = IntJoukko()
        alkuperainen_taulu = alkuperainen.to_int_list()
        kopio_taulu = kopio.to_int_list()

        for indeksi in range(0, len(alkuperainen_taulu)):
            for indeksi2 in range(0, len(kopio_taulu)):
                if alkuperainen_taulu[indeksi] == kopio_taulu[indeksi2]:
                    y.lisaa(kopio_taulu[indeksi2])

        return y

    @staticmethod
    def erotus(alkuperainen, kopio):
        intjoukko = IntJoukko()
        alkuperainen_taulu = alkuperainen.to_int_list()
        kopio_taulu = kopio.to_int_list()

        for indeksi in range(0, len(alkuperainen_taulu)):
            intjoukko.lisaa(alkuperainen_taulu[indeksi])

        for indeksi in range(0, len(kopio_taulu)):
            intjoukko.poista(kopio_taulu[indeksi])

        return intjoukko

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.lukujono[0]) + "}"
        else:
            tuotos = "{"
            for indeksi in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.lukujono[indeksi])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lukujono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
