print ('Seleccione el solido al cual desea conocer su volumen\n')
print ('1. Prisma')
print ('2. Piramide')
print ('3. Cono truncado')
print ('4. Cilindro')       
vi = int(input())

if vi==1:
    pl = float(input('digite el largo del prisma en cm: \n'))
    pa = float(input('digite el ancho del prisma en cm: \n'))
    pal = float(input('digite la altura del prisma en cm: \n'))
    r = pl * pa * pal
    print(f'el volumen del prisma es: {r} cm3')
elif vi==2:
    ab = float(input('digite el valor de area de base de la piramide en cm: \n'))
    alt = float(input('digite la altura de la piramide en cm: \n'))
    var = 3
    rp = (ab * alt)/3 
    print(f'el volumen de la piramide es: {rp:.2f} cm3')
elif vi==3:
    ri = float(input('digite el valor del radio inferior en cm: \n'))
    rie = ri**2
    rs = float(input('digite el valor del radio superior en cm: \n'))
    rse = rs**2
    ac = float(input('digite el valor de la altura del cono en cm: \n'))
    pi = 3.14
    ra = ri*rs
    rc = ((pi*ac)*(rie+rse+ra))/3
    print(f'el volumen del cono es: {rc:.2f} cm3')
elif vi==4:
    rci = float(input('digite el valor del radio en cm: \n'))**2
    aci = float(input('digite el valor de la altura en cm: \n'))
    pic = 3.14
    reci= pic*rci*aci
    print(f'el volumen del cilindro es: {reci:.2f} cm3')
else:
    print('Opcion incorrecta')