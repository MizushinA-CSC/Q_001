# 入力文字列Sに対し、入力自然数NだけSの前に"a"を加える

# 標準入力
S = str(input())
N = int(input())

# 標準入力の代わり
#S: str = "x"
#N: int = 2

for i in range(0, N):
    S = "a" + S

print(S)
