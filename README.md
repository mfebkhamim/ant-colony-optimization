# Traveling Salesman Problem using Ant Colony Optimization 🐜

> Optimization of the Traveling Salesman Problem (TSP) using the Ant Colony Optimization (ACO) algorithm with a case study of cities and regencies in East Java, Indonesia.

The algorithm simulates the behavior of ants in finding the shortest path through pheromone communication and heuristic exploration.

----------------------------------------------------------------------------------------------------
## 📌 Overview
Traveling Salesman Problem (TSP) is a classical optimization problem where a salesman must visit every city exactly once and return to the starting city with minimum total distance.

Brute force approaches become computationally expensive as the number of cities increases. Therefore, this project uses Ant Colony Optimization as a metaheuristic approach to find near-optimal solutions efficiently.

----------------------------------------------------------------------------------------------------
## 🐜 Ant Colony Optimization Workflow 
The algorithm works through the following steps:
```text
1. Initialize pheromone matrix
2. Place ants randomly on cities
3. Each ant constructs a route probabilistically
4. Calculate total route distance
5. Update pheromone trails
6. Apply pheromone evaporation
7. Repeat until maximum iterations reached
```

----------------------------------------------------------------------------------------------------
## 🗺️ Dataset Preparation
The dataset used in this project was manually constructed using the geographical coordinates of cities and regencies in East Java, Indonesia.

For each city/regency, the latitude and longitude values were collected manually from geographic sources. These coordinates were then used to calculate the distance between every pair of cities.

A distance matrix was generated based on the latitude and longitude data, representing the travel cost between locations. This matrix became the main input for the Traveling Salesman Problem (TSP) optimization process using the Ant Colony Optimization (ACO) algorithm.

----------------------------------------------------------------------------------------------------
## ⚙️ ACO Parameters

| Parameter | Value | Description |
|---|---|---|
| Alpha | 1.0 | Controls pheromone influence |
| Beta | 2.0 | Controls heuristic influence |
| Evaporation Rate | 0.5 | Reduces pheromone intensity over time |
| Number of Ants | 10 | Number of ants exploring routes |
| Iterations | 100 | Total optimization iterations |
| Q | 100 | Pheromone deposit constant |

----------------------------------------------------------------------------------------------------
## 🚀 Installation
### 1️⃣ Clone Repository

```bash
git clone https://github.com/mfebkhamim/ant-colony-optimization.git
```

### 2️⃣ Navigate to Project Directory

```bash
cd ant-colony-optimization
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Project

```bash
python Ant-Colony-System.py
```
----------------------------------------------------------------------------------------------------
## 📊 Results
The algorithm successfully finds an optimized route among East Java cities based on pheromone updates and heuristic distance calculations.


### 🛣️ Best Route
```python
[
'Kota Surabaya', 'Kota Pasuruan', 'Kota Malang', 'Kabupaten Malang', 'Kota Batu', 'Kabupaten Bangkalan', 'Kabupaten Gresik', 'Kabupaten Mojokerto', 'Kota Mojokerto', 'Kabupaten Sidoarjo', 'Kabupaten Jombang', 'Kabupaten Tulungagung', 'Kota Blitar', 'Kabupaten Blitar', 'Kabupaten Trenggalek', 'Kabupaten Kediri', 'Kota Kediri', 'Kabupaten Nganjuk', 'Kabupaten Bojonegoro', 'Kabupaten Ngawi', 'Kabupaten Madiun', 'Kota Madiun', 'Kabupaten Pacitan', 'Kabupaten Ponorogo', 'Kabupaten Magetan', 'Kabupaten Lamongan', 'Kabupaten Sampang', 'Kabupaten Pasuruan', 'Kabupaten Jember', 'Kabupaten Bondowoso', 'Kabupaten Situbondo', 'Kabupaten Lumajang', 'Kabupaten Probolinggo', 'Kota Probolinggo', 'Kabupaten Pamekasan', 'Kabupaten Sumenep', 'Kabupaten Banyuwangi', 'Kabupaten Tuban'
]
```

### 📏 Best Distance:
```python
2653.8199999999997
```

----------------------------------------------------------------------------------------------------
## 📉 Limitations

This project uses geographical latitude and longitude coordinates to calculate distances between cities/regencies in East Java.

The generated distance matrix assumes straight-line distances between locations based on coordinate calculations. Therefore, the distances do not fully represent real-world travel conditions.

### ⚠️ Real-world travel distances may differ because of:

- Road structure and highway availability
- Traffic conditions
- Geographic obstacles (mountains, rivers, etc.)
- Transportation regulations and route accessibility
- Different road quality and travel efficiency

As a result, the optimized route produced by the algorithm represents a theoretical shortest path rather than an exact real-world transportation route.

----------------------------------------------------------------------------------------------------

## 🔮 Future Improvements

Possible future enhancements include:

- Integration with real road network distances
- Google Maps API or OpenStreetMap
- Traffic-aware routing
- Travel-time optimization
- Interactive route visualization
- Dynamic parameter tuning

----------------------------------------------------------------------------------------------------

## 📖 Learn More

For more detailed explanations about the concepts behind this project — including:

- Ant Colony Optimization (ACO)
- Pheromone update mechanism
- Algorithm implementation in Python

You can read the full article on Medium:

🔗 **Medium Article:**  
[[Insert Your Medium Link Here](https://medium.com/@mfebkhamim/ant-colony-optimization-perilaku-semut-menemukan-jalur-terpendek-9023c840f403)]
