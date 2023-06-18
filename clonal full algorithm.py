import random

# Constants
POPULATION_SIZE = 50
CLONES_FACTOR = 0.5
MUTATION_RATE = 0.1
GENERATIONS = 100
THRESHOLD = 0.4

# Generate initial population
population = []
for _ in range(POPULATION_SIZE):
    # Generate random antibodies
    antibody = [random.randint(0, 1) for _ in range(10)]  # Replace with appropriate feature size
    population.append(antibody)

# Define the dataset (you'll need to replace this with your own dataset)
# dataset = [
#     ([0, 'ed', 1, 0, 1, 1, 0, 1, 1, 1], 0),  # Example instance: ([features], label)
#     ([1, 'sd', 1, 1, 0, 1, 0, 0, 1, 0], 1),
#     ([1, 'rs', 1, 0, 0, 1, 0, 0, 0, 0], 1),
#     ([1, 'sd', 1, 0, 0, 0, 0, 0, 1, 0], 0),
#     ([1, 'rs', 1, 1, 0, 1, 1, 1, 1, 1], 0),
#     ([0, 'rs', 1, 0, 0, 1, 0, 0, 1, 0], 0),
#     # Add more instances here...
# ]
import pandas as pd;
data = pd.read_csv('C:\\Users\\BBWiSE\\eclipse-workspace\\jse\\AIS_IDS\\python\\dataset\\KDDTrain+_.csv');

dataset = data[["'protocol_type'","'service'","'flag'","'src_bytes'","'dst_bytes'","'urgent'"]];
result = data["'outcome'"];

print(dataset);

# Calculate the distance between two antibodies
def calculate_distance(antibody, instance):
    return sum([1 for a, i in zip(antibody, instance) if a != i])

# Determine if an instance is classified as an anomaly
def is_anomaly(instance):
    return any([calculate_distance(antibody, instance) <= THRESHOLD for antibody in population])

# Clone an antibody with mutation
def clone_antibody(antibody):
    clone = antibody.copy()
    for i in range(len(clone)):
        if random.random() < MUTATION_RATE:
            clone[i] = 1 - clone[i]  # Flip the bit
    return clone

# Main AIS loop
for generation in range(GENERATIONS):
    # Generate a set of non-anomalous instances
    non_anomalous_set = [instance for instance in dataset if not is_anomaly(instance[0])]
    
    # Evaluate fitness for each antibody in the population
    fitness_scores = [len([instance for instance in non_anomalous_set if calculate_distance(antibody, instance[0]) <= THRESHOLD]) for antibody in population]
    
    # Sort antibodies by fitness in descending order
    sorted_population = [antibody for _, antibody in sorted(zip(fitness_scores, population), reverse=True)]
    
    # Select the fittest antibodies for cloning
    clones_count = int(CLONES_FACTOR * POPULATION_SIZE)
    clones = [clone_antibody(antibody) for antibody in sorted_population[:clones_count]]
    
    # Replace the least fit antibodies with the clones
    population[clones_count:] = clones
    
    # Print the best antibody in this generation
    best_antibody = sorted_population[0]
    print(f"Generation {generation+1}: Best Antibody = {best_antibody}")

# After training, you can use the best antibody to classify new instances
new_instance = ['tcp','private','S0',0,0,0] #[0, 1, 0, 1, 1, 0, 0, 1, 1, 0]  # Replace with your own instance to classify
is_anomaly = is_anomaly(new_instance)
print(f"Is the new instance an anomaly? {is_anomaly}")
