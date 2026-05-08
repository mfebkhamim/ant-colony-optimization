import numpy as np
import pandas as pd
import random

# Load distance matrix from CSV
distance_matrix = pd.read_csv("jarak_jatim.csv", index_col=0).values
cities = pd.read_csv("jarak_jatim.csv", index_col=0).index.tolist()
num_cities = distance_matrix.shape[0]

# Parameter Ant Colony System
beta = 2.0  # Pengaruh heuristik (jarak)
rho = 0.3   # Evaporasi lokal
rho_g = 0.45 # Evaporasi global
tau0 = 1.2  # Nilai awal feromon
num_ants = 20  # Jumlah semut
num_iterations = 150  # Iterasi maksimum

# Kota sebagai titik awal adalah Surabaya
START_CITY = cities.index("Kota Surabaya")

# Inisialisasi feromon
pheromone_matrix = np.full((num_cities, num_cities), tau0)

def probability(pheromone, distance, alpha=1.2, beta=2.0):
    """Menghitung probabilitas pemilihan kota berikutnya berdasarkan feromon dan heuristik"""
    tau = pheromone ** alpha
    eta = (1.0 / distance) ** beta
    return tau * eta

def choose_next_city(pheromone_matrix, distance_matrix, current_city, visited):
    """Memilih kota berikutnya berdasarkan aturan probabilitas"""
    unvisited = list(set(range(num_cities)) - set(visited))
    probabilities = probability(pheromone_matrix[current_city, unvisited], distance_matrix[current_city, unvisited])
    probabilities /= probabilities.sum()  # Normalisasi
    return np.random.choice(unvisited, p=probabilities)

def local_pheromone_update(pheromone_matrix, i, j, rho, tau0):
    """Update feromon lokal"""
    pheromone_matrix[i, j] = (1 - rho) * pheromone_matrix[i, j] + rho * tau0
    pheromone_matrix[j, i] = pheromone_matrix[i, j]  # Simetris

def global_pheromone_update(pheromone_matrix, best_route, best_distance, rho_g):
    """Update feromon global berdasarkan jalur terbaik"""
    for i in range(len(best_route) - 1):
        a, b = best_route[i], best_route[i + 1]
        pheromone_matrix[a, b] = (1 - rho_g) * pheromone_matrix[a, b] + rho_g * (1 / best_distance)
        pheromone_matrix[b, a] = pheromone_matrix[a, b]  # Simetris

def ant_colony_system():
    """Menjalankan Ant Colony System Algorithm"""
    global pheromone_matrix
    best_route = None
    best_distance = float('inf')

    for t in range(num_iterations):
        all_routes = []
        all_distances = []

        for ant in range(num_ants):
            visited = [START_CITY]  # Pilih kota awal secara acak
            total_distance = 0

            while len(visited) < num_cities:
                current_city = visited[-1]
                next_city = choose_next_city(pheromone_matrix, distance_matrix, current_city, visited)
                visited.append(next_city)
                total_distance += distance_matrix[current_city, next_city]
                
                # Local pheromone update
                local_pheromone_update(pheromone_matrix, current_city, next_city, rho, tau0)

            # Tambahkan jarak kembali ke kota awal
            total_distance += distance_matrix[visited[-1], START_CITY]
            all_routes.append(visited)
            all_distances.append(total_distance)

        # Evaluasi rute terbaik
        min_distance = min(all_distances)
        if min_distance < best_distance:
            best_distance = min_distance
            best_route = all_routes[np.argmin(all_distances)]

        # Global pheromone update
        global_pheromone_update(pheromone_matrix, best_route, best_distance, rho_g)

    return best_route, best_distance

# Jalankan Ant Colony System Algorithm
best_route, best_distance = ant_colony_system()

# Tampilkan hasil
print("Rute terbaik:", [cities[i] for i in best_route])
print("Jarak total terbaik:", best_distance)
