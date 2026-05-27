import csv
import random
from datetime import datetime, timedelta


def generate_random_product():
    """Gera um nome de produto aleatório."""
    categories = ["Eletrônicos", "Roupas", "Alimentos", "Livros",
                  "Móveis", "Esportes", "Beleza", "Autopeças"]

    adjectives = ["Premium", "Pro", "Elite", "Ultra", "Basic", "Smart",
                  "Eco", "Mini", "Maxi", "Giga"]
    nouns = ["Fone", "Tênis", "Café", "Dicionário", "Sofá", "Bicicleta",
             "Crema", "Kit", "Set", "Pack"]

    return f"{random.choice(adjectives)} {random.choice(nouns)} {random.randint(1, 99)}"


def generate_random_price():
    """Gera um preço aleatório entre 5.00 e 500.00."""
    return round(random.uniform(5.0, 500.0), 2)


def generate_random_quantity():
    """Gera uma quantidade aleatória entre 1 e 50."""
    return random.randint(1, 50)


def generate_random_date(start_date=None):
    """Gera uma data aleatória a partir de start_date (últimos 365 dias)."""
    if not start_date:
        start_date = datetime.now() - timedelta(days=365)

    delta = timedelta(days=random.randint(0, 364))
    return (start_date + delta).strftime("%Y-%m-%d")


def generate_csv(filename="produtos.csv", num_records=10000):
    """Gera arquivo CSV com os dados aleatórios."""

    fieldnames = ["id", "date", "product", "quantity", "price"]

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Escreve cabeçalho
        writer.writeheader()

        # Escreve 10000 registros
        for i in range(1, num_records + 1):
            record = {
                "id": str(i).zfill(4),  # ID com leading zero (ex: 0001)
                "date": generate_random_date(),
                "product": generate_random_product(),
                "quantity": generate_random_quantity(),
                "price": f"{generate_random_price():.2f}"  # Preço com 2 casas decimais
            }
            writer.writerow(record)

    print(f"✅ Arquivo '{filename}' gerado com sucesso!")
    print(f"   • Total de registros: {num_records}")
    return filename


# Executar
if __name__ == "__main__":
    generate_csv()
