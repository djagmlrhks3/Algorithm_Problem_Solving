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



### 로또의 최고 순위와 최저 순위

```c
#include <stdio.h>

int* solution(int lottos[], size_t lottos_len, int win_nums[], size_t win_nums_len) {
    int* answer = (int*)malloc(sizeof(int)*2);
    int win = 0; int zero = 0;
    for(int i=0; i<lottos_len; i++)
    {
        if (lottos[i] == 0) zero++;
        for(int j=0; j<win_nums_len; j++)
        {
            if(lottos[i] == win_nums[j]) win++;
        }
    }
    int rank[7] = {6, 6, 5, 4, 3, 2, 1};
    answer[0] = rank[win+zero];
    answer[1] = rank[win];
    return answer;
}
```

