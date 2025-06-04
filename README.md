# duckslayeradventure

msxbas2rom.exe -c main16-6.asc

funciona na versão 0.3.0.4 - não testado em versões posteriores

# como jogar

setas ou joystick => move o cursor
botão 1 ou espaço => solta objeto
F1 ou B1+B2+Para cima => reset - nova vida (começa de novo na mesma fase)
F6 ou B1+B2+Para baixo  => select - escolhe fase para jogar

# programas auxiliares

le_room.py => converte o formato ROOM csv para legível (com informacoes da coluna RF codificadas em bits expandidas em colunas proprias)
salva_room.py => converte o formato ROOM legível para CSV

produce_map_bins.py => converte arquivos CSV ROOM, OBJECT, e OBJ_PREF para formato binario (para compilação do .ROM)

chars => monte o diretorio no openmsx. o chars.asc cria o arquivo com as fontes advchr.sc1

maze4.asc => cria as telas do labirinto da fase 4

# tela de apresentação do jogo

Editar o projeto com o nmsxtiles e salvar os arquivos de padrao (.pat), paleta (.pal) e cores (.col).

Depois, precisa executar o title\criatela.bas para compor com os sprites (e corrigir color clashes).

# documentação

ROOM.CSV: Arquivo de descrição das salas

Coluna RL: room layout
	- Bit 8 (128): 1 Layout da sala é o recurso ResLayouts + RL AND 127
	               0 Layout da sala de acordo com os bits abaixo:
				   
	- Bit 0 (1) 1 Saída Leste
	- Bit 1 (2) 1 Saída Oeste
	- Bit 2 (4) 1 Saída Norte
	- Bit 3 (8) 1 Saída Sul
	- Bit 4 (16) 1 Paredes laterais com linha preta
				 

Coluna RF: Room Flags. 
	Se a sala for um castelo:
	- bit 0: 0 porta aberta
	         1 porta fechada
	- bits 8-15: objeto da porta de entrada
	
	Qualquer tipo de sala:
	- bit 1: 0 visibilidade normal
			 2 escuro (apenas raio de 3 caracteres visíveis)
			 
	- bits 2-7: objeto que nao pode ser randomizado nessa sala:
			2: chave amarela
			3: chave branca
			4: chave preta
			5: taca
			6: dragao
			7: nenhum
			 
	
	
OBJECTS.CSV: Objetos do jogo

Coluna OA: Object Attributes
	Se o objeto for um dragão (7-9):
	- 0: dragao procurando
	- >0: dragao mordendo (vira um contador de ciclos para a duração da mordida)
	- -1: dragao buxin cheio
	- -2: dragao morto
	
	Se o objeto for um morcego (10):
	- -1: procurando objeto para trocar
	- <-1: voando com o objeto (contador de ciclos para querer trocar novamente)
	- >=0: achou um objeto, perseguindo este objeto (se ele sair da sala, volta pro -1)
	
	Se o objeto for uma porta (11-13):
	- bits 0-7: para qual sala a porta vai levar
	- bit 8 (256): 0: Porta está fechada / 1 aberta
	
# sprites
id	spr	camadas	nome
-1	0	0	cursor
0	5	1	chave amarela
1	5	2	chave branca
2 	5	3	chave preta
3 	6	4	espada
4 	7	5	ima
5 	8	6	taça
6	18-20	7,16,25	ponte (esquerda)
	21-23	29,30,31	ponte(direita)
7	9-11	8,17,26	dragao amarelo
8	9-11	9,18,27	dragao verde
9 	9-11	10,19,28	dragao vermelho 
10	24,25	11,20	morcego  
11	1-4		12,23	porta do castelo amarelo (oa: bit 256=1 aberto/0 fechado 0-255 sala que vai)
12	1-4		12,23	porta do castelo branco 
13	1-4		12,23	porta do castelo preto 
14	27	13	portal de fase 1
15 33	13	grey dot
16 27	21	portal de fase 2
17 27	22	portal de fase 3
18 		arma de portal

# Conquistas

 0- pacifista (sem matar nenhum dragao)
 1- seu jorge por favor me empresta o dragao (matou todos dragoes)
 2- easter egg
 3- atraído (atraiu a taça pra dentro do castelo)
 4- acumulador (acumulou todos os objetos no castelo)
 5- terceirização (o morcego levou a taça pro castelo)
 6- passeio (voou na barriga do dragao levado pelo morcego)
 7- terminou o jogo IV