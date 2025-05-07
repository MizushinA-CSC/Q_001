# 入力文字列Sに対し、以下の操作を行う
# (1) 入力自然数NだけSの末尾に"a"を加える操作を行う
# (2) i回の追加において、与える"a"の個数はp(i)と表される
# (3) "a"を末尾に追加する前に、必ず" "(半角スペース)が加えられる
# (4) "a"の追加は、0以上とする

# 標準入力
S = str(input())
N = int(input())
p = list(map(int, input().split()))

# 標準入力の代わり
#S: str = "Snorlax"
#N: int = 3
#p = [3, 2, 5]

for i in range(0, N):
    S += " "
    for p_i in range(0, p[i]):
        S += "a"

print(S)
