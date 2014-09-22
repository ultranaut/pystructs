import bst

st = bst.BinarySearchTree()
nt = bst.BinarySearchTree()

def setup():
    global st
    global nt

    for c in ('h', 'c', 'a', 'e', 's', 'r', 'x'):
        st.insert(c)

    for d in (50, 17, 76, 9, 23, 54, 14, 19, 72, 12, 67):
        nt.insert(d)


def test(levels):
    while len(levels):
        level = levels.pop(0)
        string = len(levels) * 4 * ' '
        for n in level:
            if not n:
                string += 4 * ' '
            else:
                string += ' '
                if n < 10:
                        string += ' '
                string += str(n) + ' '
            string += len(levels) * 4 * ' '
        print string
