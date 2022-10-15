from node import Node
import copy


class FifteensNode(Node):
    """Extends the Node class to solve the 15 puzzle.

    Parameters
    ----------
    parent : Node, optional
        The parent node. It is optional only if the input_str is provided. Default is None.

    g : int or float, optional
        The cost to reach this node from the start node : g(n).
        In this puzzle it is the number of moves to reach this node from the initial configuration.
        It is optional only if the input_str is provided. Default is 0.

    board : list of lists
        The two-dimensional list that describes the state. It is a 4x4 array of values 0, ..., 15.
        It is optional only if the input_str is provided. Default is None.

    input_str : str
        The input string to be parsed to create the board.
        The argument 'board' will be ignored, if input_str is provided.
        Example: input_str = '1 2 3 4\n5 6 7 8\n9 10 0 11\n13 14 15 12' # 0 represents the empty cell

    Examples
    ----------
    Initialization with an input string (Only the first/root construction call should be formatted like this):
    >>> n = FifteensNode(input_str=initial_state_str)
    >>> print(n)
      5  1  4  8
      7     2 11
      9  3 14 10
      6 13 15 12

    Generating a child node (All the child construction calls should be formatted like this) ::
    >>> n = FifteensNode(parent=p, g=p.g+c, board=updated_board)
    >>> print(n)
      5  1  4  8
      7  2    11
      9  3 14 10
      6 13 15 12

    """

    def __init__(self, parent=None, g=0, board=None, input_str=None):
        # NOTE: You shouldn't modify the constructor
        if input_str:
            self.board = []
            for i, line in enumerate(filter(None, input_str.splitlines())):
                self.board.append([int(n) for n in line.split()])
        else:
            self.board = board

        super(FifteensNode, self).__init__(parent, g)

    def generate_children(self):
        """Generates children by trying all 4 possible moves of the empty cell.

        Returns
        -------
            children : list of Nodes
                The list of child nodes.
                   up = 1, down =2, left=3, right=4
            根据合法移动规则生成2-4个节点，存入open表中
        """
        # TODO: add your code here
        # You should use self.board to produce children. Don't forget to create a new board for each child
        # e.g you can use copy.deepcopy function from the standard library.
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        if self.is_goal():
            print("*find the solution!*")
            return
        res = []
        x = self.find_zero()[0]  # row
        y = self.find_zero()[1]  # col
        child_g = self.g + 1
        if x > 0:
            # up
            s1 = copy.deepcopy(self.board)
            s1[x][y] = self.board[x - 1][y]
            s1[x - 1][y] = self.board[x][y]
            child_1 = FifteensNode(g=child_g, parent=self, board=s1)
            res.append(child_1)
        if x < 3:
            # down
            s2 = copy.deepcopy(self.board)
            s2[x][y] = self.board[x + 1][y]
            s2[x + 1][y] = self.board[x][y]
            child_2 = FifteensNode(g=child_g, parent=self, board=s2)
            res.append(child_2)
        if y > 0:
            # left
            s3 = copy.deepcopy(self.board)
            s3[x][y - 1] = self.board[x][y]
            s3[x][y] = self.board[x][y - 1]
            child_3 = FifteensNode(g=child_g, parent=self, board=s3)
            res.append(child_3)
        if y < 3:
            # right
            s4 = copy.deepcopy(self.board)
            s4[x][y + 1] = self.board[x][y]
            s4[x][y] = self.board[x][y + 1]
            child_4 = FifteensNode(g=child_g, parent=self, board=s4)
            res.append(child_4)
        return res
        pass

    def locate(self):
        pass

    def is_goal(self):
        """Decides whether this search state is the final state of the puzzle.

        Returns
        -------
            is_goal : bool
                True if this search state is the goal state, False otherwise.
        """

        # TODO: add your code here
        goalBoard = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
        if self.board == goalBoard:
            return True
        else:
            return False
        # You should use self.board to decide.

    def find_zero(self):
        loc = []
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 0:
                    loc.append(i)
                    loc.append(j)
                    break
        return loc

    pass

    def evaluate_heuristic(self):
        """Heuristic function h(n) that estimates the minimum number of moves
        required to reach the goal state from this node.

        Returns
        -------
            h : int or float
                The heuristic value for this state.
        """

        # TODO: add your code here
        # You may want to use self.board here.
        goalBoard = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
        diff = 0
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 0:
                    continue
                if self.board[i][j] != goalBoard[i][j]:
                    diff += 1
        return diff
        pass

    def _get_state(self):
        """Returns an hashable representation of this search state.

        Returns
        -------
            state: tuple
                The hashable representation of the search state
        """
        # NOTE: You shouldn't modify this method.
        return tuple([n for row in self.board for n in row])

    def __str__(self):
        """Returns the string representation of this node.

        Returns
        -------
            state_str : str
                The string representation of the node.
        """
        # NOTE: You shouldn't modify this method.
        sb = []  # String builder
        for row in self.board:
            for i in row:
                sb.append(' ')
                if i == 0:
                    sb.append('  ')
                else:
                    if i < 10:
                        sb.append(' ')
                    sb.append(str(i))
            sb.append('\n')
        return ''.join(sb)

    def findZero(self):
        pass


class SuperqueensNode(Node):
    """Extends the Node class to solve the Superqueens problem.

    Parameters
    ----------
    parent : Node, optional
        The parent node. Default is None.

    g : int or float, optional
        The cost to reach this node from the start node : g(n).
        In this problem it is the number of pairs of superqueens that can attack each other in this state configuration.
        Default is 1.

    queen_positions : list of pairs
        The list that stores the x and y positions of the queens in this state configuration.
        Example: [(q1_y,q1_x),(q2_y,q2_x)]. Note that the upper left corner is the origin and y increases downward
        Default is the empty list [].
        ------> x
        |
        |
        v
        y

    n : int
        The size of the board (n x n)

    Examples
    ----------
    Initialization with a board size (Only the first/root construction call should be formatted like this):
    >>> n = SuperqueensNode(n=4)
    >>> print(n)
         .  .  .  .
         .  .  .  .
         .  .  .  .
         .  .  .  .

    Generating a child node (All the child construction calls should be formatted like this):
    >>> n = SuperqueensNode(parent=p, g=p.g+c, queen_positions=updated_queen_positions, n=p.n)
    >>> print(n)
         Q  .  .  .
         .  .  .  .
         .  .  .  .
         .  .  .  .

    """

    def __init__(self, parent=None, g=0, queen_positions=[], n=1):
        # NOTE: You shouldn't modify the constructor
        self.queen_positions = queen_positions
        self.n = n
        super(SuperqueensNode, self).__init__(parent, g)

    def generate_children(self):
        """Generates children by adding a new queen.

        Returns
        -------
            children : list of Nodes
                The list of child nodes.
        """
        # TODO: add your code here
        # You should use self.queen_positions and self.n to produce children.
        # Don't forget to create a new queen_positions list for each child.
        # You can use copy.deepcopy function from the standard library.

        if self.is_goal():
            return
        col = []
        res = []
        length = len(self.queen_positions)
        for i in range(length):
            col.append(self.queen_positions[i][1])
        for i in range(self.n):
            if  i not in col :
                queen_positions = copy.deepcopy(self.queen_positions)
                queen_positions.append((length, i))
                child = SuperqueensNode(parent=self, g=self.g+self.evaluate_g(), queen_positions=queen_positions,n=self.n)
                res.append(child)
        return res
        pass

    def evaluate_g(self):
        g = 0
        length = len(self.queen_positions)
        for i in range(length):
            for j in range(length - i - 1):
                left = self.queen_positions[i]
                right = self.queen_positions[j]
                # 对角线
                if abs(left[0] - right[0]) == abs(left[1] - right[1]):
                    g += 1
                # 马走日
                if abs(left[0] - right[0]) == 2 * abs(left[1] - right[1]):
                    g += 1
                if 2 * abs(left[0] - right[0]) == abs(left[1] - right[1]):
                    g += 1
        return g
        pass

    def is_goal(self):
        """Decides whether all the queens are placed on the board.

        Returns
        -------
            is_goal : bool
                True if all the queens are placed on the board, False otherwise.
        """
        # You should use self.queen_positions and self.n to decide.
        # TODO: add your code here
        if self.n == len(self.queen_positions):
            return True
        else:
            return False
        pass

    def evaluate_heuristic(self):
        """Heuristic function h(n) that estimates the minimum number of conflicts required to reach the final state.

        Returns
        -------
            h : int or float
                The heuristic value for this state.
        """
        # If you want to design a heuristic for this problem, you should use self.queen_positions and self.n.
        # TODO: add your code here (optional)
        return 0

    def _get_state(self):
        """Returns an hashable representation of this search state.

        Returns
        -------
            state: tuple
                The hashable representation of the search state
        """
        # NOTE: You shouldn't modify this method.
        return tuple(self.queen_positions)

    def __str__(self):
        """Returns the string representation of this node.

        Returns
        -------
            state_str : str
                The string representation of the node.
        """
        # NOTE: You shouldn't modify this method.
        sb = [[' . '] * self.n for i in range(self.n)]  # String builder
        for i, j in self.queen_positions:
            sb[i][j] = ' Q '
        return '\n'.join([''.join(row) for row in sb])
