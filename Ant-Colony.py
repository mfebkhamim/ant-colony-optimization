import numpy as np
import pandas as pd
import random

# Load distance matrix from CSV
# Matriks jarak antar kota dibaca dari file CSV
distance_matrix = pd.read_csv("jarak_jatim.csv", index_col=0).values
cities = pd.read_csv("jarak_jatim.csv", index_col=0).index.tolist()

# Inisialisasi parameter ACO
NUM_ANTS = 20  # Jumlah semut
NUM_ITERATIONS = 150  # Jumlah iterasi
ALPHA = 1.2  # Pengaruh feromon
BETA = 2.0  # Pengaruh heuristik (jarak)
EVAPORATION_RATE = 0.4  # Tingkat evaporasi
Q = 100  # Konstanta feromon

# Kota sebagai titik awal adalah Surabaya
START_CITY = cities.index("Kota Surabaya")

num_cities = distance_matrix.shape[0]
# Inisialisasi matriks ukuran nxn yang tiap elemennya diisi dengan nilai awal 1
pheromone_matrix = np.ones((num_cities, num_cities))  

def probability(i, unvisited, pheromone_matrix, distance_matrix):
    """Menghitung probabilitas pemilihan kota berikutnya"""
    pheromone = pheromone_matrix[i, unvisited] ** ALPHA
    heuristic = (1.0 / distance_matrix[i, unvisited]) ** BETA
    probabilities = pheromone * heuristic
    return probabilities / probabilities.sum()

def ant_colony_optimization():
    """Menjalankan algoritma Ant Colony Optimization untuk mencari rute terbaik"""
    global pheromone_matrix
    best_route = None
    best_distance = float('inf') # karena kita ingin mencari jarak minimum
    
    for iteration in range(NUM_ITERATIONS):
        all_routes = []
        all_distances = []
        
        for ant in range(NUM_ANTS):
            visited = [START_CITY]  # Mulai dari kota acak
            unvisited = set(range(num_cities)) - set(visited)
            total_distance = 0
            
            while unvisited:
                current_city = visited[-1]
                unvisited_list = list(unvisited)
                probabilities = probability(current_city, unvisited_list, pheromone_matrix, distance_matrix)
                next_city = np.random.choice(unvisited_list, p=probabilities)
                
                visited.append(next_city)
                unvisited.remove(next_city)
                total_distance += distance_matrix[current_city, next_city]
            
            # Tambahkan jarak kembali ke kota awal
            total_distance += distance_matrix[visited[-1], START_CITY]
            all_routes.append(visited)
            all_distances.append(total_distance)
            
        # Update rute terbaik
        min_distance = min(all_distances)
        if min_distance < best_distance:
            best_distance = min_distance
            best_route = all_routes[np.argmin(all_distances)]
        
        # Update feromon dengan evaporasi dan penambahan jejak semut
        pheromone_matrix *= (1 - EVAPORATION_RATE)
        for i, route in enumerate(all_routes):
            for j in range(len(route) - 1):
                pheromone_matrix[route[j], route[j+1]] += Q / all_distances[i]
                pheromone_matrix[route[j+1], route[j]] += Q / all_distances[i]
    
    return best_route, best_distance

# Jalankan ACO dan tampilkan hasil
best_route, best_distance = ant_colony_optimization()
print("Rute terbaik:", [cities[i] for i in best_route])
print("Jarak total terbaik:", best_distance)