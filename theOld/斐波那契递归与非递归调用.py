class Soulution:
    # 递归
    def Fibonacci(self, n):
        if n <= 1:
            return n
        else:
            return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)

    # 非递归
    def Fibonacci2(self, n):
        a, b = 0, 1
        while n > 0:
            a, b = b, a + b
            n -= 1
        return a


if __name__ == '__main__':
    f = Soulution()
    print('递归', f.Fibonacci(10))
    print('非递归', f.Fibonacci2(10))
