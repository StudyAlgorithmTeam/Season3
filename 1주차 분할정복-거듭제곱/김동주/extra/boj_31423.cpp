#include <cstring>
#include <iostream>

#define MAX_N 500000


using namespace std;


/**
 * list: [1]-[2]-[3]-[4]
 *
 * HEAD: 위 리스트의 head는 [1] 을 가리킨다.
 *  (t_list lists[MAX_N+1] 에서 인덱스 번호를 head로 사용하므로, 필드에는 포함하지 않았다.)
 * NEXT: 위 리스트의 next는 head의 다음 원소를 의미하며, [2]를 나타낸다.
 * TAIL: 위 리스트의 tail은 새로 원소가 추가될 위치를 의미하며, [4]를 나타낸다.
*/
typedef struct list {
    char* s;
    struct list* next;
    struct list* tail;
} t_list;


t_list lists[MAX_N+1]; // 인덱스 번호를 head로 사용한다.
char buffer[2*MAX_N];


int main()
{
    int N;
    int n;
    int i;
    int j;
    char *buf_head;
    t_list *list_ptr;

    // fast I/O
    // (python으로 치면 input = sys.stdin.readline 이랑 비슷)
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(false);

    cin >> N;

    // 리스트 초기화
    buf_head = buffer;
    for (n = 1; n <= N; n++) {
        cin >> buf_head;
        /**
         * buffer에는 널 문자로 구분된 단어를 전부 직렬로 받아놓고,
         * 각 단어의 시작지점 포인터(buf_head)를 리스트의 s 필드에 할당함.
         */
        lists[n].s = buf_head;
        lists[n].next = nullptr;
        lists[n].tail = &lists[n];

        buf_head += strlen(buf_head)+1; // null 문자도 포함하여 건너뜀
    }

    // 쿼리 수행
    for (n = 0; n < N-1; n++) {
        cin >> i >> j;
        /** Single linked-list 연결하기.
         *
         * 1. 기존 리스트(lists[i])의 tail의 다음 원소는 새로 연결할 리스트(lists[j])의 head가 됨.
         * 2. 기존 리스트(lists[i])의 tail 대신 새로 연결할 리스트(lists[j])의 tail이 새로운 tail이 됨.
         */
        lists[i].tail->next = &lists[j];
        lists[i].tail = lists[j].tail;
    }

    // 마지막 문자열 출력
    for (list_ptr = &lists[i]; list_ptr != nullptr; list_ptr = list_ptr->next) {
        cout << list_ptr->s;
    }

    return 0;
}