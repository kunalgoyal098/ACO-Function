import numpy as np

def move_robot(current_position, pheromone_map, communication_range, exploration_factor):
    # Define the possible moves the robot can make
    possible_moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # down, up, right, left
    
    # Get the dimensions of the pheromone map
    map_height, map_width = pheromone_map.shape
    
    # Initialize a list to store the probabilities for each move
    move_probabilities = []
    
    # Calculate the probability of each move based on local pheromone concentration
    for move in possible_moves:
        new_position = (current_position[0] + move[0], current_position[1] + move[1])
        
        # Check if the new position is within the communication range and map boundaries
        if (0 <= new_position[0] < map_height and 0 <= new_position[1] < map_width and
            np.linalg.norm(np.array(new_position) - np.array(current_position)) <= communication_range):
            # Calculate the probability based on pheromone concentration and exploration factor
            pheromone_concentration = pheromone_map[new_position]
            probability = (pheromone_concentration ** exploration_factor) / np.sum(pheromone_map ** exploration_factor)
            move_probabilities.append(probability)
        else:
            move_probabilities.append(0)
    
    # Normalize the probabilities
    move_probabilities = move_probabilities / np.sum(move_probabilities)
    
    # Choose the next move based on the calculated probabilities
    next_move = np.random.choice(len(possible_moves), p=move_probabilities)
    
    # Update the robot's position
    new_position = (current_position[0] + possible_moves[next_move][0],
                    current_position[1] + possible_moves[next_move][1])
    
    # Update the pheromone map with decay and evaporation
    pheromone_map *= (1 - decay_rate)
    pheromone_map[new_position] += 1  # Increase pheromone level at the new position
    
    return new_position, pheromone_map

# Example usage:
current_position = (5, 5)
pheromone_map = np.ones((10, 10))
communication_range = 2
exploration_factor = 2
decay_rate = 0.1

new_position, updated_pheromone_map = move_robot(current_position, pheromone_map, communication_range, exploration_factor)
print(f"New Position: {new_position}")
print(f"Updated Pheromone Map:\n{updated_pheromone_map}")


