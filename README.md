# Collatz Inverse Expansion Algorithm

This repository contains an implementation of the inverse expansion algorithm for the Collatz conjecture, as presented in the paper:

> Enis Olgac. *Proof of the Collatz Conjecture through the Inverse Expansion Graph* (2025). DOI: [10.13140/RG.2.2.23090.88006](https://doi.org/10.13140/RG.2.2.23090.88006)

The algorithm constructs the inverse Collatz graph \( P \) via breadth-first outward expansion from the root node 1, using the canonical inverse rules. This structural approach proves that the graph covers all positive integers, confirming the Collatz conjecture.

## Features

- **Pure Python implementation** of the BFS expansion algorithm.
- Outputs accumulated nodes, edges, and BFS frontiers \( \Delta L_i \).
- **Unit tests** to verify correctness (e.g., root cycle `{1, 2, 4}`, back edge `(1,4)`).
- Modular and extensible code for further research.

## Usage

1.  Clone the repository:
    ```bash
    git clone https://github.com/EnisOlgac/Inverse-Expansion-Of-Collatz-Graph.git
    cd Inverse-Expansion-Of-Collatz-Graph
    ```

2.  Run the algorithm:
    ```bash
    python src/inverse_expansion.py
    ```

3.  Run tests:
    ```bash
    python -m unittest tests/test_inverse_expansion.py
    ```
## Example Output

```
Frontiers:
ΔL_0 = [1]
ΔL_1 = [2]
ΔL_2 = [4]
ΔL_3 = [8, 1]   # Note: 1 is a recurrence (cycle)
ΔL_4 = [16]
ΔL_5 = [32, 5]
...
```
## References

- Olgac, E. (2025). *Proof of the Collatz Conjecture through the Inverse Expansion Graph*. Preprint. DOI: [10.13140/RG.2.2.23090.88006](https://doi.org/10.13140/RG.2.2.23090.88006)

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for improvements or extensions.
