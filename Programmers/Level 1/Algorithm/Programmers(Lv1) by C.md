# Programmers(Lv1) by C

### 수박수박수박수박수박수?

```c
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(int n) {
    char* answer = (char*)malloc(n * strlen("수"));
    strcpy(answer, "");
    for(int i=0; i<n; i++)
    {
        i%2? strcat(answer, "박") : strcat(answer, "수");
    }
    return answer;
}
```

