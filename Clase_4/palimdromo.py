def run():
    pali = input("Ingrese su posible palindromo: ")
    pali = pali.lower()
    pali = pali.replace( " ", "")
    if pali == pali[::-1]:
        print("Sí")
    else:
        print("No")



if __name__ == "__main__":
    run()