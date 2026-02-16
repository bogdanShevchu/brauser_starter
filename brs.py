import webbrowser as wb

def open_url(url):
	wb.open(url)

print("1 = start_1_linc, 1p = save_1_linc:")
while True:
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
		vi = None
		break
