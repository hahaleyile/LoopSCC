#include <assert.h>

void start(int x, int y) {
    int x1 = x;
    int y1 = y;
    while (x1 > y1) {
        x1 = x1 - 1;
        x1 = x1 + 1000;
        y1 = y1 + 1000;
    }
    while (y1 > 0) {
        y1 = y1 - 1;
    }
    while (x1 < 0) {
        x1 = x1 + 1;
    }
    assert(x1 == {2});
    assert(y1 == {3});
}

int main() {
    int x = {0};
    int y = {1};
    start(x, y);
    return 0;

}