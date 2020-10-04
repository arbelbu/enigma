from graphviz import Digraph, Graph
import webbrowser
import os
dot = Graph(format='svg')
dot.attr(ranksep="1.6")#, , ranksep="20")  pad="24.5"nodesep="10"
names_of_characters = open(r'names_of_characters.txt', 'r', encoding="utf-8")
kinship_of_characters = r'kinship_of_characters.txt'

list_of_names = names_of_characters.read().split("\n")

def add_person(graph, number):
    name, tooltip = get_tooltip(number)
    graph.node(str(number), name, tooltip=tooltip, fillcolor="beige", style="filled", shape="rectangle" )

def chrome_hebrew(name):
    if "(" in name:
        #import pdb;pdb.set_trace()
        return name + u'\u200F'
    return name

def get_tooltip(number):
    name = list_of_names[number]
    open_, close_ = name.find("["), name.find("]")
    if open_==-1 or close_==-1:
        return chrome_hebrew(name), str(number)
    return chrome_hebrew(name[:open_]), name[open_+1:close_]

def get_diagram_husband_and_wife(husband, wife, source):
    husband_ = str(husband)+"_"
    wife_ = str(wife)+"_"
    with dot.subgraph() as s:
        s.attr(rank='same')
        point_name = str(husband) + "+" + str(wife)
        s.node(point_name, shape = 'point')
    with dot.subgraph() as s:
        s.rankdir = "TB"
        add_person(s, husband)
        add_person(s, wife)
        s.edge(str(husband),point_name, tooltip=source, fontname="Arial", fontcolor="blue", fontsize="10" , penwidth="2" , color = "green")
        s.edge(point_name, str(wife), tooltip=source , fontname="Arial" , fontcolor="blue" , fontsize="10"  , penwidth="2" ,color="green")

def get_diagram_father_and_son(parentes, son, source):
    # parentes is string (E.g. "3" or "3+4")
    # son is always int
    # source is str (of course...)
    d = dot
    d.rankdir = "TB"
    if "+" in parentes:
        t = parentes.split("+")
        father = int(t[0])
        mother = int(t[1])
        add_person(d, father)
        add_person(d, mother)
        d.node(parentes , shape='point')
    else:
        father = int(parentes)
        add_person(d, father)

        parentes = str(father)
    add_person(d, son)
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
dot.render(r"dorot")
chrome_path = 'C:/Users/burstain/AppData/Local/Google/Chrome/Application/chrome.exe --profile-directory="Profile 1" %s'
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
dorot = os.path.join(os.path.dirname(__file__),"dorot.svg")
webbrowser.get(chrome_path).open(dorot)
