import pandas as pd
import numpy as np


df = pd.read_csv( "ROOM2.CSV" )

# deprecar?
df[ 'porta aberta' ]         = np.bitwise_and( df[ 'rf' ] , 1 )

# se sala é escura
df[ 'escuro' ]               = np.bitwise_and( df[ 'rf' ] , 2 )

# quais objetos não podem ser colocados nas salas quando randomizar
df[ 'chave amarela inicio' ] = np.bitwise_and( df['rf'],4 )
df[ 'chave branca inicio' ]  = np.bitwise_and( df['rf'],8 )
df[ 'chave preta inicio' ]   = np.bitwise_and( df['rf'],16 )
df[ 'taca inicio' ]          = np.bitwise_and( df['rf'],32 )
df[ 'dragao inicio' ]        = np.bitwise_and( df['rf'],64 )
df[ 'nenhum inicio' ]        = np.bitwise_and( df['rf'],128 )

# se é a entrada de um castelo, qual o objeto porta correspondente
df[ 'objeto porta' ] = df[ 'rf' ] // 256


# salva como readable
df.to_csv("READABLE_ROOM2.CSV")