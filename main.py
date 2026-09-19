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
    categories.add(category)

    while True:
        try:
            price = float(input("Enter price (decimal): "))
            if price > 0:
                break
            print("Error: Price must be greater than zero.")
        except ValueError:
            print("Error: Please enter a valid numeric value.")

    while True:
        status = input(f"Enter status ({', '.join(allowed_statuses)}): ").strip().lower()
        if status in allowed_statuses:
            break
        print("Error: Invalid status. Choose from disponible, reservada, vendida.")

    while True:
        description = input("Enter description (must include 'usada' or 'certificada'): ")
        if "usada" in description or "certificada" in description:
            break
        print("Error: Description must contain the word 'usada' or 'certificada'.")

        item = {
            "id": item_id,
            "name": name,
            "category": category,
            "price": price,
            "status": status,
            "description": description
        }

        catalog.append(item)
        categories.add(category)

        
