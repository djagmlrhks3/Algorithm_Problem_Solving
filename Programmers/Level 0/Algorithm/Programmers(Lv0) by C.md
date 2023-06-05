# Programmers(Lv0) by C



### flag에 따라 다른 값 반환하기

```C
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int a, int b, bool flag) {
    if (flag) {
        return a+b;
    } else {
        return a-b;
    }
}
```

