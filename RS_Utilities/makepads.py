import os.path
import sys
import re

# No arguments.
if len(sys.argv)==1 or len(sys.argv)>3:
    print('MAKEPADS ERROR -- Requires two arguments: makepads <input filename> <output filename>')
    sys.exit()

# 2 or three arguments.  Check if the fle exists. Only continue if the input file exists.
if len(sys.argv)<=3:
    #If the file does not exist...
    if os.path.isfile(sys.argv[1])==False:
        print('MAKEPADS ERROR -- Input file %s does not exist. '%sys.argv[1])
        sys.exit()
    else:
        input_file = open(sys.argv[1])
        if len(sys.argv)==2:
            ofname='output.scr'
        else:
            ofname=sys.argv[2]
        output_file = open(ofname,'wt')

SCR_File=input_file.readlines()

Pad_Layers=[1,29,31]
for Layer in Pad_Layers:
    for L in SCR_File:
        # if re.search(r'SET WIDTH (\d+.\d+);',L):
        #     print(re.sub(r'SET WIDTH (\d+.\d+);',r'SET WIDTH 0',L))
        # if re.search(r'LAYER\s+(\d+);',L):
        #     print(re.sub(r'LAYER\s+(\d+);',r'LAYER %d'%Layer,L))
        if re.search(r'POLYGON\s+',L):
            print(re.sub(r'POLYGON\s+(\(-?\d+\.\d+);',r'POLYGON Command',L))


# print('Written to %s'%ofname)
# print('\npolyfix v0.1: c. 2018 RedSparx*, J. Salik')
input_file.close()
output_file.close()
print 