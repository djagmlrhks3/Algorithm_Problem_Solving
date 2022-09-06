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



### 음양 더하기

```c
#include <stdio.h>
#include <stdbool.h>

int solution(int absolutes[], size_t absolutes_len, bool signs[], size_t signs_len) {
    int answer = 0;
    for(int i=0; i<signs_len; i++)
    {
        answer += signs[i]? absolutes[i]:-absolutes[i];
    }    
    return answer;
}
```



### 내적

```c
#include <stdio.h>

int solution(int a[], size_t a_len, int b[], size_t b_len) {
    int answer = 0;
    for(int i=0; i<a_len; i++)
    {
        answer += (a[i] * b[i]);
    }
    return answer;
}
```



### 약수의 개수와 덧셈

```c
#include <stdio.h>

int solution(int left, int right) {
    int answer = 0;
    for(int i=left; i<=right; i++)
    {
        int cnt = 0;
        for (int j=1; j<= i; j++)
        {
            if (i % j == 0) cnt++;
        }
        answer += cnt%2? -i:i;
    }
    return answer;
}
```



### 3진법 뒤집기

```C
#include <stdio.h>
#include <math.h>

int solution(int n) {
    int three[10] = {0};
    int idx = 0;
    while (n>2)
    {
        three[idx] = n%3;
        n /= 3;
        idx++;
    }
    if(n > 0)
    {
        three[idx] = n;
        idx++;
    }
    
    int answer = 0;
    for(int i=0;i<idx;i++)
    {
        answer += three[i] * pow(3, idx-i-1);
    }
    return answer;
}
```



### 두 개 뽑아서 더하기

```C
#include <stdio.h>

int* solution(int numbers[], size_t numbers_len) {
    int chk[201] = {0};
    int cnt = 0;
    for(int i=0; i<numbers_len; i++)
    {
        for(int j=i+1; j<numbers_len; j++)
        {
            int sum = numbers[i] + numbers[j];
            if (chk[sum] == 0)
            {
                chk[sum] = 1;
                cnt++;
            }
        }
    }
    int* answer = (int*)malloc(sizeof(int)*(cnt+1));
    int idx = 0;
    for(int i=0; i<201; i++)
    {
        if(chk[i])
        {
            answer[idx] = i;
            idx++;
        }
    }
    return answer;
}
```

