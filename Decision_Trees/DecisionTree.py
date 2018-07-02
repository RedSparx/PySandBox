import graphviz
import numpy as np
import xlsxwriter
from sklearn import tree
import zipfile

#region Generate ramdom data.
Filename='DecisionTree'
N_Attributes=5
N_Data=250
N_Labels=2
X = np.array(np.random.random([N_Data,N_Attributes])>0.5, dtype=int)
Y = np.random.random_integers(0,N_Labels-1,N_Data)
#endregion

#region Create helper functions to label results.
Boolean=lambda b: 'FALSE' if b==0 else 'TRUE'
Class = lambda c: 'Class ' + chr(65+c)
Class_Labels =[Class(Cls) for Cls in range(0,N_Labels)]
Feature_Labels = ['Attribute %d'%i for i in range(0,N_Attributes)]
#endregion

#region Build the decision tree.
DTree = tree.DecisionTreeClassifier(criterion='entropy')
DTree.fit(X,Y)
#endregion

#region Render decision tree.
dot_data = tree.export_graphviz(DTree, out_file=None, filled=True, rounded=True, rotate=True, proportion=True,\
                                feature_names=Feature_Labels,\
                                class_names=Class_Labels)
graph = graphviz.Source(dot_data)
graph.format = 'png'
graph.render(Filename,view=True)
#endregion

#region Write Excel spreadsheet file.

Export_File=xlsxwriter.Workbook(Filename+'.xlsx')
Sheet=Export_File.add_worksheet()
Row_Offset=4
for row in range(0,N_Data):
    for col in range(0,N_Attributes):
        Sheet.write(row+Row_Offset, col, Boolean(X[row,col]))
        Sheet.write(row+Row_Offset, N_Attributes, Class(Y[row]))
Sheet.insert_image(Row_Offset, N_Attributes+2,'DecisionTree.png',{'x_scale':0.5, 'y_scale':0.5})
Export_File.close()
#endregion

#region Create a Zip file of the Excel file and the image.  They can then be removed from the directory.
ZIP_Files=[Filename+'.png', Filename+'.xlsx']
zf = zipfile.ZipFile(Filename + '.zip', mode='w')
for F in ZIP_Files:
    zf.write(F)
zf.close()
#endregion