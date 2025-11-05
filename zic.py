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

class Bid:
    def __init__(self, price, trader): #trader should be an actual trader
        self.bid_price = price
        self.trader = trader
    
class Ask:
    def __init__(self, price, trader):
        self.ask_price = price
        self.trader = trader

class MarketEnv:

    # the "market price" is just that because there is only one asset in the market
    # what is happening is that the market holds the agents, and then when the market needs to be "broadcast" it just makes
    # every agent observe the information they need to observe

    def __init__(self, traders, init_price = 100):
        self.price = init_price
        self.traders = traders # array of Traders
        self.bids = []
        self.asks = []

    def step(self, actions):
       self.bids = [b for b in actions if isinstance(b, Bid)]
       self.asks = [a for a in actions if isinstance(a, Bid)]

    def calculate_trade_price(bid, ask): # can change this
        return (bid + ask) / 2.0


    def broadcast_state(self):
        for a in self.agents:
            a.observe(self.price)

    def match_bid_and_ask(self): # idk if they need to like have the same bid amount or smth, im assuming that only 1 unit of the asset is being traded
        if not self.bids or not self.asks:
            return None # no trade occured
        
        best_bid = max(self.bids, key = lambda b: b.price, default=None)
        best_ask = min(self.bids, key=lambda a: a.price, defautlt=None)
        
        if best_bid is None or best_ask is None:
            return None #also no trade
        if best_bid.price >= best_ask.price:
            trade_price = self.calculate_trade_price(best_bid, best_ask)
            best_bid.trader.asset += 1 # can change this to be however many units are being traded
            best_bid.trader.cash -= trade_price
            best_ask.trader.asset -= 1
            best_ask.trader.cash += trade_price
        
        
        return None # if there is no crossover between the best bid and the best ask
        



class Trader:
    def __init__(self, id): # id ∈ ℕ
        self.id = id,
        self.cash = 100,
        self.asset = 5

    def decide(self, price):
        return 5
        # what is the policy ??
        # can return a buy_offer or ask_price


    def observe(self, new_price):
        # somehow update the policy
        return 5


    