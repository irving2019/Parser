from urllib.request import urlopen
url = input("Enter your url: ") #view url = https(http)://site.domen
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
file1 = open("Myfyle2.txt", "w")
file1.write(html)
with open("Myfyle2.txt", "w") as f:
    data = [html]
    line = ">"
    for line in data:
        f.write(line + "\n")
