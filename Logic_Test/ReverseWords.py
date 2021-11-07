def balikKata(kalimat):
	banyakKata = kalimat.split(" ")
	kataBaru = [kata[::-1] for kata in banyakKata]
	kalimatBaru = " ".join(kataBaru)
	return kalimatBaru

kalimat = str(input('masukan kata: '))
print(balikKata(kalimat))
