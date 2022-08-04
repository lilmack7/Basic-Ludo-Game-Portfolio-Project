# Author: Aidan MacKenzie
# GitHub username: aidanmackenzie
# Date: 07/31/2022
# Description: This code consists of a simplified game of Ludo. This game is made up of classes LudoGame and Player at
# a minimum. The player class contains at least the position the player chooses, the start and end space for the player,
# current position of their two tokens, and the current state of the player. It may contain additional information.
# Whereas the LudoGame object contains information about the players and information about the board.


class Board:
    """Represents the game board."""

    def __init__(self):
        """Creates a game board."""
        self._general_board_spots = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [],
                                      '10': [], '11': [], '12': [], '13': [], '14': [], '15': [], '16': [], '17': [],
                                      '18': [], '19': [], '20': [], '21': [], '22': [], '23': [], '24': [], '25': [],
                                      '26': [], '27': [], '28': [], '29': [], '30': [], '31': [], '32': [], '33': [],
                                      '34': [], '35': [], '36': [], '37': [], '38': [], '39': [], '40': [], '41': [],
                                      '42': [], '43': [], '44': [], '45': [], '46': [], '47': [], '48': [], '49': [],
                                      '50': [], '51': [], '52': [], '53': [], '54': [], '55': [], '56': []}

        self._a_board_spots = {"H": [], "R": [], "A1": [], "A2": [], "A3": [], "A4": [], "A5": [], "A6": [], "E": []}      # Possibly rename to just match step value
        self._b_board_spots = {"H": [], "R": [], "B1": [], "B2": [], "B3": [], "B4": [], "B5": [], "B6": [], "E": []}       # If I do that, adjust add/remove methods to match
        self._c_board_spots = {"H": [], "R": [], "C1": [], "C2": [], "C3": [], "C4": [], "C5": [], "C6": [], "E": []}
        self._d_board_spots = {"H": [], "R": [], "D1": [], "D2": [], "D3": [], "D4": [], "D5": [], "D6": [], "E": []}

    def get_general_board_spots(self):
        """Returns the general board spots and what is present on each."""
        return self._general_board_spots

    def get_a_board_spots(self):
        """Returns the unique board spots of player A and what is present on each."""
        return self._a_board_spots

    def get_b_board_spots(self):
        """Returns the unique board spots of player B and what is present on each."""
        return self._b_board_spots

    def get_c_board_spots(self):
        """Returns the unique board spots of player C and what is present on each."""
        return self._c_board_spots

    def get_d_board_spots(self):
        """Returns the unique board spots of player D and what is present on each."""
        return self._d_board_spots

    def general_add_token(self, spot_value, token_object):
        """Adds a token to a general board spot."""
        self._general_board_spots[spot_value].append(token_object)

    def a_add_token(self, spot_value, token_object):
        """Adds a token to an A player board spot."""
        if spot_value == "-1":
            self._a_board_spots["H"].append(token_object)

        elif spot_value == "0":
            self._a_board_spots["R"].append(token_object)

        elif spot_value == "57":
            self._a_board_spots["E"].append(token_object)

        else:
            inner_spot_value = f"A{int(spot_value) - 50}"
            self._a_board_spots[inner_spot_value].append(token_object)

    def b_add_token(self, spot_value, token_object):
        """Adds a token to a B player board spot."""
        if spot_value == "-1":
            self._b_board_spots["H"].append(token_object)

        elif spot_value == "0":
            self._b_board_spots["R"].append(token_object)

        elif spot_value == "57":
            self._b_board_spots["E"].append(token_object)

        else:
            inner_spot_value = f"B{int(spot_value) - 50}"
            self._b_board_spots[inner_spot_value].append(token_object)

    def c_add_token(self, spot_value, token_object):
        """Adds a token to a C player board spot."""
        if spot_value == "-1":
            self._c_board_spots["H"].append(token_object)

        elif spot_value == "0":
            self._c_board_spots["R"].append(token_object)

        elif spot_value == "57":
            self._c_board_spots["E"].append(token_object)

        else:
            inner_spot_value = f"C{int(spot_value) - 50}"
            self._c_board_spots[inner_spot_value].append(token_object)

    def d_add_token(self, spot_value, token_object):
        """Adds a token to a D player board spot."""
        if spot_value == "-1":
            self._d_board_spots["H"].append(token_object)

        elif spot_value == "0":
            self._d_board_spots["R"].append(token_object)

        elif spot_value == "57":
            self._d_board_spots["E"].append(token_object)

        else:
            inner_spot_value = f"D{int(spot_value) - 50}"
            self._d_board_spots[inner_spot_value].append(token_object)

    def general_remove_token(self, token_object):
        """Removes a token from a general board spot."""
        for key in self._general_board_spots:
            if token_object in self._general_board_spots[key]:
                self._general_board_spots[key].remove(token_object)

    def a_remove_token(self, token_object):
        """Removes a token from an A board spot"""
        for key in self._a_board_spots:
            if token_object in self._a_board_spots[key]:
                self._a_board_spots[key].remove(token_object)

    def b_remove_token(self, token_object):
        """Removes a token from a B board spot"""
        for key in self._b_board_spots:
            if token_object in self._b_board_spots[key]:
                self._b_board_spots[key].remove(token_object)

    def c_remove_token(self, token_object):
        """Removes a token from a C board spot"""
        for key in self._c_board_spots:
            if token_object in self._c_board_spots[key]:
                self._c_board_spots[key].remove(token_object)

    def d_remove_token(self, token_object):
        """Removes a token from a D board spot"""
        for key in self._d_board_spots:
            if token_object in self._d_board_spots[key]:
                self._d_board_spots[key].remove(token_object)


class Tokens:
    """Represents the player tokens."""

    def __init__(self, token_name, player_position):
        """Creates a Tokens object."""
        self._token_name = token_name
        self._token_player_position = player_position
        self._token_location = "-1"                 # Guess this will just be string of -1 to 57? Improve after works

    def get_token_name(self):
        """Returns the token name, p or q."""
        return self._token_name

    def get_token_player_position(self):
        """Returns the player position of the token in question"""
        return self._token_player_position

    def get_token_location(self):
        """Returns the token's location as a string of an integer ranging from -1 to 57."""
        return self._token_location

    def update_token_location(self, new_location):
        """Shifts token location to new value."""
        self._token_location = new_location


class Player:
    """Represents a player."""

    def __init__(self, player_position, start_pos, end_pos):        # Start pos and end pos may be determined here by player position or in LudoGame TBD
        self._player_tokens = [Tokens('p', player_position), Tokens('q', player_position)]
        self._player_position = player_position
        self._start_pos = start_pos
        self._end_pos = end_pos
        self._token_p_step_count = "-1"
        self._token_q_step_count = "-1"
        self._completed = False
        for token in self._player_tokens:
            if self._player_position == "A":
                board.a_add_token(token.get_token_location(), token)

            elif self._player_position == "B":
                board.b_add_token(token.get_token_location(), token)

            elif self._player_position == "C":
                board.c_add_token(token.get_token_location(), token)

            elif self._player_position == "D":
                board.d_add_token(token.get_token_location(), token)

    def get_player_position(self):
        """Returns the player's position."""
        return self._player_position

    def get_player_tokens(self):
        """Returns the players token objects."""
        return self._player_tokens

    def get_token_p_step_count(self):
        """Returns the total steps that token p has taken."""
        return self._token_p_step_count

    def get_token_q_step_count(self):
        """Returns the total steps that token q has taken."""
        return self._token_q_step_count

    def update_step_count(self, token_name, new_step_count):
        """Updates the step count of the appropriate token."""
        if token_name == "p":
            self._token_p_step_count = new_step_count

        elif token_name == "q":
            self._token_q_step_count = new_step_count

    def get_completed(self):
        """Returns True if player has finished game, False otherwise."""
        if self._token_q_step_count == "57" and self._token_p_step_count == "57":
            return True

        else:
            return False

    def get_space_name(self, total_steps):
        """Returns the name of the space the token with given step count has landed on."""
        for token in self._player_tokens:
            if token.get_token_location() == str(total_steps):
                if str(total_steps) == "-1":
                    return "H"

                elif str(total_steps) == "0":
                    return "R"

                elif str(total_steps) == "57":
                    return "E"

                elif 50 < total_steps < 57:
                    return f"{self._player_position}{total_steps - 50}"

                elif total_steps + int(self._start_pos) - 57 == 0:
                    return "56"

                elif total_steps + int(self._start_pos) >= 57:
                    return f"{(total_steps + int(self._start_pos)) - 57}"

                else:
                    return f"{total_steps + int(self._start_pos) - 1}"



    def move_token(self, token_name, new_pos):    # Need to determine if new_pos will be string, currently coding as string
        """Moves a player's token from initial spot to new spot based on their 'roll'."""
        for token in self._player_tokens:
            if token.get_token_name() == token_name:
                if 1 <= int(token.get_token_location()) <= 50:
                    board.general_remove_token(token)
                    if int(new_pos) == -1:
                        if self._player_position == "A":
                            board.a_add_token("-1", token)

                        if self._player_position == "B":
                            board.b_add_token("-1", token)

                        if self._player_position == "C":
                            board.c_add_token("-1", token)

                        if self._player_position == "D":
                            board.d_add_token("-1", token)

                    elif int(new_pos) == 0:
                        if self._player_position == "A":
                            board.a_add_token("0", token)

                        if self._player_position == "B":
                            board.b_add_token("0", token)

                        if self._player_position == "C":
                            board.c_add_token("0", token)

                        if self._player_position == "D":
                            board.d_add_token("0", token)

                    elif 0 < int(new_pos) + int(self._start_pos) <= 56 and int(new_pos) < 51:
                        board.general_add_token(f"{int(new_pos) + int(self._start_pos)}", token)

                    elif int(new_pos) + int(self._start_pos) > 56 and int(new_pos) < 51:
                        board.general_add_token(f"{int(new_pos) - (57 - int(self._start_pos))}", token)

                    elif 57 > int(new_pos) >= 51:
                        if self._player_position == "A":
                            board.a_add_token(f"{self._player_position}{int(new_pos) - 50}", token)

                        if self._player_position == "B":
                            board.b_add_token(f"{self._player_position}{int(new_pos) - 50}", token)

                        if self._player_position == "C":
                            board.c_add_token(f"{self._player_position}{int(new_pos) - 50}", token)

                        if self._player_position == "D":
                            board.d_add_token(f"{self._player_position}{int(new_pos) - 50}", token)

                else:
                    if self._player_position == "A":
                        board.a_remove_token(token)
                        if new_pos == "-1":
                            board.a_add_token("-1", token)

                        if new_pos == "0":
                            board.a_add_token("0", token)

                        elif 0 < (int(new_pos) + int(self._start_pos) - 1) <= 56 and int(new_pos) < 51:
                            board.general_add_token(f"{int(new_pos) + int(self._start_pos) - 1}", token)

                        elif int(new_pos) + int(self._start_pos) - 1 >= 56 and int(new_pos) < 51:
                            board.general_add_token(f"{int(new_pos) - (57 - int(self._start_pos))}", token)

                        elif 51 <= int(new_pos) <= 57 or int(new_pos) == -1 or int(new_pos) == 0:
                            board.a_add_token(new_pos, token)

                        elif int(new_pos) > 57:
                            bounce_pos = str(57 - (int(new_pos) - 57))
                            return self.move_token(token_name, bounce_pos)

                    elif self._player_position == "B":
                        board.b_remove_token(token)
                        if new_pos == "-1":
                            board.b_add_token("-1", token)

                        if new_pos == "0":
                            board.b_add_token("0", token)

                        elif 0 < (int(new_pos) + int(self._start_pos) - 1) <= 56 and int(new_pos) < 51:
                            board.general_add_token(f"{int(new_pos) + int(self._start_pos) - 1}", token)

                        elif int(new_pos) + int(self._start_pos) -1 >= 56 and int(new_pos) < 51:
                            board.general_add_token(f"{int(new_pos) - (57 - int(self._start_pos))}", token)

                        elif 51 <= int(new_pos) <= 57 or int(new_pos) == -1 or int(new_pos) == 0:
                            board.b_add_token(new_pos, token)

                        elif int(new_pos) > 57:
                            bounce_pos = str(57 - (int(new_pos) - 57))
                            return self.move_token(token_name, bounce_pos)

                    elif self._player_position == "C":
                        board.c_remove_token(token)
                        if new_pos == "-1":
                            board.c_add_token("-1", token)

                        if new_pos == "0":
                            board.c_add_token("0", token)

                        elif 0 < (int(new_pos) + int(self._start_pos) - 1) <= 56 and int(new_pos) < 51:
                            board.general_add_token(f"{int(new_pos) + int(self._start_pos) - 1}", token)

                        elif int(new_pos) + int(self._start_pos) - 1 >= 56 and int(new_pos) < 51:
                            board.general_add_token(f"{int(new_pos) - (57 - int(self._start_pos))}", token)

                        elif 51 <= int(new_pos) <= 57 or int(new_pos) == -1 or int(new_pos) == 0:
                            board.c_add_token(new_pos, token)

                        elif int(new_pos) > 57:
                            bounce_pos = str(57 - (int(new_pos) - 57))
                            return self.move_token(token_name, bounce_pos)

                    elif self._player_position == "D":
                        board.d_remove_token(token)
                        if new_pos == "-1":
                            board.d_add_token("-1", token)

                        if new_pos == "0":
                            board.d_add_token("0", token)

                        elif 0 < (int(new_pos) + int(self._start_pos) - 1) <= 56 and int(new_pos) < 51:
                            board.general_add_token(f"{int(new_pos) + int(self._start_pos) - 1}", token)

                        elif int(new_pos) + int(self._start_pos) - 1 >= 56 and int(new_pos) < 51:
                            board.general_add_token(f"{int(new_pos) - (57 - int(self._start_pos))}", token)

                        elif 51 <= int(new_pos) <= 57 or int(new_pos) == -1 or int(new_pos) == 0:
                            board.d_add_token(new_pos, token)

                        elif int(new_pos) > 57:
                            bounce_pos = str(57 - (int(new_pos) - 57))
                            return self.move_token(token_name, bounce_pos)

                token.update_token_location(new_pos)
                self.update_step_count(token_name, new_pos)


class LudoGame:
    """Represents the game as played."""

    def __init__(self):
        """Creates a LudoGame object."""        # Add more to init
        self._board = Board()

    def get_board(self):
        """Returns the game board for current game."""
        return self._board

    # Where the game is actually played. Makes local objects?
    # Should consider dictionary with player object as key, tokens as values in list
    # For player creation: for playa in players: if playa == "A": (player object list).append(Player("A", "1", "50")
    # get_player_by_position used to assign actual object to player variable like player_A
    # May need to shift board used in previous code into a get_board line

board = Board()
player_A = Player("A", "1", "50")
player_A.move_token("p", "57")
player_A.move_token("q", "57")
print(player_A.get_token_p_step_count())
print(player_A.get_token_q_step_count())
#print(player_A.get_space_name(57))
print(player_A.get_completed())
print(board.get_general_board_spots())
print(board.get_a_board_spots())

player_C = Player("C", "29", "22")
player_C.move_token("p", "29")