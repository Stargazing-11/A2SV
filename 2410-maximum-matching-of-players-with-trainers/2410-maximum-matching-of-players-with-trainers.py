class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        player, trainer = 0, 0
        counter = 0
        players.sort()
        trainers.sort()
        while player < len(players) and trainer < len(trainers):
            if players[player] <= trainers[trainer]:
                counter += 1
                player += 1
            trainer += 1
        return counter 