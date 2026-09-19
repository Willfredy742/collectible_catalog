
print("=" * 60)
print("      BIENVENIDO AL SISTEMA DE CATÁLOGO DE COLECCIONABLES       ")
print("=" * 60)

catalog = []
categories = set()
allowed_statuses = ["disponible", "reservada", "vendida"]

print("\nPlease enter information for 10 collectible items:")

for i in range(1, 11):
    print(f"\n--- Registering item {i} of 10 ---")