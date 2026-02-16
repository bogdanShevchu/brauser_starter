import webbrowser as wb

def open_url(url):
	wb.open(url)

while True:
	print("2 = start_2_linc, 2p = save_2_linc:")
	vi = input("1 = start_1_linc, 1p = save_1_linc:")
	if vi == "1p":
		linc1 = open("linc1", "w")
		l1 = input("write linc")
		linc1.write(l1)
		linc1.close()
		vi = None
	elif vi == "1":
		linc1 = open("linc1", "r")
		linc_1_st = linc1.read()
		open_url(linc_1_st)
		linc1.close()
		vi = None
		break
	elif vi == "2p":
		linc2 = open("linc2", "w")
		l2 = input("write linc")
		linc2.write(l2)
		linc2.close()
		vi = None
	elif vi == "2":
		linc2 = open("linc2", "r")
		linc_2_st = linc2.read()
		open_url(linc_2_st)
		linc2.close()
		vi = None
		break
