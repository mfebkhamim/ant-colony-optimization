import numpy as np
import pandas as pd

# Load matriks jarak dari file CSV
distance_matrix = pd.read_csv("jarak_jatim.csv", index_col=0).values
cities = pd.read_csv("jarak_jatim.csv", index_col=0).index.tolist()

num_cities = distance_matrix.shape[0]

# Kota sebagai titik awal adalah Surabaya
START_CITY = cities.index("Kota Surabaya")

# Inisialisasi Matriks Feromon
def initialize_pheromone_matrix(num_cities, initial_pheromone_value=1.2):
    return np.full((num_cities, num_cities), initial_pheromone_value)

# Pilih kota selanjutnya berdasarkan probabilitas dari feromon
def choose_next_city_saco(pheromone, current_city, visited):
    probabilities = []
    for city in range(len(pheromone)):
        if city not in visited:
            probability = pheromone[current_city][city]
            probabilities.append(probability)
        else:
            probabilities.append(0)
    
    probabilities = np.array(probabilities)
    probabilities /= np.sum(probabilities)  # Normalisasi agar totalnya 1
    next_city = np.random.choice(range(len(pheromone)), p=probabilities)
    return next_city

def simple_ant_colony_optimization(num_cities, distance_matrix, num_ants, num_iterations):
    pheromone = initialize_pheromone_matrix(num_cities)
    best_path = None
    best_path_length = float('inf')  # Karena kita mencari jarak minimum

    for iteration in range(num_iterations):
        paths = []
        for ant in range(num_ants):
            path = [START_CITY]  # Pilih kota awal Surabaya
            while len(path) < num_cities:
                next_city = choose_next_city_saco(pheromone, path[-1], path)
                path.append(next_city)
            
            path.append(START_CITY)
            paths.append(path)

        # Evaluasi panjang setiap jalur
        for path in paths:
            path_length = sum([distance_matrix[path[i]][path[i+1]] for i in range(len(path)-1)])
            path_length += distance_matrix[path[-1]][path[0]]  # Tambahkan jarak kembali ke kota awal
            
            if path_length < best_path_length:
                best_path_length = path_length
                best_path = path

    best_path = [int(city) for city in best_path]
    return best_path, best_path_length

# Parameter ACO
num_ants = 20
num_iterations = 150

best_path, best_path_length = simple_ant_colony_optimization(num_cities, distance_matrix, num_ants, num_iterations)

print("Rute terbaik:", [cities[i] for i in best_path])
print("Jarak total terbaik:", best_path_length)