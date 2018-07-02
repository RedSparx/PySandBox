import graphviz
import pandas as pd
from sklearn import tree

def Get_Grades():
    df=pd.read_csv('Student_Data.csv')
    # Process assessments.
    df.Midterm = df.Midterm/27*100
    df.Final = df.Final/35*100
    df.Professionalism=df.Professionalism/10*10
    df.Assignment_1=df.Assignment_1/15*100
    df.Assignment_2=df.Assignment_2/30*100
    df.Project=df.Project/25*100
    # Compute final results.
    df['Final_Mark']=\
        df.Midterm*0.15+\
        df.Final*0.25+\
        df.Professionalism*0.10+\
        df.Assignment_1*0.10+ \
        df.Assignment_2*0.15 + \
        df.Project*0.25
    df['Final_Result']=df.Final_Mark>60
    return df

if __name__=='__main__':
    Grades=Get_Grades()
    X=Grades[['Midterm','Final','Professionalism','Assignment_1','Assignment_2','Project']]
    Y=Grades['Final_Result']
    # region Build the decision tree.
    DTree = tree.DecisionTreeClassifier(criterion='entropy')
    DTree.fit(X, Y)
    # endregion
    # region Render decision tree.
    dot_data = tree.export_graphviz(DTree, out_file=None, filled=True, rounded=True, rotate=True, proportion=True, \
            feature_names = list(X),\
            class_names=['Fail','Pass'])
    graph = graphviz.Source(dot_data)
    graph.format = 'png'
    graph.render('Grade_Breakdown', view=True)
    # endregion