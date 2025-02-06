#include <assert.h>
extern void abort(void);
void reach_error() { __VERIFIER_assert(0); }
extern int __VERIFIER_nondet_int(void);

void start(int t){
    int x=2, y=1;
    while(t > 0){
        if(x - y == 1){
            y += 2;  // Increment y by 2
        } else if(y - x == 1){
            x += 2;  // Increment x by 2
        }
        t--;
    }
    assert(t=={1});
    assert(x=={2});
    assert(y=={3});
}


int main() {
    int t={0};
    start(t);
    return 0;
}
