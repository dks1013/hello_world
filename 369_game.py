## 369게임 : 3의 배수와 3이 들어간 수는 "짝!"을 반환, 나머지는 숫자를 반환하는 함수를 작성하라.

num = int(input("숫자를 입력하시오 :"))

if num%3 == 0:
    print("짝")
else:
    print(num)