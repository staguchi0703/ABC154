# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\E\E_input.txt', 'r', encoding="utf-8")
# inputをフルパスで指定
# win10でファイルを作るとs-jisで保存されるため、読み込みをutf-8へエンコードする必要あり
# VScodeでinput file開くとutf8になってるんだけど中身は結局s-jisになっているらしい
sys.stdin=f

#
# 入力スニペット
# num = int(input())
# num_list = [int(item) for item in input().split()]
# num_list = [input() for _ in range(3)]
##################################
# %%
# 以下ペースト可
import numpy as np

N = int(input())
K = int(input())

N_str = str(N)
oder_N = len(N_str)

dp = np.zeros((oder_N+1, K+1, 2), dtype='int32')
dp[0, 0, 0] = 1

for i in range(oder_N):
    temp_num = int(N_str[i])
    for j in range(K):
        for k in range(2):
            for d in range(10):
                ni = i + 1
                nj = j
                nk = k

                if d != 0:
                    nj += 1
                if nj > K:
                    continue
                if k == 0:
                    if d > temp_num:
                        continue
                    if d < temp_num:
                        nk = 1

            dp[ni, nj, nk] += dp[i, j ,k]
            

print(dp)