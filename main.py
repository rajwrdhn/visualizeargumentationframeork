import networkx as nx
import matplotlib.pyplot as plt
#Visualizing directed graph using networkx

def main():
    #read aa benchmark file
    G = nx.DiGraph()
    arguments, attacks = open_aa_file()
    G.add_nodes_from(arguments)
    G.add_edges_from(attacks)
    nx.draw(G)
    plt.show()

def open_aa_file()-> tuple[list, list]:
    arguments = []
    attacks = []
    with open("./af_nbr20_500_3_0.4", "r") as aa:
        for arg_att in aa:
            try:
                if arg_att.startswith("arg"):
                    arg_num = arg_att.removeprefix("arg(").removesuffix(").\n")
                    arguments.append(arg_num)
                if arg_att.startswith("att"):
                    att_num, att_num2 = arg_att.removeprefix("att(").removesuffix(").\n").split(",")
                    attacks.append((att_num,att_num2))

            except Exception as e:
                print("Error : ", e)

    return arguments, attacks

if __name__ == "__main__":
    main()