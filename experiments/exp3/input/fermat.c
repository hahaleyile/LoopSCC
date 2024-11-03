#include "klee/klee.h"

void Success() {}

/* program computing a divisor for factorisation, by Knuth */
int fermat(int N, int R)
{
    int u, v, r;
    u = 2 * R + 1;
    v = 1;
    r = R * R - N;

    while (r != 0)
    {

        while (r > 0)
        {
            r = r - v;
            v = v + 2;
        }

        while (r < 0)
        {
            r = r + u;
            u = u + 2;
        }
    }

    return ((u - v) / 2);
}

int main()
{
    int N, R;
    int result;
    klee_make_symbolic(&N, sizeof(N), "N");
    klee_make_symbolic(&R, sizeof(R), "R");
    klee_assume(N >= 1);
    klee_assume((R - 1) * (R - 1) < N);
    klee_assume(N <= R * R);
    klee_assume(N % 2 == 1);
    klee_assume(N >= 1);
    klee_assume(N <= 100);
    klee_assume(R >= 1);
    klee_assume(R <= 100);
    result = fermat(N, R);
    if (result == 37)
        Error();
    return 0;
}
