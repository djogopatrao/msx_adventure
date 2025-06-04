import pandas as pd
import numpy as np


def monta_byte( bits ):
    total = 0
    i = 1
    for b in bits:
        if b!=0:
            total += i
        i *= 2
    return total

column_to_bit = ['porta aberta', 'escuro', 'chave amarela inicio',
 'chave branca inicio', 'chave preta inicio', 
 'taca inicio', 'dragao inicio', 'nenhum inicio' ]


df = pd.read_csv( "READABLE_ROOM2.CSV", index_col=0 )

for i, row in df.iterrows():
    bit_array = map( lambda x: row[x], column_to_bit )
    rf = monta_byte( bit_array )
    rf += row['objeto porta'] * 256
    row['rf'] = rf

df = df.drop( column_to_bit + [ 'objeto porta' ], axis = 1 )

df.to_csv("ROOM2.CSV", index=False)