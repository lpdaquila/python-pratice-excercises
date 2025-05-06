lista = ['Lucas', 'Pedro', 'Juan', 'Maria', 'Ana']
lista.append('Jose')
# lista.insert(2, 'Pablo')

# i = range(len(lista))

for index, nome in enumerate(lista):
    print("%s - %s" % (index, nome))
    
