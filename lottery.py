import random

# Function to generate a random lottery number between 1 and 100
def generate_lottery_number():
  # Returns a random number between 1 and 100
  return random.randint(1, 100)

# Function to get the player's numbers
def get_player_numbers(name):
  # Gets the player's numbers from the user
  player_numbers = []
  for _ in range(3):
    number = int(input("{} enter a number between 1 and 100: ".format(name)))
    while number not in range(1, 101):
      # Checks if the number is between 1 and 100
      print("Invalid number. Please enter a number between 1 and 100: ".format(name))
      number = int(input())
    # Adds the number to the list of player numbers
    player_numbers.append(number)
  # Returns the list of player numbers
  return player_numbers

# Function to check if the player has won
def check_winner(player_numbers, lottery_numbers, name):
  # Counts the number of matches between the player's numbers and the lottery numbers
  points = 0
  for number in player_numbers:
    if number in lottery_numbers:
      points += 1
  # Returns a message depending on the number of matches
  if points == 2 or points == 3:
    return "{} has won!".format(name)
  else:
    return "{} has lost.".format(name)

# Function to run the lottery
def run_lottery():
  # Creates a list of players
  players = []
  # Gets the total stake from the players
  stake = 0
  # Gets the number of players
  number_of_players = int(input("Enter the number of players: "))
  if number_of_players < 6:
    # Checks if the number of players is at least 6
    print("The number of players must be at least 6.")
    return
  # Gets the name of each player
  player_names = []
  for i in range(number_of_players):
    name = input("Player {} enter your name: ".format(i + 1))
    player_names.append(name)
    # Gets the player's numbers
    player_numbers = get_player_numbers(name)
    # Adds the player's stake to the total stake
    stake += int(input("{} enter your stake: ".format(name)))
    # Creates a dictionary for the player with their name, numbers, and stake
    players.append({
      "name": name,
      "numbers": player_numbers,
      "stake": stake
    })
  # Generates the lottery numbers
  lottery_numbers = [generate_lottery_number() for _ in range(3)]
  # Finds the winners
  winners = []
  for player in players:
    if check_winner(player["numbers"], lottery_numbers, player["name"]) == "{} has won!".format(player["name"]):
      if stake > 0:
        winners.append(player)
      else:
        print("{} has won nothing since the stake is 0.".format(player["name"]))
  # If there are more than one winners, they share the money equally
  if len(winners) > 0:
    if stake > 0:
      shared_stake = stake / len(winners)
      for winner in winners:
        print("{} has won {}!".format(winner["name"], shared_stake))
  else:
    print("No winners this time.")

if __name__ == "__main__":
  # Runs the lottery
  run_lottery()
