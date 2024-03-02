import cv2
lista_areas = []
img = cv2.imread("SeccionC/susuki.JPG")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thr = cv2.threshold(gray, 210, 255, cv2.THRESH_BINARY_INV, cv2.THRESH_OTSU)
contornos, _ = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contornos)):
    area = cv2.contourArea(contornos[i])
    lista_areas.append(area)
cMax = lista_areas.index(max(lista_areas))
cnt = contornos[cMax]
print (f'las cordenadas X - Y del logo de susuki son \n {cnt}')
cv2.drawContours(img, contornos, cMax, (0, 255, 0), 1)
cv2.imshow("puntos extremos", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

lista_areas2 = []
img2 = cv2.imread("SeccionC/chevrolet.JPG")
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
_, thr2 = cv2.threshold(gray2, 210, 255, cv2.THRESH_BINARY_INV, cv2.THRESH_OTSU)
contornos2, _ = cv2.findContours(thr2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contornos2)):
    area2 = cv2.contourArea(contornos2[i])
    lista_areas2.append(area2)
cMax2 = lista_areas2.index(max(lista_areas2))
cnt2 = contornos2[cMax2]
print (f'las cordenadas X - Y del logo de chevrolet son \n {cnt2}')
cv2.drawContours(img2, contornos2, cMax2, (0, 255, 0), 1)
cv2.imshow("puntos extremosR", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()