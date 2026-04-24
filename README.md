# Aplicación de Operaciones Matriciales en IA: Buscador Semántico

Este proyecto forma parte de la asignatura de Álgebra Lineal en el **Instituto Tecnológico de las Américas (ITLA)**. Consiste en una demostración práctica de cómo las operaciones matriciales son fundamentales en el Procesamiento de Lenguaje Natural (NLP).

## 📝 Descripción del Proyecto
El proyecto explora el concepto de **Word Embeddings**, donde las palabras o documentos se transforman en vectores numéricos dentro de un espacio n-dimensional. La aplicación práctica utiliza la **multiplicación de matrices (Producto Punto)** para calcular la similitud entre una consulta (query) y una base de datos de documentos.

## 🚀 Cómo funciona
La lógica matemática detrás del buscador es la siguiente:
1. Tenemos una matriz $D$ de $m \times n$, donde cada fila es un documento.
2. Tenemos un vector $q$ de $n \times 1$ que representa la búsqueda.
3. Al realizar la operación $S = D \cdot q$, obtenemos un vector de puntuaciones de similitud.

## 🛠️ Requisitos
- Python 3.x
- NumPy

## 📦 Instalación y Uso
1. ```bash
   git clone https://github.com/MoisesRAlvarez/IA-Operaciones-Matriciales.git 