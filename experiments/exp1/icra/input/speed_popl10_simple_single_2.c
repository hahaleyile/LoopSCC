#include <assert.h>

void start(int x0, int y0) {
    int x = x0;
    int y = y0;

    while (1) {
        if (x < 100) {
            x = x + 1;
            y = y + 1;
        } else if (y < 30) {
            x = x + 1;
            y = y + 1;
        } else {
            break;
        }
    }

    assert(x == {2});
    assert(y == {3});
}

int main() {
    int x = {0};
    int y = {1};
    start(x, y);
    return 0;
}