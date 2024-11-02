#include <assert.h>

void start(int n, int y) {
    while (n < 0) {
        n = n + 1;
        y = y + 1000;
        while (y >= 100) {
            y = y - 100;
        }
    }
    assert(n == {2});
    assert(y == {3});
}

int main() {
    int n = {0};
    int y = {1};
    start(n, y);
    return 0;
}