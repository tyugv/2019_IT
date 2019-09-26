import matplotlib.pyplot as plt 
import numpy as np 
from math import pi,e 


def f_gauss(u,v,sigma): 
	return 1/(2*pi*sigma*sigma)*e**(-1*(u**2+v**2)/(2*sigma**2)) #функция Гаусса


def get_gauss_kernel(r, sigma = 3): 
	kernel = np.zeros((2*r, 2*r)) 
	for pic_x in range(2*r): 
		for pic_y in range(2*r): 
			kernel[pic_x,pic_y] += f_gauss(pic_x,pic_y,sigma) #делаем фильтр размытия
	kernel/=kernel.sum() #нормируем
	return kernel 


def gauss_filter(img,r=4): 
	img2 = np.zeros_like(img) 
	kernel = get_gauss_kernel(r) 
	for k in range(img.shape[2]): 
		for i in range(r, img.shape[0]-r):
			for j in range(r, img.shape[1]-r):
				img_part = img[i-r:i+r, j-r:j+r, k] #выделяем кусочек изображения для обработки
				img2[i,j,k] = (kernel*img_part).sum() #применяем фильтр
	return img2 


def main(): 

	img = plt.imread("img.png")[:, :, :3] 

	img2 = gauss_filter(img) 

	fig, axs = plt.subplots(1,2) 
	axs[0].imshow(img) 
	axs[1].imshow(img2) 
	plt.show() 


if __name__ == "__main__": 
	main()