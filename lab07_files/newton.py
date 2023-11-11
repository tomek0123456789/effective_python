import argparse
from scipy.misc import derivative


def newton_method(function, initial_guess, derivative_step, max_steps, precision):
    x = initial_guess
    steps = 0
    while steps < max_steps:
        f = function(x)
        f_prime = derivative(function, x, dx=derivative_step)
        if abs(f_prime) < precision:
            break
        x = x - f / f_prime
        steps += 1
    return x


def main():
    parser = argparse.ArgumentParser(description='Demo program finding zero points using Newton\'s method')
    parser.add_argument('function', type=str, help='Function for finding zero points')
    parser.add_argument('-i', '--initial_guess', type=float, default=0, help='Initial guess (default: 0)')
    parser.add_argument('-s', '--derivative_step', type=float, default=0.001,
                        help='Step size in derivative calculation (default: 0.001)')
    parser.add_argument('-m', '--max_steps', type=int, default=100,
                        help='Maximum number of method steps (default: 100)')
    parser.add_argument('-p', '--precision', type=float, default=0.0001, help='Precision (default: 0.0001)')

    args = parser.parse_args()
    function = lambda x: eval(args.function)

    result = newton_method(function, args.initial_guess, args.derivative_step, args.max_steps, args.precision)

    print(f"Zero point of function {args.function} found using Newton's method: {result}")


if __name__ == '__main__':
    main()