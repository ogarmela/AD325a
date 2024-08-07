import math

def calculate_permutations(n, r):
    """Calculate the number of permutations P(n, r)."""
    return math.factorial(n) // math.factorial(n - r)

def calculate_combinations(n, r):
    """Calculate the number of combinations C(n, r)."""
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

def main():
    try:
        n = int(input("Enter the value for n (total items): "))
        r = int(input("Enter the value for r (items to be chosen or arranged): "))

        if n < 0 or r < 0:
            print("Both n and r must be non-negative integers.")
            return

        if r > n:
            print("r must be less than or equal to n.")
            return

        permutations = calculate_permutations(n, r)
        combinations = calculate_combinations(n, r)

        print(f"Permutations P({n}, {r}) = {permutations}")
        print(f"Combinations C({n}, {r}) = {combinations}")

    except ValueError:
        print("Invalid input. Please enter integer values for n and r.")

if __name__ == "__main__":
    main()
