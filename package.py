from os import listdir,remove
from os.path import isfile, join
year = "2021"
onlyxml = [f for f in listdir(year) if isfile(join(year, f))]

for ce in range(len(onlyxml)):
  onlyxml[ce] = onlyxml[ce].replace('.xml', '')
  

arq = open("listar.txt")
linhas = arq.readlines()
onlydomain = []
for linha in linhas:
  onlydomain.append(linha.replace('\n', ''))

onlysieg = []
siegdomain = []

for domain in onlydomain:
  if domain in onlyxml: siegdomain.append(domain)

for xml in onlyxml:
  if xml in onlydomain:
    pass
  else:
    onlysieg.append(xml)
  
if isfile("./resultado/somente_xml.txt") :
  remove("./resultado/somente_xml.txt")
  
somente_xml = open("./resultado/somente_xml.txt",'x')
for sieg in onlysieg:
  somente_xml.write(f"{sieg}\n")
  
if isfile("./resultado/sieg_dominio.txt") :
  remove("./resultado/sieg_dominio.txt")
siegdominio_txt = open("./resultado/sieg_dominio.txt",'x')
for dominio in siegdomain:
  siegdominio_txt.write(f"{dominio}\n")
# print(onlysieg, siegdomain)
    
# print(onlydominio)