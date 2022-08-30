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



### 없는 숫자 더하기

```c
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int numbers[], size_t numbers_len) {
    int sum = 0;
    for(int i=0; i<numbers_len; i++)
    {
        sum += numbers[i];
    }
    return 45-sum;
}
```

### 나머지가 1이 되는 수 찾기

```c
#include <stdio.h>

int solution(int n) 
{
    for(int i=1; i<=n; i++) if(n%i == 1) return i;
}
```
