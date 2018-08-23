import time
def busca_sequencial (v, x):
	i = 0
	while i < len(v):
		if v[i] == x:
			return i
		i = i+1	
	return False

def busca_sequencial_sentinela(v,x):
	v.append(x) #add sentinela
	i = 0
	while v[i] != x:
		i += 1
	if i == len(v)-1:
		return -1
	return i


vetor = list (range(0,1000000))

elemento = int(input('Digite o valor que gostaria de encontrar: '))
antes = time.time()
posicao = busca_sequencial(vetor, elemento)
depois = time.time()
total = (depois-antes)*1000

if posicao >= 0:
	print("O elemento foi encontrado na posicao %d." % (posicao))
else:
	print("O elemento não foi encontrado.")
print("Tempo de execucao: %0.2f ms" %(total))

posicao2 = busca_sequencial_sentinela(vetor,elemento)
antes2 = time.time()
posicao = busca_sequencial(vetor, elemento)
depois2 = time.time()
total2 = (depois2-antes2)*1000

if posicao >= 0:
	print("O elemento foi encontrado na posicao %d." % (posicao2))
else:
	print("O elemento não foi encontrado.")
print("Tempo de execucao: %0.2f ms" %(total2))
