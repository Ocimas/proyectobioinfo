from Bio import Entrez
Entrez.email = "ocia@alumni.uv.es"
handle = Entrez.einfo()
result = handle.read()
print (result)
