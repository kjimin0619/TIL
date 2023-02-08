# 심사문제 : 지뢰찾기
# * : 지뢰 | col : 가로크기(열) | row : 세로크기(행)
# 행+-1, 열+-1, 행+-1&열+-1 값이 *(지뢰) 이면 +1
row, col = map(int, input().split())
mine_matrix = []
for i in range(row):
    mine_matrix.append(list(input()))

# x,i / y,j
for x in range(row) :
    for y in range(col):
        cnt_mine = 0
        # 지뢰 찾기 
        for i in range(row) :
            for j in range(col):
                # 본인이 지뢰인 경우
                if mine_matrix[x][y] == '*':
                    cnt_mine = '*'
                # 주변 지뢰 탐색
                elif abs(x-i) <= 1 and abs(y-j) <= 1 and mine_matrix[i][j] == '*':
                    cnt_mine += 1
   
        print(cnt_mine,end='')
    print()
            
