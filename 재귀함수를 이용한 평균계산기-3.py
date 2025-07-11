# 재귀함수
n = int(input("입력한 숫자의 개수만큼 더한 후 평균을 출력합니다.>>>"))
count = n 
sum = 0

def sum_and_count(n):
  global sum
  if count == n:
    return sum, n
  else:
    num = int(input("숫자 입력 : "))
    sum += num
    return sum_and_count(n + 1)

# 숫자 3개 평균 출력
sum, n = sum_and_count(0)
print("총",n,"개 입력한 총합",sum, "의 평균은",round(sum/n,2),"입니다.")

