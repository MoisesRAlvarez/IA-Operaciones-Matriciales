import numpy as np

def main():
    print("--- Demostración de Operaciones Matriciales en NLP ---")
    
    # 1. Representación de los 'Embeddings' (Vectores)
    # En el uso de nuestro dia a dia, estos númeross son generados por un modelo de IA Generativa.
    # Aquí tenemos una matriz de 4 documentos x 3 dimensiones de Características semánticas
    
    # Matriz D (4x3)
    documents_matrix = np.array([
        [0.8, 0.1, 0.2],  # Doc 0: "Implementación de agentes autónomos y automatización"
        [0.1, 0.9, 0.1],  # Doc 1: "Las mejores fragancias de diseñador con notas cítricas"
        [0.7, 0.2, 0.3],  # Doc 2: "Uso de Python y Docker para flujos de trabajo"
        [0.0, 0.8, 0.2]   # Doc 3: "Proyección y longevidad en perfumes de lujo"
    
    # 2. vector de búsqueda (Query)
    # Vector q 3x1 que Representa la búsqueda: "Quiero aprender a programar IA"
    query_vector = np.array([0.9, 0.1, 0.2])
    
    print("\nMatriz de Documentos (Embeddings):\n", documents_matrix)
    print("\nVector de Búsqueda:\n", query_vector)
    
    # 3. LA OPERACIÓN MATRICIAL: Producto Punto (Dot Product)
    # Multiplico la matriz (4x3) por el vector (3x1)
    # Esto me da un vector de (4x1) con los "Scores de Similitud"
    similarities = np.dot(documents_matrix, query_vector)
    
    print("\nResultados de la Multiplicación de Matrices (Similitud del 0 al 1):")
    for i, score in enumerate(similarities):
        print(f"Documento {i}: {score:.4f}")
        
    # 4. Encontrar el ganador
    best_match_index = np.argmax(similarities)
    print(f"\nEl documento más relevante es el Documento {best_match_index} con un score de {similarities[best_match_index]:.4f}")

if __name__ == "__main__":
    main()