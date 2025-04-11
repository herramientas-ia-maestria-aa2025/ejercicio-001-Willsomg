def app(): 
    with open('informacion.txt') as archivo: 
        print(archivo.read()) 
app()