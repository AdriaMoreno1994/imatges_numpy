import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image  as mpimg

print("EX1")

arr = np.arange((9), dtype=np.int64)
print("Array:",arr)
print("dimensio:",arr.ndim)
print("forma de la matriu",arr.shape)
print("matriu:\n",arr)
print("Ex2")
mitja =np.median(arr)
print("Valor mitjà:",mitja)
newArr = np.subtract(arr,mitja)
print(newArr)
print("Ex3")
matrix = np.random.randint(1,10+1,size=(5,5))
print(matrix)
matrix_max = np.amax(matrix)
print("valor maxim",matrix_max)
max_y = np.amax(matrix,axis=0)
max_x = np.amax(matrix,axis=1)
print("valors maxims eix y:",max_y)
print("valors maxims eix x:",max_x)

print("Ex4")
matrixA = np.random.randint(low=1,high=10,size = (4,6))
matrixB = np.random.randint(low=1,high=10,size = (4,1))
print("A\n")
print(matrixA)
print("B\n")
print(matrixB)
print("A partir del broadcasting per poder sumar les matrius  primer compararà si tenen el mateix shape en cas contrari,\n"
      "expandirà la matriu inferior per poder  tenir el mateix nombre de columnes i files\n ")
print(matrixA+matrixB)
print("En el seguent exemple  la matriu C es unidimensional mentres que la matriu D es bidimensional\n"
      "per tant el broadcasting expandirà la matriu C fins a tenir el mateix nombre de files que la matriu D")
matrixC = np.random.randint(low=1,high=10,size = (1,3))
matrixD = np.random.randint(low=1,high=10,size = (4,3))
print("C")
print(matrixA)
print("D")
print(matrixB)
print("C+D")
print(matrixA+matrixB)


print("Ex5")
matrix = np.random.randint(low=1,high =10, size = (5,5))
print(matrix)
print("prova")
colum = matrix[:,0]
row = matrix[0,:]
sum = colum + row
print("sum of first row and first colum")
print(sum)
print("EX6")
print("mask")
mask = matrix % 4 == 0
print(mask)
print("Ex7")
print(matrix[mask])
image = mpimg.imread("Europe_a_Prophecy_copy_K_plate_01.jpg")
print("Ex 8")
print(image)

newImage = image[:,:,0]
print("sense verd ni blau")



print(np.shape(newImage))
plt.imshow(newImage)
plt.show()
mpimg.imsave("image.png",newImage)



















