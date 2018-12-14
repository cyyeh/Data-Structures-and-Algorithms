# Uses python3

def fibonacci_sum_squares(n):
    def get_fibonacci_mod_m(n, m):
        if n <= 1:
            return n

        fib_list = [0, 1]
        fib_mod_m_list = [0, 1]
        i = 2

        while True:
            if len(fib_mod_m_list) > 2 and fib_mod_m_list[-2:] == [0, 1]:
                fib_mod_m_list = fib_mod_m_list[0 : -2]
                break
            elif (i - 1) == n:
                return fib_mod_m_list[-1]

            next = fib_list[i - 1] + fib_list[i - 2]
            fib_mod_m_list.append(next % m)
            fib_list.append(next)
            i += 1

        remainder = n % len(fib_mod_m_list)
        return fib_mod_m_list[remainder] 

    if n <= 1:
        return n

    f_n_last_digit = get_fibonacci_mod_m(n, 10)
    f_n_plus_one_last_digit = get_fibonacci_mod_m(n + 1, 10)

    return (f_n_last_digit * f_n_plus_one_last_digit) % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
