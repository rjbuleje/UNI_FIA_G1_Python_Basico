def run():
    my_list = ["djdjd", 2, [1, 2], (1, 2), True, 5.2]
    tupla = (473, "fjfjfjf", (1), [3, (1, 3, [1])], False)
    my_dicci = { "primero" : 46, "segundo" : "dos", 2 : (1, 3), True : [56.5]}

    my_list.append(125265)
    my_list.append("hola mundo")

  
    my_list.pop(1)


    print(my_dicci)
    print(tupla)
    print(my_list)

    for key in my_dicci.keys():
        print(key)

    for valor in my_dicci.values():
        print(valor)    
    
    for llave, valor in my_dicci.items():
        print(llave)
        print(valor)



if __name__ == "__main__":
    run()