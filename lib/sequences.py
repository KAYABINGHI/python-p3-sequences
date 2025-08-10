def print_fibonacci(length):
    
    if length <= 0:
        print([]) 
        return

    fib_seq = [0]
    if length > 1:
        fib_seq.append(1)

    while len(fib_seq) < length:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])

    print(fib_seq)
