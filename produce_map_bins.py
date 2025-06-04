import pandas as pd

def convert_to_binary(input_file, output_file, header='infer'):
    print("Processando %s => %s" % ( input_file, output_file ) ) 
    df = pd.read_csv(input_file, engine='python', header=header)
    df = df.rename( { "'ol":"ol" } , axis = 1 )
    df = df.dropna()

    with open(output_file, 'wb') as f:
        for i, row in df.iterrows():
            for c in df.columns:
                if c!='texto':
                
                    if type( row[c] ) == str:
                        if row[c].strip() == '?':                            
                            v = -1
                        else:
                            v = int( row[c] )                        
                    else:
                        v = int( row[c] )
                        
                    if v==-1:
                        v=65535
                    try:
                      f.write( int.to_bytes( v, 2, 'little' ) )
                    except:
                      print( "Row:", row , "(",i,")" )
                      print( "Column:", c )
                      print( "Value: ", v )
                      raise


convert_to_binary( 'OBJECTS0.csv', 'data/OBJECTS0.bin' )
convert_to_binary( 'OBJECTS1.txt', 'data/OBJECTS1.bin' )
convert_to_binary( 'OBJECTS2.CSV', 'data/OBJECTS2.bin' )
convert_to_binary( 'OBJECTS3.CSV', 'data/OBJECTS3.bin' )

convert_to_binary( 'temple/OBJECTS.CSV', 'temple/OBJECTS.bin' )

convert_to_binary( 'ROOM0.CSV', 'data/ROOM0.bin' )
convert_to_binary( 'ROOM1.CSV', 'data/ROOM1.bin' )
convert_to_binary( 'ROOM2.CSV', 'data/ROOM2.bin' )
convert_to_binary( 'ROOM3.CSV', 'data/ROOM3.bin' )

convert_to_binary( 'OBJ_PREF.CSV', 'data/OBJ_PREF.bin' )

convert_to_binary( 'title.csv', 'data/TITLE.bin',header=None )

#convert_to_binary( 'psg_ini.csv', 'data/psg_ini.bin' )
#convert_to_binary( 'psg_sfx.csv', 'data/psg_sfx.bin' )

convert_to_binary( 'ObjetoSalaFlag.csv', 'data/ObjetoSalaFlag.bin' )
