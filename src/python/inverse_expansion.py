# src/inverse_expansion.py
def inverse_expansion(max_levels=20):
    """
    Generates the inverse Collatz graph P via BFS outward expansion.
    Returns:
        L (set): All nodes visited.
        edges (list): Edges in the graph (child, parent).
        frontiers (list): BFS frontiers ΔL_i.
    """
    L = {1}
    Δ = [1]          # Current frontier
    edges = []       # List of edges (child, parent)
    frontiers = [Δ]  # List of frontiers

    for level in range(max_levels):
        new_Δ = []
        for n in Δ:
            # Rule 1: Doubling
            child1 = 2 * n
            edges.append((child1, n))
            if child1 not in L:
                L.add(child1)
                new_Δ.append(child1)

            # Rule 2: Inverse (3n+1) step
            if n % 6 == 4:  # n ≡ 4 mod 6
                child2 = (n - 1) // 3
                edges.append((child2, n))
                if child2 not in L:
                    L.add(child2)
                    new_Δ.append(child2)

        Δ = new_Δ
        frontiers.append(Δ)
        if not Δ:
            break

    return L, edges, frontiers

# Example usage
if __name__ == "__main__":
    L, edges, frontiers = inverse_expansion(max_levels=10)
    print("Frontiers:")
    for i, Δ in enumerate(frontiers):
        print(f"ΔL_{i} = {Δ}")