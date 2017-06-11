from graphviz import Digraph

dot = Digraph(comment='The Round Table')

dot.node('A', 'King Arthur')
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')

dot.edges(['AB', 'AL'])
dot.edge('B', 'L', constraint='false')

print dot.source

"""
[CLS]: default render
"""
dot.render('output_python_gen_dot.render.dot', view=True)  

"""
[CLS]: manual save as a file
"""
with open("output_python_gen_dot.filewrite.dot","w") as out_file:
    out_file.write(dot.source)
    
