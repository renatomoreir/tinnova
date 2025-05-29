VALID_MARCAS = {
    "Ford", "Honda", "Volkswagen", "Chevrolet", "Fiat", "Toyota", "Nissan", "Jeep",
    "Hyundai", "Renault", "Peugeot", "Citroën", "Kia", "Mitsubishi", "Mercedes-Benz",
    "BMW", "Audi", "Chery", "Land Rover", "Subaru", "Suzuki", "Volvo", "Lexus",
    "Jaguar", "Porsche", "Ram", "Dodge", "Mini", "JAC", "BYD", "Geely", "Great Wall",
    "SsangYong", "Troller", "Tesla", "Bugatti", "Ferrari", "Lamborghini", "Maserati",
    "Alfa Romeo", "Aston Martin", "Bentley", "Rolls-Royce", "Smart", "Pontiac",
    "Buick", "Cadillac", "Chrysler", "GMC", "Lincoln", "Acura", "Infiniti", "Isuzu",
    "Saab", "Seat", "Skoda", "Daihatsu", "Datsun", "Lada", "Mahindra", "Pagani",
    "McLaren", "Hummer", "Opel", "Rover", "Scania", "International", "Agrale",
    "Effa", "Foton", "Lifan", "Shineray", "Sinotruk", "Spyker", "Tata", "VLE",
    "Willys", "Zotye"
}

def marca_valida(marca):
    return marca in {m.lower() for m in VALID_MARCAS}
