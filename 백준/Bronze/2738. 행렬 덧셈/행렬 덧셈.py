def make_matrix(N,M):
    A = []
    B = []
    for i in range(N*2):
        row = list(map(int, input().split()))
        if len(row) > M:
            print("행렬의 길이를 다시 확인해주세요")
            break
        else:
            if i < N:
                A.append(row)
            else:
                B.append(row)
    return A, B


def sum_matrix(A,B):
    return list(map(str,[A[i][j]+B[i][j] for i in range(N) for j in range(M)]))

def make_result(sum_matrix_list):
    for i in range(0,N*M,M):
        print(" ".join(j for j in sum_matrix_list[i:i+M]))
    
N, M = map(int, input().split())
A, B = make_matrix(N,M)
sum_list = sum_matrix(A,B)
make_result(sum_list)