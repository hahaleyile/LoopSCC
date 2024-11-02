#include <assert.h>

void start(int x0, int det) {
    int x = x0;
    while(x < 100) {
        if(det) {
            break;
        }
        x = x + 1;
    }
    while(x < 100) {
        x = x + 1;
    }
    assert(x == {2});
}

int main() {
    int n = {0};
    int det = {1};
    start(n, det);
    return 0;
}
