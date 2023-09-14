def solution(number):

    # 첫번째 자리부터 stack에 입력
    # 다시 함수로 돌아가서 두번째 자리 입력
    # 함수 돌려서 세번째 자리 입력하고 합이 0이면 count에 플러스
    # 마지막 자리까지 돌면 다시 두번째 자리 입력부터 돌기

    def solve(idx, number): 

        if len(stack) >= 3:
            # print(visited)
            if sum(stack) == 0 and (str(visited) not in visited_save):
                answer.append((sorted(stack)))
                visited_save.append(str(visited))
                # print(answer)
                # print('야호')
                # print(visited_save)
                return 
            return
    

        for i in range(len(number)):
            if visited[i] == False:          
                stack.append(number[i])
                # print(stack)
                visited[i] = True
                solve(idx+1, number)
                stack.remove(number[i])
                # print(stack)
                visited[i] = False

        return answer
        
    answer = []
    stack = []
    visited_save = []
    idx = 0
    
    visited = [False] * len(number)

    solve(idx, number)

    
    return len(answer)

print(solution([-2, 3, 0, 2, -5]))
print(solution([0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]))