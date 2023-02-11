class RecentCounter:

    def __init__(self):
        self.pings = []

    def ping(self, t: int) -> int:

        self.pings.append(t)

        # Remove pings less than 3000 unit old from start of queue
        low_limit = (t - 3000)
        while self.pings and self.pings[0] < low_limit:
            self.pings.pop(0)

        return len(self.pings)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
