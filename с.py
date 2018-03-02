from copy import copy

g, d, f = list(map(int, input().split(' ')))

g_arr = list(map(int, input().split(' ')))
d_arr = list(map(int, input().split(' ')))
f_arr = list(map(int, input().split(' ')))


class Graph():
    def __init__(self, number, mn, mx):
        self.mn = mn
        self.mx = mx
        self.n = number
        self.childrens = []

    def add(self, child):
        self.childrens.append(child)


def srav(num, added, gr, letter):
    if num < gr.mn:
        if num * 2 < gr.mx:
            cp_added = copy(added)
            cp_added[letter] += 1
            cp_added['used'].add(num)
            # gr.add(recu(Graph(num, num, gr.mx), cp_added))
            return [cp_added, Graph(num, gr.mn, num)]
    elif num > gr.mx:
        if gr.mn * 2 < num:
            cp_added = copy(added)
            cp_added[letter] += 1
            cp_added['used'].add(num)
            return [cp_added, Graph(num, gr.mn, num)]
            # gr.add(recu(Graph(num, gr.mn, num), cp_added))
    else:
        cp_added = copy(added)
        cp_added[letter] += 1
        cp_added['used'].add(num)
        return [cp_added, Graph(num, gr.mn, num)]
        # gr.add(recu(Graph(num, gr.mn, num), cp_added))


def recu(gr, added):
    if added['g']:
        if added['d'] == 2:
            if added['f'] == 3:
                return gr
            else:
                for num in f_arr:
                    if num not in added['used']:
                        pass

        # else:
