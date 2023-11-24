#centroide et box
import matplotlib.pyplot as plt

arr = create_image((50, 50))
#draw_circle(arr, (20, 30), 10)
#draw_circle(arr, (35, 30), 10)
arr[5:30, 5:10] = 1
arr[5:10, 10:30] = 1
#arr = np.identity(5)
print(f'Centroid : {centroid(arr)}')
print(f'Aire : {area(arr)}')
xx = np.sum(np.sum(arr, axis=0).astype(np.bool_))
yy = np.sum(np.sum(arr, axis=1).astype(np.bool_))
print(f'Somme x : { xx }')
print(f'Somme y : { yy }')
print(f'Aire bounding box : {xx * yy}')

arr = create_image((50, 50))
#draw_circle(arr, (20, 30), 10)
#draw_circle(arr, (35, 30), 10)
arr[5:40, 5:20] = 1
arr[5:20, 5:40] = 1
#arr = np.identity(5)
print(f'Centroid : {centroid(arr)}')
print(f'Aire : {area(arr)}')
xx = np.sum(np.sum(arr, axis=0).astype(np.bool_))
yy = np.sum(np.sum(arr, axis=1).astype(np.bool_))
print(f'Somme x : { xx }')
print(f'Somme y : { yy }')
print(f'Aire bounding box : {xx * yy}')


plt.imshow(arr, cmap=plt.cm.gray)
plt.show()