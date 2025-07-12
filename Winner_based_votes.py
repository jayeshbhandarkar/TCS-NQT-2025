def find_winner(n, m, votes):
    vote_count = {}

    for vote in votes:
        if vote in vote_count:
            vote_count[vote] += 1
        else:
            vote_count[vote] = 1

    total_votes = sum(vote_count.values())

    max_votes = max(vote_count.values())

    winners = []
    for candidate, count in vote_count.items():
        if count == max_votes:
            winners.append(candidate)

    if len(winners) > 1:
        return "No Winner"

    winner = winners[0]

    if vote_count[winner] > total_votes / 2:
        return winner
    else:
        return "No Winner"

n = int(input())
m = int(input())
votes = input().split(',')
print(find_winner(n, m, votes))
