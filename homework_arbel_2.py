from graphviz import Digraph, Graph
import webbrowser
dot = Graph(format='svg')
dot.attr(ranksep="1.6")#, , ranksep="20")  pad="24.5"nodesep="10"
names_of_characters = open(r'c:\Users\burstain\.PyCharmCE2018.1\config\scratches\names_of_characters.txt', 'r')
kinship_of_characters = r'c:\Users\burstain\.PyCharmCE2018.1\config\scratches\kinship_of_characters.txt'

list_of_names = names_of_characters.read().split("\n")

def get_diagram_husband_and_wife(husband, wife, source):
    with dot.subgraph() as s:
    #s = Graph(format='svg')
    #s=dot
        point_name = str(husband) + "+" + str(wife)
        s.attr(rank='same')
        s.node(str(husband), list_of_names[husband], fillcolor="beige", style="filled", shape="rectangle")
        s.node(str(wife), list_of_names[wife],  fillcolor="beige", style="filled", shape="rectangle")
        s.node(point_name, shape = 'point')
        s.edge(str(husband),point_name, tooltip=source, fontname="Arial", fontcolor="blue", fontsize="10", color = "green")
        s.edge(point_name, str(wife), tooltip=source , fontname="Arial" , fontcolor="blue" , fontsize="10" ,color="green")

def get_diagram_father_and_son(parentes, son, source):
    # parentes is string (E.g. "3" or "3+4")
    # son is always int
    # source is str (of course...)
    d = dot#Graph(format='svg')
    #d.attr(rank='max')
    d.rankdir = "TB"
    if "+" in parentes:
        t = parentes.split("+")
        father = int(t[0])
        mother = int(t[1])
        d.node(str(father) , list_of_names[father] , tooltip=source , fillcolor="beige" , style="filled" , shape="rectangle")
        d.node(str(mother) , list_of_names[mother] , tooltip=source , fillcolor="beige" , style="filled" , shape="rectangle")
        d.node(parentes , shape='point')
    else:
        father = int(parentes)
        d.node(str(father), list_of_names[father],tooltip=source, fillcolor="beige", style="filled", shape="rectangle")
        parentes = str(father)
    d.node(str(son) , list_of_names[son] , fillcolor="beige" , style="filled" , shape="rectangle")
    d.edge(parentes , str(son) , tooltip=source , fontname="Arial" , fontcolor="blue" , fontsize="10" , penwidth="2" , color="red")
    #dot.subgraph(d)


list_of_hasbends_and_wifes = []
list_of_fathers_and_sons = []
def main():
    with open(kinship_of_characters, 'r', encoding="utf-8") as fid:
        lines =  fid.readlines()
    for num, source in zip(lines[::2], lines[1::2]):
        kinship_number = num.replace("\n", "")
        if '#' in kinship_number:
            continue
        source = source.replace("\n", "")
        if ',' in kinship_number:
            kinship_number = kinship_number.split(',')
            list_of_fathers_and_sons.append((kinship_number[0], int(kinship_number[1]), source))
            get_diagram_father_and_son(kinship_number[0] , int(kinship_number[1]) , source)
        elif '+' in kinship_number:
            husband_and_wife = list(map(int ,kinship_number.split('+')))
            list_of_hasbends_and_wifes.append((husband_and_wife[0], husband_and_wife[1], source))
            get_diagram_husband_and_wife(husband_and_wife[0], husband_and_wife[1], source)
    #for parents in list_of_hasbends_and_wifes:
        #parents is tuple of (num_hasbend, num_wife, sorce)
        #get_diagram_husband_and_wife(parents[0] , parents[1] ,parents[2])
    #for father, son, source in list_of_fathers_and_sons:
        #num_father/or string E.g. 0+1, num_son, sorce
        #get_diagram_father_and_son(father, son, source, "s")
main()
print(dot.source)
dot.render(r"c:\Users\burstain\.PyCharmCE2018.1\config\scratches\dorot")
chrome_path = 'C:/Users/burstain/AppData/Local/Google/Chrome/Application/chrome.exe --profile-directory="Profile 1" %s'
webbrowser.get(chrome_path).open(r'c:\Users\burstain\.PyCharmCE2018.1\config\scratches\dorot.svg')
