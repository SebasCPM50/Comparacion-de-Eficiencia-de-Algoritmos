unsigned long long factorial_iterativo(int n) {
    unsigned long long resultado = 1;
    for (int i = 1; i <= n; ++i)
        resultado *= i;
    return resultado;
}