def fibonaci(num):
	if (num == 0):
		print(0)
		return

	angka_pertama = 0
	angka_kedua = 1
	angka_ketiga = angka_pertama + angka_kedua

	while (angka_ketiga <= num):
		angka_pertama = angka_kedua

		angka_kedua = angka_ketiga

		angka_ketiga = angka_pertama + angka_kedua

	if (abs(angka_ketiga - num) >=
		abs(angka_kedua - num)):
		ans = angka_kedua
	else:
		ans = angka_ketiga

	print(ans)

if __name__ == '__main__':
	
	N = int(input('masukan angka:'))
	
	fibonaci(N)


