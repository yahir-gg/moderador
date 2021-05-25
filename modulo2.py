from modulo1 import iniciar

def filtro():
    resultado = []
    resultado.append(iniciar())

    """Mostrando longitud de la lista principal"""

    print(len(resultado))

    """La lista tiene longitud 1, es decir, tiene una lista dentro, exploramos esa lista interna"""

    print(len(resultado[0]))

    """La lista interna tiene una longitud de 4, es decir, las 4 listas que retorna la funcion principal
    * Si quieren imprimir la primera lista 1:
    resultado [0] [0]
    * Para la segunda lista:
    resultado [0] [1]

    Primero va el nombre, luego el 0 (siempre) y luego el numero de la lista (0,1,2, o 3)
    """

    c1 = 0
    for elem in resultado[0]:
        print('Lista ',c1,': ',elem)
        c1+=1

    """POO, Creacion de una clase: como atributos tiene nombre y cantidad (de mensajes agresivos)"""

    class Objeto:
        nombre = ""
        cantidad = 0

    """a1 es la lista de usuarios agresivos"""

    a1=[]
    # recorremos la lista de mensajes agresivos
    for e in resultado[0][0]:
        # verificamos que no se repitan los nombres
        if e['from'] not in a1:
            # se agrega el user a la lista
            a1.append(e['from'])

    a1

    """Se crea una lista llamada objetos que guardara objetos, por cada usuario agresivo se crea un objeto"""

    objetos = []
    # recorremos la lista de user agresivos
    for e in a1:
        # se crea objeto
        o = Objeto()
        # asignacion de nombre
        o.nombre = str(e)
        # cantidad por default se pone en 0
        # el objeto se añade a la lista objetos
        objetos.append(o)
        print('Objeto ',e, 'creado')

    """**CONTAMOS LOS MENSAJES AGRESIVOS Y LOS ASIGNAMOS AL OBJETO**"""

    cont = 0
    # recorremos la lista de msj agresivos
    for d in resultado[0][0]:
        # recorremos la lista de objetos
        for h in objetos:
            # verificamos si el usuario agresivo tiene un objeto creado
            if d['from'] == h.nombre:
                # se aumenta en uno la cantidad de msj agr
                h.cantidad+=1

    """Imprimimos los objetos que tenemos"""

    print('Objetos')
    # recorremos la lista de objetos
    for h in objetos:
        print('User: ',h.nombre,' Num.MsjAgr: ',h.cantidad)

    """Comprobamos en la lista de mensajes agresivos"""

    for e in resultado[0][0]:
        print(e['from'],e['text'])

    """Listo, ya esta lo mas dificil, ahora continuen con sus demas listas. Cuando hagan su parte denle a las variables y listas nombres adecuados"""

    blockUsers = []
    userSlice  = slice(3)
    for o in objetos:
        # La cantidad tiene que ser >= que 3, pero para funcionara en este ejemplo lo puse como 2
        if o.cantidad >= 2:
            blockUsers.append(o.nombre)
            bloqueaUsers= blockUsers[userSlice]
    
    print(bloqueaUsers)

    #resultado[0][3]
    msjAgrUs = []
    for w in resultado[0][3]:
        for t in bloqueaUsers:
            if w['from'] != t:
                msjAgrUs.append(w)

    print(msjAgrUs)

    return bloqueaUsers, msjAgrUs

    

    

