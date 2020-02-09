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

N = int(input())
K = int(input())

oder_N = len(str(N))
num_zero = oder_N - K

res = 0

if K == 1:
    res = (num_zero + 1) * 9
    res -=  (9 - int(str(N)[0:-2]))

if K ==2:
    res = (num_zero + 1) * 9
    res -=  (9 - int(str(N)[0:-2]))
else:
    res = (num_zero + 1) * 9
    res -=  (9 - int(str(N)[0:-2]))
print(res)
