#include <assert.h>

void start(int x, int y, int det){
    while(x > 0){
        x = x - 1;
        if(det){
            y = y + 1;
        } else {
            while(y > 0){
                y = y - 1;
            }
        }
    }
    assert(x == {3});
    assert(y == {4});
}

int main(){
    int x = {0};
    int y = {1};
    int det = {2};
    start(x, y, det);
    return 0;
}