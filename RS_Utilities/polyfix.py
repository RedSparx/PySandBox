import os.path
import sys
import re

# No arguments.
if len(sys.argv)==1 or len(sys.argv)>3:
    print('POLYFIX ERROR -- Requires two arguments: polyfix <input filename> <output filename>')
    sys.exit()

# 2 or three arguments.  Check if the fle exists. Only continue if the input file exists.
if len(sys.argv)<=3:
    #If the file does not exist...
    if os.path.isfile(sys.argv[1])==False:
        print('POLYFIX ERROR -- Input file %s does not exist. '%sys.argv[1])
        sys.exit()
    else:
        input_file = open(sys.argv[1])
        if len(sys.argv)==2:
            ofname='output.scr'
        else:
            ofname=sys.argv[2]
        output_file = open(ofname,'wt')

print('Completing POLYGON coordinates in SCR...')
SCR_File=input_file.readlines()
for L in SCR_File:
    if 'POLYGON' in L:
        Coordinates = re.findall('(-?\d+.\d+ -?\d+.\d+)+',L)
        Coordinates2= ['({})'.format(Coordinates[i]) for i in range(len(Coordinates))]
        Coordinates2.append(Coordinates2[0])
        print('POLYGON '+' '.join(Coordinates2)+';',file=output_file)
    else:
        print(L.strip(),file=output_file)
print('Written to %s'%ofname)
print('\npolyfix v0.1: c. 2018 RedSparx*, J. Salik')
input_file.close()
output_file.close()
print