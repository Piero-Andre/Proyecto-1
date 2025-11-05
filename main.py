def saludo(nombre: str) -> str:
    return f"hola, {nombre}! Bienvenido a Git. Hermoso"

if __name__ == "__main__":
    nombre = input("¿Tu nombre? ")
    print(saludo(nombre))