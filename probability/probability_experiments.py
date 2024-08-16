import random
import matplotlib.pyplot as plt

# Task 1: Simulating Coin Tosses
def simulate_coin_tosses():
    tosses = [random.choice(['Heads', 'Tails']) for _ in range(100)]
    heads = tosses.count('Heads')
    tails = tosses.count('Tails')
    
    # Plotting the results
    plt.bar(['Heads', 'Tails'], [heads, tails])
    plt.title('Coin Toss Results')
    plt.show()

# Task 2: Rolling a Die
def simulate_die_rolls():
    rolls = [random.randint(1, 6) for _ in range(60)]
    frequencies = [rolls.count(i) for i in range(1, 7)]
    
    # Plotting the distribution
    plt.bar(range(1, 7), frequencies)
    plt.title('Die Roll Distribution')
    plt.xlabel('Die Face')
    plt.ylabel('Frequency')
    plt.show()

# Task 3: Drawing Cards
def simulate_drawing_cards():
    deck = ['Red'] * 26 + ['Black'] * 26
    random.shuffle(deck)
    draws = [deck.pop() for _ in range(20)]
    red_count = draws.count('Red')
    black_count = draws.count('Black')
    
    # Plotting the results
    plt.bar(['Red', 'Black'], [red_count, black_count])
    plt.title('Card Drawing Results')
    plt.show()

# Task 4: Probability of Compound Events
def simulate_two_coin_flips():
    outcomes = [(random.choice(['Heads', 'Tails']), random.choice(['Heads', 'Tails'])) for _ in range(50)]
    both_heads = outcomes.count(('Heads', 'Heads'))
    at_least_one_head = sum(1 for outcome in outcomes if 'Heads' in outcome)
    
    # Plotting the results
    plt.bar(['Both Heads', 'At Least One Head'], [both_heads, at_least_one_head])
    plt.title('Two Coins Flip Results')
    plt.show()

# Main function to run all tasks
if __name__ == "__main__":
    print("Simulating Coin Tosses...")
    simulate_coin_tosses()
    
    print("Simulating Die Rolls...")
    simulate_die_rolls()
    
    print("Simulating Drawing Cards...")
    simulate_drawing_cards()
    
    print("Simulating Two Coin Flips...")
    simulate_two_coin_flips()
