# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\D\D_input.txt', 'r', encoding="utf-8")
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
N, K = [int(item) for item in input().split()]
N_list = [int(item) for item in input().split()]

k_list = [(i+1)/2 for i in N_list]


memo = sum(k_list[0:K])
accum_list = [memo]

for i in range(N-K):
    memo += k_list[i+K] - k_list[i]
    accum_list.append(memo)

print(max(accum_list))

