#include <stdio.h>

#define ENABLE_PRINT 1
#define N 5

int main()
{
    int i, fact = 1;
    for (i = 1; i <= N; i++)
    {
        fact *= i;
    }

#if ENABLE_PRINT
    printf("Factorial of %d is %d\n", N, fact);
#endif

    return 0;
}
