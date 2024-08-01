"""You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome."""
from collections import defaultdict

matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]

def findWinners(matches):

  lost_counts = defaultdict(int)
  res = [[],[]]

  for match in matches:
    if match[0] not in lost_counts:
      lost_counts[match[0]] = 0
    lost_counts[match[1]] += 1
  
  for player, count in lost_counts.items():
    if count == 0:
      res[0].append(player)
    if count == 1:
      res[1].append(player)
  
  return [sorted(res[0]), sorted(res[1])]

print(findWinners(matches))
    
