class Stadium:
    def __init__(self, meno, datum_otvorenia, krajina, pocet_sedaciek):
        self.name = meno
        self.date = datum_otvorenia
        self.country = krajina
        self.seating_capacity = pocet_sedaciek


ultraford = Stadium("Ultraford", 1985, "Anglicko", 150000)
rockford = Stadium("Rockford", 1945, "Belgicko", 550000)
trinidat = Stadium("Trinidat", 1995, "Afrika", 1468000)

stadion = [ultraford, rockford, trinidat]
najvacia_kapacita = 0
najvacsi_stadion = None

for i in stadion:
    if i.seating_capacity > najvacia_kapacita:
        najvacsia_kapacita = i.seating_capacity
        najvacsi_stadion = i

print(najvacsi_stadion.name)

stadion.sort(key=lambda i:i.seating_capacity, reverse=True)

print(stadion[0].name)

