class Biblioteka:


	ksiazki = []
	egzemplarze = []
	czytelnicy = []


	def __init__(self, limit):
		self.limit = limit


	def dodaj_egzemplarz_ksiazki(self, ksiazka):
		self.ksiazki.append(ksiazka)
		return True


	def wypozycz(self, czytelnik, tytul):
		if len(czytelnik.lista_czytelnika) < 3:
			for ksiazka_wypozyczona in self.ksiazki:
				if ksiazka_wypozyczona.tytul == tytul:
					for ksiazka_czytelnika in czytelnik.lista_czytelnika:
						if ksiazka_czytelnika.tytul == tytul:
							return False
					czytelnik.lista_czytelnika.append(ksiazka_wypozyczona)
					self.ksiazki.remove(ksiazka_wypozyczona)
					return True
		return False


	def oddaj(self, nazwisko, tytul):
		for czytelnik in self.czytelnicy:
			if czytelnik.nazwisko == nazwisko:
				for ksiazka_czytelnika in czytelnik.lista_czytelnika:
					if ksiazka_czytelnika.tytul == tytul:
						self.ksiazki.append(ksiazka_czytelnika)
						czytelnik.lista_czytelnika.remove(ksiazka_czytelnika)
						return True
		return False


class Ksiazka:
	def __init__(self, tytul, autor, rok):
		self.tytul = tytul
		self.autor = autor
		self.rok = rok


class Egzemplarz:
	def __init__(self, rok_wydania, wypozyczony):
		self.rok_wydania = rok_wydania
		self.wypozyczony = wypozyczony


class Czytelnik:
	def __init__(self, nazwisko, lista_czytelnika):
		self.nazwisko = nazwisko
		self.lista_czytelnika = lista_czytelnika


n = int(input())
operacje = [input().strip(' ') for operacja in range(n)]
usun = []
biblioteka = Biblioteka(15)


for x in operacje:
	nawias = x.replace("(", "")
	nawias_2 = nawias.replace(")", "")
	cudzyslow = nawias_2.replace("\"", "")
	usun = cudzyslow.split(", ")
	if usun[0].strip() == "dodaj":
		ksiazka = Ksiazka(tytul=usun[1].strip(), autor=usun[2].strip(), rok=usun[3].strip())
		print(biblioteka.dodaj_egzemplarz_ksiazki(ksiazka))
	if usun[0].strip() == "wypozycz":
		wypozyczona = False
		tytul = usun[2].strip()
		for czytelnik in biblioteka.czytelnicy:
			if czytelnik.nazwisko == usun[1].strip():
				wypozyczona = True
				print(biblioteka.wypozycz(czytelnik, tytul))
				break
		if not wypozyczona:
			nowy_czytelnik = Czytelnik(usun[1].strip(), [])
			biblioteka.czytelnicy.append(nowy_czytelnik)
			print(biblioteka.wypozycz(nowy_czytelnik, tytul))
	if usun[0].strip() == "oddaj":
		nazwisko = usun[1].strip()
		tytul = usun[2].strip()
		print(biblioteka.oddaj(nazwisko, tytul))
