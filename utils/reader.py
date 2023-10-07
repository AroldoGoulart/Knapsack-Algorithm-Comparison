import os
from functools import lru_cache

@lru_cache(maxsize=None) 
def read_instance(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    n, c = map(int, lines[0].strip().split())
    values = []
    weights = []

    for line in lines[1:]:
        _id, weight, value = map(int, line.strip().split())
        values.append(value)
        weights.append(weight)

    return n, c, values, weights

def load_test_cases(directory):
    test_cases = []
    files_in_directory = os.listdir(directory)
    # Listar todos os arquivos do diretório
    for filename in files_in_directory:
        # progresso da leitura %
        print(f"Progress: {len(test_cases) / len(files_in_directory) * 100:.2f}%")
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            n, c, values, weights = read_instance(filepath)
            test_cases.append({"values": values, "weights": weights, "capacity": c})

    return test_cases