#include <assert.h>

void start(int y0, int z0){
    int y = y0;
    int z = z0;
    while(z > y){
        y = y + 1;
    }
    while(y > 2){
        y = y - 3;
    }
    assert(y == {2});
}

int main(){
    int y = {0};
    int z = {1};
    start(y,z);
    return 0;
}