def func(n):
    breakpoint()
    if n==0:
        return
    print(n)
    func(n-1)
    print(n)

func(3)