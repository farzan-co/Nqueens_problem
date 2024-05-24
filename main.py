def nqueens(n):
    col = set()
    posdiag = set() 
    negdiag = set()
    result = []
    board = [[".\t"]*n for i in range(n)]

    def solution(r):
        if r == n:
            copy = ["".join(row) for row in board]
            result.append(copy)
            return
        
        for c in range(n):
            if c in col or r+c in posdiag or r-c in negdiag:
                continue

            col.add(c)
            posdiag.add(r+c)
            negdiag.add(r-c)
            board[r][c] = "Q\t"

            solution(r+1)

            col.remove(c)
            posdiag.remove(r+c)
            negdiag.remove(r-c)
            board[r][c] = ".\t"
    
    solution(0)
    
    print("Numbers of solutions:")
    print(len(result))
    
    if len(result) != 0:
        print("Solutions:")
        situations = range(len(result))
        for i in situations:
            print(f"{i+1}:")
            for j in result[i]:
                print(f"{j}\n")

n = int(input("Enter the number of queens: "))

if n == 0:
    print("Invalid number !")
else:
    nqueens(n)