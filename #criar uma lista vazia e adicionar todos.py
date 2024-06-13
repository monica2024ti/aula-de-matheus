Lista=[]
for nome in range(1,20):
    nome= input("digite o nome do aluno:ou digite 'fim'para parar:")
    if nome=='fim':
        break
    Lista.append(nome)
    print("nome dos alunos:",Lista)