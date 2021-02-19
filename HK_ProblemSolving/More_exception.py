class Calculator:
    def power(self, x, y):
        try:
            if x >= 0 and y >= 0:
                return x ** y
            else:
                return "n and p should be non-negative"
        except Exception as e:
            print(e)


myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)
