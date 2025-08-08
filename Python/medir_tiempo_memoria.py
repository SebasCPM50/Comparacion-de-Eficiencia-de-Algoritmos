import time
from memory_profiler import memory_usage
from factorial_iterativo import facto_i
from factorial_recursivo import facto_r
import matplotlib.pyplot as plt

def medir_tiempo_y_memoria(funcion, n):
    inicio_tiempo = time.time()
    memoria, resultado = memory_usage((funcion, (n,)), retval=True, max_usage=True)
    fin_tiempo = time.time()
    return {
        "resultado": resultado,
        "tiempo": fin_tiempo - inicio_tiempo,
        "memoria_MB": memoria  # Esto es la memoria máxima usada
    }

if __name__ == "__main__":
    valores_n = [10, 50, 100, 200, 300, 500]
    tiempos_i, tiempos_r = [], []
    memorias_i, memorias_r = [], []

    print("{:<10} {:<15} {:<15} {:<15} {:<15}".format("n", "Tiempo I", "Tiempo R", "Memoria I (MB)", "Memoria R (MB)"))
    for n in valores_n:
        datos_i = medir_tiempo_y_memoria(facto_i, n)
        datos_r = medir_tiempo_y_memoria(facto_r, n)

        tiempos_i.append(datos_i["tiempo"])
        tiempos_r.append(datos_r["tiempo"])
        memorias_i.append(datos_i["memoria_MB"])
        memorias_r.append(datos_r["memoria_MB"])

        print(f"{n:<10} {datos_i['tiempo']:<15.8f} {datos_r['tiempo']:<15.8f} {datos_i['memoria_MB']:<15.6f} {datos_r['memoria_MB']:<15.6f}")

    # Gráfica de Tiempo
    plt.figure(figsize=(10, 6))
    plt.plot(valores_n, tiempos_i, marker='o', label='Iterativo')
    plt.plot(valores_n, tiempos_r, marker='s', label='Recursivo')
    plt.xlabel('Valor de n')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Tiempo: Factorial Iterativo vs Recursivo')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("grafica_tiempo_factorial.png")
    plt.show()

    # Gráfica de Memoria
    plt.figure(figsize=(10, 6))
    plt.plot(valores_n, memorias_i, marker='o', label='Iterativo')
    plt.plot(valores_n, memorias_r, marker='s', label='Recursivo')
    plt.xlabel('Valor de n')
    plt.ylabel('Memoria utilizada (MB)')
    plt.title('Memoria: Factorial Iterativo vs Recursivo')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("grafica_memoria_factorial.png")
    plt.show()

