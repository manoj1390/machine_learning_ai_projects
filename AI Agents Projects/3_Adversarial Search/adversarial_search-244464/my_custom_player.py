
from sample_players import DataPlayer


class CustomPlayer(DataPlayer):
    """ Implement your own agent to play knight's Isolation

    The get_action() method is the only required method for this project.
    You can modify the interface for get_action by adding named parameters
    with default values, but the function MUST remain compatible with the
    default interface.

    **********************************************************************
    NOTES:
    - The test cases will NOT be run on a machine with GPU access, nor be
      suitable for using any other machine learning techniques.

    - You can pass state forward to your agent on the next turn by assigning
      any pickleable object to the self.context attribute.
    **********************************************************************
    """
    
    # Matrix for evaluation function
    MAT = [
        -4, -2, -2, -2, -2, -2, -2, -2, -2, -2, -4, float("-inf"), float("-inf"),
        -2,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, float("-inf"), float("-inf"),
        -2,  0,  0, 1, 1, 1, 1, 1,  0,  0, -2, float("-inf"), float("-inf"),
        -2,  0,  0, 1,  2,  2,  2, 1,  0,  0, -2, float("-inf"), float("-inf"),
        -2,  0,  0, 1,  2,  4,  2, 1,  0,  0, -2, float("-inf"), float("-inf"),
        -2,  0,  0, 1,  2,  2,  2, 1,  0,  0, -2, float("-inf"), float("-inf"),
        -2,  0,  0, 1,  1,  1,  1, 1, 0,  0, -2, float("-inf"), float("-inf"),
        -2,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, float("-inf"), float("-inf"),
        -4, -2, -2, -2, -2, -2, -2, -2, -2, -2, -4, float("-inf"), float("-inf"),
    ]
    def get_action(self, state):
        """ Employ an adversarial search technique to choose an action
        available in the current state calls self.queue.put(ACTION) at least

        This method must call self.queue.put(ACTION) at least once, and may
        call it as many times as you want; the caller will be responsible
        for cutting off the function after the search time limit has expired.

        See RandomPlayer and GreedyPlayer in sample_players for more examples.

        **********************************************************************
        NOTE: 
        - The caller is responsible for cutting off search, so calling
          get_action() from your own code will create an infinite loop!
          Refer to (and use!) the Isolation.play() function to run games.
        **********************************************************************
        """
        # TODO: Replace the example implementation below with your own search
        #       method by combining techniques from lecture
        #
        # EXAMPLE: choose a random move without any search--this function MUST
        #          call self.queue.put(ACTION) at least once before time expires
        #          (the timer is automatically managed for you)
        import random
        if state.ply_count < 2:
            self.queue.put(random.choice(state.actions()))
        #else:
        #    self.queue.put(self.minimax(state, depth=3))
        else:

            # Iterative Deepening
            for i in range(3, 32):
                #self.queue.put(self.minimax(state, depth=i))
                self.queue.put(self.alphabeta(state, depth=i))
        
    def minimax(self, state, depth):

            def min_value(state, depth):
                if state.terminal_test(): 
                    return state.utility(self.player_id)
                if depth <= 0: 
                    return self.score(state)
                value = float("inf")
                for action in state.actions():
                    value = min(value, max_value(state.result(action), depth - 1))
                return value

            def max_value(state, depth):
                if state.terminal_test(): 
                    return state.utility(self.player_id)
                if depth <= 0: 
                    return self.score(state)
                value = float("-inf")
                for action in state.actions():
                    value = max(value, min_value(state.result(action), depth - 1))
                return value

            return max(state.actions(), key=lambda x: min_value(state.result(x), depth - 1))
    

    def alphabeta(self, state, depth):
        """
        Minimax + alpha-beta pruning.
        """
        def min_value(state, depth, alpha, beta):
            if state.terminal_test(): 
                return state.utility(self.player_id)
            if depth <= 0: 
                return self.score(state)
            value = float("inf")
            for action in state.actions():
                value = min(value, max_value(state.result(action), depth - 1, alpha, beta))
                beta = min(beta, value)
                if beta <= alpha: 
                    break
            return value

        def max_value(state, depth, alpha, beta):
            if state.terminal_test(): return state.utility(self.player_id)
            if depth <= 0: return self.score(state)
            value = float("-inf")
            for action in state.actions():
                value = max(value, min_value(state.result(action), depth - 1, alpha, beta))
                alpha = max(alpha, value)
                if beta <= alpha: break
            return value
        return max(state.actions(), key=lambda x: min_value(state.result(x), depth - 1, float("-inf"), float("inf")))
    
    
    def score(self, state):
        own_loc = state.locs[self.player_id]
        opp_loc = state.locs[1 - self.player_id]
        own_liberties = state.liberties(own_loc)
        opp_liberties = state.liberties(opp_loc)
        return len(own_liberties) - len(opp_liberties) + self.MAT[own_loc] - self.MAT[opp_loc]