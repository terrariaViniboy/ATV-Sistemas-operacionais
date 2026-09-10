import os, subprocess
# Mostra a pasta atual
print(os.getcwd())

#Mostra o processo atual
print("Processo atual",os.getpid())


subprocess.run("notepad")

#Cria um arquivo
with open("Arquivo_aula.txt","w") as arquivo:
    arquivo.write("teste")