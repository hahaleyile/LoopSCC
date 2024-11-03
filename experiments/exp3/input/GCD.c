#include "klee/klee.h"

void Success() {}

/* extended Euclid's algorithm */
int gcd(int x, int y)
{
    int a, b, p, q, r, s;

    a = x;
    b = y;
    p = 1;
    q = 0;
    r = 0;
    s = 1;

    while (a != b)
    {

        if (a > b)
        {
            a = a - b;
            p = p - q;
            r = r - s;
        }

        else
        {
            b = b - a;
            q = q - p;
            s = s - r;
        }
    }

    return a;
}

int main()
{
    int x,y;
    klee_make_symbolic(&x, sizeof(x), "x");
    klee_make_symbolic(&y, sizeof(y), "y");
    klee_assume(y < 100);
    klee_assume(y > 0);
    klee_assume(x < 100);
    klee_assume(x > 0);
    int result=gcd(x,y);
    if (result == 37)
        Success();
    return 0;
}
