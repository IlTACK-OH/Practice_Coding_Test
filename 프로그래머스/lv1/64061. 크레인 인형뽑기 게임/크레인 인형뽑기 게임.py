def solution(board, moves):
    len_col = len(board[0])
    new_board = []
    catch_list = [0]
    score = 0
    """
    함수를 뒤집어서 [0] 인덱스에는 1번에 담긴 정보 리스트가
    오도록 만들어주는 영역입니다.
    """
    for _ in range(len_col):
        new_board.append([])
    
    for i in board:
        num_row = 0
        for j in i:
            if j:
                new_board[num_row].append(j)
            num_row += 1
    for i in range(len_col):
        new_board[i].reverse()
        
    # --------------------------------------
    for i in moves:
        if new_board[i-1]:
            catch = new_board[i-1].pop()
            if catch_list[-1] == catch:
                score += 2
                catch_list.pop()
            else:
                catch_list.append(catch)
    
    return score