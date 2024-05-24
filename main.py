#lista de 15 nomes 
nomes = ['Alex', 'Eduardo','Maria','Mariana','Joãom','José','Joana','Fernanda', 'Fulano', 'Cicrano','Beltrano','Connor', 'Corona', 'Cecilia','Alexandre']

#usuario informa o nome que deseja pesquisar 
nome = input('Digite o nome a ser pesquisado:').capitalize()

# retorna o indice do nome pesquisado
try:
    indice = nomes.index(nome)
    print(f'nome encontrado:{nome}no indice{indice}.')

#verifica se o nome esta na lista ou não
#if nome in nomes: deu erro 
    print(f'Nome encontrado :{nome} no indice {indice}.')
except:
    print(f'{nome} não encontrado na lista.')        
        