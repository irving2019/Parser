from urllib.request import urlopen
url = input("Enter your url: ") #view url = https(http)://site.domen
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
file1 = open("File.txt", "w") # file for save
file1.write(html)
