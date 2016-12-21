# MDP from the example by Sebastian Thrun in: https://www.youtube.com/watch?v=glHKJ359Cnc&t=44s
mdp = [[-3, -3, -3, 100], [-3, None, -3, -100], [-3, -3, -3, -3]]

# Initial Utilities
utilities = [[0, 0, 0, 100], [0, None, 0, -100], [0, 0, 0, 0]]

# Actions
# These are the actions the agent can perform,
# they are defined as lists which mark positional changes.
# See function transition(s, direction)
up = [-1, 0]
down = [1, 0]
left = [0, -1]
right = [0, 1]


def hit_wall(s):
    """Checks if the agents hit a wall.

    A wall in this World is defined as either entering a Position
    that exceeds the bounds of the mpd List or a Position that
    has None as its value.

    :param s: The position/state of the agent represented as a List of two ints
    :return: True, if agent would hit a wall with the next step
    """
    if s == [1, 1]:  # We would enter the None-Field
        return True
    elif s[0] < 0 or s[0] > 2 or s[1] < 0 or s[1] > 3:  # We would be out of bounds
        return True
    else:
        return False


def transition(s, direction):
    """The agent makes a transition in the world from on state into the next one

    The agent needs to move in the world. Therefore the action e.g. right can
    be added to the position of the agent.
    Example: Position = [0, 0], Action = right => [0 ,0] + [0, 1] = [0, 1]
    If the agents tries to move but would hit a wall the new position
    will be the old position.

    :param s: The position/state of the agent represented as a List of two ints
    :param direction: The direction in which the agent moves
    :return: The new position
    """
    new_pos = [sum(x) for x in zip(s, direction)]  # sum up every element at same index of two lists
    if hit_wall(new_pos):
        return s
    else:
        return new_pos


def get_utility(s, direction):
    """Gets the utility from a certain state s after action direction

    :param s: The position/state of the agent represented as a List of two ints
    :param direction: The direction in which the agent moves
    :return: The utility of the newly reached state
    """
    new_pos = transition(s, direction)
    new_utility = utilities[new_pos[0]][new_pos[1]]
    return new_utility


def value(s):
    """Equation that computes the value fpr every state s

    Designed after the Bellman Equation but in a simplified version.
    U(s) = R(s) + max(P(s'|s, a) U(s))
    The reward plus the max value of all neighbouring utilities mulitplied by their respective
    probability to reach the stat s'.

    :param s: The position/state of the agent represented as a List of two ints
    :return: None
    """
    utilities[s[0]][s[1]] = -3 + max(
        [0.8 * get_utility(s, up) + 0.1 * get_utility(s, left) + 0.1 * get_utility(s, right),  # go up
         0.8 * get_utility(s, down) + 0.1 * get_utility(s, left) + 0.1 * get_utility(s, right),  # go down
         0.8 * get_utility(s, right) + 0.1 * get_utility(s, up) + 0.1 * get_utility(s, down),  # go right
         0.8 * get_utility(s, left) + 0.1 * get_utility(s, up) + 0.1 * get_utility(s, down), ])  # go left
    # print(utilities)        #Uncomment to see the utilities of every iteration


def value_iteration(iterations):
    """Iterates through all the states and calculates value function

    :param iterations: Number of iterations, this is up to you. 100 is sufficient for this problem
    :return: None
    """
    for _ in range(0, iterations):
        for i in range(0, 3):
            for j in range(0, 4):
                if [i, j] == [1, 1] or [i, j] == [0, 3] or [i, j] == [1, 3]:
                    None
                else:
                    value([i, j])

    print(utilities)


value_iteration(100)
