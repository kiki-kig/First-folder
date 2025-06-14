def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "0으로 나눌 수 없습니다!"
    return x / y

print("간단 계산기")
print("1. 더하기")
print("2. 빼기")
print("3. 곱하기")
print("4. 나누기")

choice = input("원하는 연산을 선택하세요 (1/2/3/4): ")

num1 = float(input("첫 번째 숫자 입력: "))
num2 = float(input("두 번째 숫자 입력: "))

if choice == "1":
    print("결과:", add(num1, num2))
elif choice == "2":
    print("결과:", subtract(num1, num2))
elif choice == "3":
    print("결과:", multiply(num1, num2))
elif choice == "4":
    print("결과:", divide(num1, num2))
else:
    print("잘못된 선택입니다.")
