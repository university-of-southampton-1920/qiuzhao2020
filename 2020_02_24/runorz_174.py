class Solution:
  def calculateMinimumHP(self, dungeon):
    need = [[None for _ in range(len(dungeon[0]))]for _ in range(len(dungeon))]
    # for i in range(len(need[len(dungeon)])):
    #   need[len(dungeon)][i] = 1
    # for i in range(len(need)):
    #   need[i][len(dungeon[0])] = 1
    for rindex in range(len(dungeon)-1, -1, -1):
      for cindex in range(len(dungeon[0])-1, -1, -1):
        if rindex == len(dungeon)-1 and cindex == len(dungeon[0]) - 1:
          n = -dungeon[rindex][cindex]
          need[rindex][cindex] = n+1 if n > 0 else 1
        elif rindex == len(dungeon)-1:
          n = need[rindex][cindex+1] - dungeon[rindex][cindex]
          need[rindex][cindex] = n if n > 0 else 1
        elif cindex == len(dungeon[0])-1:
          n = need[rindex+1][cindex] - dungeon[rindex][cindex]
          need[rindex][cindex] = n if n > 0 else 1
        else:
          n = min(need[rindex+1][cindex], need[rindex][cindex+1]) - dungeon[rindex][cindex]
          need[rindex][cindex] = 1 if n <= 0 else n
    print(need)
    return need[0][0]
