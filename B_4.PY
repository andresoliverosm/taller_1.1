print ('Escoja un tipo de robot\n')
print ('1. Cilindrico')
print ('2. Cartesiano')
print ('3. Esferico')     
vi = int(input())

if vi==1:
    print(f'el robot cilindrico tiene dos articulaciones prismaticas')
elif vi==2:
    print(f'el robot cartesiano tiene tres articulaciones de rotacion')
elif vi==3:
    print(f'el robot esferico tiene dos articulaciones rotacionales y una lineal')
else:
    print('Opcion incorrecta')