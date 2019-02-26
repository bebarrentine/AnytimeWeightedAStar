import math


class Puzzle:
    """Implementation of the sliding tile puzzle."""
    # The actions available in this environment are sliding the blank space
    # up, down, left or right. These actions are encoded as integers in this
    # implementation.
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


    def __init__(self, i=None, j=None, state=[]):
        """Initialize a new sliding tile puzzle.

        Keyword arguments:
        - `i`: The number of rows in the puzzle.
        - `j`: The number of columns in the puzzle.
        - `state` (optional): A list representing the configuration of tiles
          in the puzzle. If no state is passed, then the puzzle has the
          configuration of the goal state.
        """

        # Knowing the dimensions of the puzzle is important for computing
        # legality of moves and heuristic functions.
        self.num_rows = i
        self.num_cols = j

        # `state.configuration` is a list that temporarily stores the puzzle's
        # state. This list will be converted to an integer later to speed up
        # creating new states.
        if state:
            # If passed, a puzzle configuration is saved.
            self.configuration = state[:]
        else:
            # If no configuration was passed, then generate a new
            # configuration. The default configuration is:
            #
            #     [0, 1, 2, 3, 4, 5, 6, 7, 8]
            #
            # for a 3x3 puzzle.
            self.configuration = []
            for i in range(i * j):
                self.configuration.append(i)

        return

    def find_blank(self):
        """Return the position of the blank space.
        
        The blank isn't explicitly passed during construction, so it's
        necessary to search for it.

        Typically, this is only used once for an unpacked state. One a state
        is packed, the blank position is always known.

        Returns the index of the blank position in the 1-D list.
        """
        try:
            if self.blank_pos:
                return self.blank_pos
        except:
            None

        try:
            # If this attribute doesn't exist, then the state needs to be
            # packed.
            self.places
        except:
            self.update_signature()

        # Sequentially search the puzzle for the blank space.
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if 0 == self.tile_at(i=i, j=j):
                    # Found the blank, so save its place.
                    self.blank_pos = i * self.num_rows + j
                    break

        return self.blank_pos


    def calculate_shift(self, i):
        """Return the number count of binary shifts to find the tile at i."""
        # The calculation depends on knowing how many bits it takes to encode
        # all of the tiles in binary.
        try:
            return (self.num_cells - i - 1) * self.places
        except:
            # So if the state wasn't packed then pack it and try again.
            self.update_signature()

            return self.calculate_shift(i)

    def tile_at(self, i=None, j=None):
        """Returns the value of the tile at `(i, j)`.
        
        `0` is the value of the blank.
        """

        # Multiplying row index `i` by the number of rows in the puzzle and
        # then adding the column index `j` reveals the index of the
        # sought-after tile in the packed puzzle state.
        index = i * self.num_rows + j

        # Make sure the state was packed before attempting to determine the
        # tile value at (i, j).
        try:
            return self.signature >> self.calculate_shift(index) \
                & self.max_tile_value
        except AttributeError:
            self.update_signature()

            return self.tile_at(i=i, j=j)

    def move(self, direction=None):
        """Swap the blank with a tile next to it.
        
        Keyword arguments:
        - `direction`: Can be `Puzzle.UP`, `Puzzle.DOWN`, `Puzzle.LEFT`,
          `Puzzle.RIGHT`.
        
        If it's not possible to swap the blank, then it fails silently and no
        change to the puzzle configuration occurs.
        """
        # Make sure it's possible to move in this direction.
        if self.can_move(direction):
            # If the blank position isn't known then find it first.
            if not self.blank_pos:
                self.find_blank()

            # Using the value of the old blank position for the new one makes
            # it easier to update because we can just add or subract the
            # values we need from the old blank to update it.
            new_blank = self.blank_pos
        
            # Update the new blank position based on the direction of the
            # swap.
            #
            # Up and down directions merely add or subtract the number of rows
            # in the puzzle to update its linear position.
            if direction == self.UP:
                new_blank -= self.num_rows
            elif direction == self.DOWN:
                new_blank += self.num_rows
            # Left and right directions add or subtract one to move into
            # different columns.
            elif direction == self.LEFT:
                new_blank -= 1
            elif direction == self.RIGHT:
                new_blank += 1

            # Slide the tile currently in the new blank position into the
            # current blank position.
            self.swap_tiles(new_blank, self.blank_pos)
            # Then update the puzzle's blank position.
            self.blank_pos = new_blank

    def swap_tiles(self, i=0, j=0):
        """Swap a tile in position i with the tile in position j.

        Keyword arguments:
        - `i`: An index into the 1-D list that represents the state of the
          puzzle. The tile in position i moves into position j.
        - `j`: An index into the 1-D list that represents the state of the
          puzzle. The tile in position j moves into position i.

        This method does not check to see if the move is legal, so be careful!
        """
        try:
            # Shift the packed state so that we can binary AND it to get the
            # tile's value.
            i_shift = self.calculate_shift(i)
            i_value = self.signature >> i_shift & self.max_tile_value

            j_shift = self.calculate_shift(j)
            j_value = self.signature >> j_shift & self.max_tile_value

            # Subtract the tile's value at i with itself so it leaves a
            # substring of 0s in the packed state.
            self.signature -= i_value << i_shift
            # Shift j's value to have the same position as i in the packed
            # state and add it to the packed state.
            #
            # This accomplished the swap.
            self.signature += j_value << i_shift

            # Now swap i into j's place.
            self.signature -= j_value << j_shift
            self.signature += i_value << j_shift
        except AttributeError:
            # If the state wasn't packed yet, go ahead and pack it now.
            self.update_signature()
            self.swap_tiles(i=i, j=j)

        return

    def calculate_num_cells(self):
        """Computes and stores the number of cells in the puzzle."""
        self.num_cells = self.num_rows * self.num_cols

        return

    def calculate_places(self):
        """Compute and store the number of bits needed to encode a tile."""
        
        # Max tile value is 8 == 0b1000,
        #
        #     4 == math.ceil(math.log2(9))
        #
        self.places = math.ceil(math.log2(self.num_cells))
        # Determine the largest number that can be represented in the number
        # of bits stored in `self.places`.
        #
        # This value is ANDed with the packed state to determine values of
        # tiles at specified positions.
        self.max_tile_value = 2 ** self.places - 1

        return

    def pack_state(self, state=[]):
        """Pack a list of non-negative integers into an integer."""
        packed_state = 0

        # For each row in the puzzle:
        for i in range(self.num_rows):
            # And for every tile in that row:
            for j in range(self.num_cols):
                # Determine the index of the tile in the puzzle configuration.
                index = i * self.num_rows + j
                # Determine the number of binary places to shift the tile's
                # value to the left.
                #
                # e.g. for the 8 puzzle,
                #
                #   * `num_cells` is the number of places in puzzle: 9
                #   * index is the current 1D coordinate of the tile in the
                #     puzzle configuration: 4
                #   * `places` is the number of places needed to store the
                #     maximum tile value: 4
                #
                # So:
                #
                #     (9 - 1 - 0) * 4 == (8) * 4 == 32 places  
                #     (9 - 1 - 1) * 4 == (7) * 4 == 28 places  
                #     (9 - 1 - 2) * 4 == (6) * 4 == 24 places  
                #     (9 - 1 - 3) * 4 == (5) * 4 == 20 places  
                #     (9 - 1 - 4) * 4 == (4) * 4 == 16 places  
                #     (9 - 1 - 5) * 4 == (3) * 4 == 12 places  
                #     (9 - 1 - 6) * 4 == (2) * 4 == 8 places  
                #     (9 - 1 - 7) * 4 == (1) * 4 == 4 places  
                #     (9 - 1 - 8) * 4 == (0) * 4 == 0 places  
                #
                #     000011112222333344445555666677778888
                #
                try:
                    shift_places = ((self.num_cells - 1) - index) \
                        * self.places
                except:
                    # Compute the number of places needed to store a tile's
                    # value in binary.
                    self.calculate_num_cells()
                    self.calculate_places()

                    shift_places = ((self.num_cells - 1) - index) \
                        * self.places

                # OR existing signature with packed tile value.
                packed_state = packed_state | (state[index] << shift_places)

        return packed_state


    def update_signature(self):
        """Update the packed state of the puzzle."""
        try:
            # Set the puzzle's packed state to 0, since we OR positions
            # together.
            self.signature = self.pack_state(state=self.configuration)

            del self.configuration
        except ValueError:
            None


    def __eq__(self, other):
        """Determine if one puzzle is equal to another puzzle."""
        try:
            return self.signature == other.signature
        except AttributeError:
            if not hasattr(self, "signature"):
                self.update_signature()

            if not hasattr(other, "signature"):
                other.update_signature()

            return self.__eq__(other)

    
    def can_move(self, direction=None):
        """Returns `True` if a move is legal and `False` if not."""
        result = False

        # Make sure the blank position is known.
        try:
            self.blank_pos
        except AttributeError:
            self.find_blank()

        # Can't move left if the blank is at the left edge.
        if Puzzle.LEFT == direction and 0 !=  self.blank_pos % self.num_rows:
            result = True
        # Can't move right if the blank is at the right edge.
        elif Puzzle.RIGHT == direction and \
            (self.num_cols - 1 > (self.blank_pos % self.num_cols)):
            result = True
        # Can't move down if the blank is at the bottom edge.
        elif Puzzle.DOWN == direction and \
            (self.blank_pos < (self.num_rows - 1) * self.num_cols):
            result = True
        # Can't move up if the blank is at the top edge.
        elif Puzzle.UP == direction and self.blank_pos >= self.num_rows:
            result = True

        return result 

    def __hash__(self):
        """Return the puzzle signature to be used for hashing."""
        # The puzzle's packed state is used for hashing, so check for it
        # before returning it.
        try:
            return self.signature
        except AttributeError:
            self.update_signature()

            return self.signature

