
print("=" * 60)
print("      BIENVENIDO AL SISTEMA DE CATÁLOGO DE COLECCIONABLES       ")
print("=" * 60)

catalog = []
categories = set()
allowed_statuses = ["disponible", "reservada", "vendida"]

print("\nPlease enter information for 10 collectible items:")

for i in range(1, 11):
    print(f"\n--- Registering item {i} of 10 ---")

item_id = input("Enter ID: ").strip()
name = input("Enter name: ").strip()
category = input("Enter category: ").strip()

while True:
    try:
        price = float(input("Enter price (decimal): "))
        if price > 0:
            break
        print("Error: Price must be greater than zero.")
    except ValueError:
        print("Error: Please enter a valid numeric value.")
