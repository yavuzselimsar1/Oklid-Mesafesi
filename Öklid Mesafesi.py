import math

# Noktaların Tanımlanması
points = [(1, 2), (3, 4), (5, 6), (7, 8)]  # Örnek olarak noktaları tanımladım

# Öklid Mesafesi İçin Bir Fonksiyon Yazma
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Mesafelerin Hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Minimum Mesafenin Bulunması
min_distance = min(distances)
print("Minimum mesafe:", min_distance)