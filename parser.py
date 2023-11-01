from urllib.request import urlopen
url = input("Введите url: ")
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
file1 = open("index.html", "w")
file1.write(html)
with open("index.html", "w") as f:
    data = [html]
    line = ">"
    for line in data:
        f.write(line + "\n")
