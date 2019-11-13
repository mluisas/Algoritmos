class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.p = None
        self.color = None
    def __str__(self):
        return str(self.data)


class RBTree:
    def __init__(self, data):
        null = Node(None)
        self.null = null
        self.null.color = 'Black'
        node = Node(data)
        self.root = node
        node.color = 'Black'
        self.root.left = null
        self.root.right = null
        node.p = null



    def iterative_search(self, x, k):
        while x is not self.null and k is not x.data:
            if k < x.data:
                x = x.left
            else:
                x = x.right
        return x

    def inorder_tree_walk(self, x):
        # Enquanto o nó não for sentinela
        if x is not self.null:
            # Visita a sub-árvore esquerda
            self.inorder_tree_walk(x.left)
            # Visita a raiz
            print(x.data, x.color)
            # Visita a sub-árvore direita
            self.inorder_tree_walk(x.right)

    def pre_order(self, x):
        # Enquanto o nó não for sentinela
        if x is not self.null:
            # Visita a raiz
            print(x.data, x.color)
            # Visita a sub-árvore esquerda
            self.pre_order(x.left)
            # Visita a sub-árvore direita
            self.pre_order(x.right)

    def pos_order(self, x):
        # Enquanto o nó não for sentinela
        if x is not self.null:
            # Visita a sub-árvore esquerda
            self.pos_order(x.left)
            # Visita a sub-árvore direita
            self.pos_order(x.right)
            # Visita a raiz
            print(x.data, x.color)

    # Retorna o elemento mais "a esquerda" da árvore
    def tree_minimum(self, x):
        while x.left is not self.null:
            x = x.left
        return x
    # Retorna o elemento mais "a direita" da árvore
    def tree_maximum(self, x):
        while x.right is not self.null:
            x = x.right
        return x

    # Retorna o nó mais à esquerda da subárvore direita
    def tree_successor(self, x):
        if x.right is not self.null:
            return self.tree_minimum(x.right)
        y = x.p
        while y is not self.null and x is y.right:
            x = y
            y = y.p
        return y
    # Retorna o nó mais à direita da subárvore esquerda
    def tree_predecessor(self, x):
        if x.left is not self.null:
            return self.tree_maximum(x.left)
        y = x.p
        while y is not self.null and x is y.left:
            x = y
            y = y.p
        return y

    def left_rotate(self, x):
        if x.right is not self.null:
            y = x.right
            x.right = y.left
            if y.left is not self.null:
                y.left.p = x
            y.p = x.p
            if x.p is self.null:
                self.root = y
            elif x is x.p.left:
                x.p.left = y
            else:
                x.p.right = y
            y.left = x
            x.p = y

    def right_rotate(self, x):
        if x.left is not self.null:
            y = x.left
            x.left = y.right
            if y.right is not self.null:
                y.right.p = x
            y.p = x.p
            if x.p is self.null:
                self.root = y
            elif x is x.p.right:
                x.p.right = y
            else:
                x.p.left = y
            y.right = x
            x.p = y

    def RB_insert_fixup(self, z):
        # Como z é vermelho, o único caso que quebra alguma das regras é quando o pai de z for vermelho
        while z.p.color == 'Red':

            if z.p is z.p.p.left:
                y = z.p.p.right
                if y.color == 'Red':
                    z.p.color = 'Black'
                    y.color = 'Black'
                    z.p.p.color = 'Red'
                    z = z.p.p
                elif z is z.p.right:
                    z = z.p
                    self.left_rotate(z)
                else:
                    z.p.color = 'Black'
                    z.p.p.color = 'Red'
                    self.right_rotate(z.p.p)
            else:
                y = z.p.p.left
                if y.color == 'Red':
                    z.p.color = 'Black'
                    y.color = 'Black'
                    z.p.p.color = 'Red'
                    z = z.p.p
                elif z is z.p.left:
                    z = z.p
                    self.right_rotate(z)
                else:
                    z.p.color = 'Black'
                    z.p.p.color = 'Red'
                    self.left_rotate(z.p.p)
        tree.root.color = 'Black'

    def RB_insert(self, z):
        y = self.null
        x = self.root
        while x is not self.null:
            y = x
            if z.data < x.data:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y is self.null:
            self.root = z
        elif z.data < y.data:
            y.left = z
        else:
            y.right = z
        z.left = self.null
        z.right = self.null
        z.color = 'Red'
        self.RB_insert_fixup(z)

    def RB_transplant(self, u, v):
        if u.p is self.null:
            self.root = v
        elif u is u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p
    
    def RB_delete_fixup(self, x):
        while x is not self.root and x.color == 'Black':
            if x is x.p.left:
                w = x.p.right
                if w.color == 'Red':
                    w.color = 'Black'
                    x.p.color = 'Red'
                    self.left_rotate(x.p)
                    w = x.p.right
                if w.left.color == 'Black' and w.right.color == 'Black':
                    w.color = 'Red'
                    x = x.p
                else:
                    if w.right.color == 'Black':
                        w.left.color = 'Black'
                        w.color = 'Red'
                        self.right_rotate(w)
                        w = x.p.right
                    w.color = x.p.color
                    x.p.color = 'Black'
                    w.right.color = 'Black'
                    self.left_rotate(x.p)
                    x = self.root
            else:
                w = x.p.left
                if w.color == 'Red':
                    w.color = 'Black'
                    x.p.color = 'Red'
                    self.right_rotate(x.p)
                    w = x.p.left
                if w.right.color == 'Black' and w.left.color == 'Black':
                    w.color = 'Red'
                    x = x.p
                else:
                    if w.left.color == 'Black':
                        w.right.color = 'Black'
                        w.color = 'Red'
                        self.left_rotate(w)
                        w = x.p.left
                    w.color = x.p.color
                    x.p.color = 'Black'
                    w.left.color = 'Black'
                    self.right_rotate(x.p)
                    x = self.root
        x.color = 'Black'

    def RB_delete(self, z):
        y = z
        y_original_color = y.color
        if z.left is self.null:
            x = z.right
            self.RB_transplant(z, z.right)
        elif z.right is self.null:
            x = z.left
            self.RB_transplant(z, z.left)
        else:
            y = self.tree_minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.p is z:
                x.p = y
            else:
                self.RB_transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.RB_transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if y_original_color is 'Black':
            self.RB_delete_fixup(x)


if __name__ == '__main__':
    opcao = 0
    while opcao < 10:
        opcao = int(input('''Digite a operação desejada:
    0 - Criar árvore
    1 - Inserir nós
    2 - Deletar nós
    3 - Predecessor
    4 - Sucessor
    5 - Mínimo
    6 - Máximo
    7 - Inorder-Walk
    8 - Pré-Ordem
    9 - Pós-Ordem
    10 - Sair\n'''))
        if opcao == 0:
            root = int(input('Digite o valor do nó raiz: '))
            tree = RBTree(root)
        if 'tree' in globals():
            if opcao == 1:
                quantidade = int(input('Quantos nós você deseja adicionar? '))
                for i in range(quantidade):
                    data = int(input('Digite o valor do nó a ser inserido: '))
                    tree.RB_insert(Node(data))

            elif opcao == 2:
                quantidade = int(input('Quantos nós você deseja deletar? '))
                for i in range(quantidade):
                    data = int(input('Digite o valor do nó a ser deletado: '))
                    node = tree.iterative_search(tree.root, data)
                    if node is not tree.null:
                        tree.RB_delete(node)

            elif opcao == 3:
                data = int(input('Digite o valor do nó: '))
                node = tree.iterative_search(tree.root, data)
                if node is not tree.null:
                    print(tree.tree_predecessor(node))

            elif opcao == 4:
                data = int(input('Digite o valor do nó: '))
                node = tree.iterative_search(tree.root, data)
                if node is not tree.null:
                    print(tree.tree_successor(node))

            elif opcao == 5:
                print(tree.tree_minimum(tree.root))

            elif opcao == 6:
                print(tree.tree_maximum(tree.root))

            elif opcao == 7:
                tree.inorder_tree_walk(tree.root)
            elif opcao == 8:
                tree.pre_order(tree.root)
            elif opcao == 9:
                tree.pos_order(tree.root)
        else:
            print('Você precisa criar uma árvore antes!')
