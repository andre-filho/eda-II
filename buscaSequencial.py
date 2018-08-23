import time
def busca_sequencial (v, x):
	i = 0
	while i < len(v):
		if v[i] == x:
			return i
		i = i+1	
	return False

def busca_sequencial_sentinela(v, x):
	v.append(x) #add sentinela
	i = 0
	while v[i] != x:
		i += 1
	if i == len(v)-1:
		return -1
	return i

def busca_binaria(vetor, inicio, fim, element):
	if inicio <= fim:
		meio = (inicio+fim) // 2 #indice do meio
		if element > vetor[meio]: #element ta a direita
			return busca_binaria(vetor, meio+1, fim, element)
		elif element < vetor[meio]:
			return busca_binaria(vetor, inicio, meio-1, element)
		else: 
			return meio
	return -1

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
print("Tempo de execucao sequencial: %0.2f ms" %(total))


antes2 = time.time()
posicao2 = busca_sequencial_sentinela(vetor,elemento)
depois2 = time.time()
total2 = (depois2-antes2)*1000

if posicao2 >= 0:
	print("O elemento foi encontrado na posicao %d." % (posicao2))
else:
	print("O elemento não foi encontrado.")
print("Tempo de execucao sequencial sentinela: %0.2f ms" %(total2))

antes3 = time.time()
posicao3 = busca_binaria(vetor, 0, len(vetor)-1, elemento)
depois3 = time.time()
total3 = (depois3-antes3)*1000

if posicao3 >= 0:
	print("O elemento foi encontrado na posicao %d." % (posicao3))
else:
	print("O elemento não foi encontrado.")
print("Tempo de execucao busca binaria: %0.2f ms." % (total3))




