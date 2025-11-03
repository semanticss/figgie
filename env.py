import random
# two agents, one assets, fixed supply, fixed time
# the environment holds public information, like prices, order book, public time
# each agent is essentially a private state, like cash, inventories, and beliefs
# each agent chooses actions at discrete time intervals
# the loop kinda goes like agents act, the market clears, new prices, agents observe REPEAT
# the feedback is basically the profit or loss

# there is an observation space, which is the data that every agent in the market sees (last trade,
# their own cash, other agent's quotes)
# there is an action space, which is what choices each person can make (buy / sell quantites, prices)
# there is a transition function, which decides how actions change the market state
# the reward function changes whose hands the wealth is in
# pretty good approximation of real markets -- decentralized decisions, local + global info, global price

class MarketEnv:

    # the "market price" is just that because there is only one asset in the market
     def __init__(self, init_price = 100):
        self.price = init_price
        self.agent_states = {
            0: {"cash": 1000, "asset": 5},
            1: {"cash": 1000, "asset": 5}
        }

    def step(self, actions):
        a0, a1 = actions
        trade = None

