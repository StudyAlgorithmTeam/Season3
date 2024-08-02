#include <iostream>
#include <algorithm>
#include <queue>
#include <cstring>
#include <vector>
using namespace std;

#define INF 987654321
int numE, numV;
int dist[20001];

// O((E + V) logV)
void dijkstra(int start, vector<pair<int, int>> graph[]) {
    priority_queue<pair<int, int>> pq; 

    dist[start] = 0;
    pq.push({ 0, start });

    // O((E + V) logV)
    while (!pq.empty()) {
        // O(V logV): while문은 총 V회 돈다. pq에 모든 노드가 저장되기 때문.
        int cur_dist = -pq.top().first;
        int cur_node = pq.top().second;
        pq.pop(); // O(logV)

        if (cur_dist > dist[cur_node])
            continue;

        // O(E logV): 간선을 탐색함. + push 연산
        for (auto& edge : graph[cur_node]) {
            int nxt_node = edge.first;
            int nxt_dist = cur_dist + edge.second;

            if (nxt_dist < dist[nxt_node]) {
                dist[nxt_node] = nxt_dist;
                pq.push({ -nxt_dist, nxt_node }); // push 연산 자체가 O(logV)
            }
        }
    }

    // O(V)
    for (int i = 1; i <= numV; i++) {
        if (dist[i] == INF) cout << "INF\n";
        else cout << dist[i] << "\n";
    }
}


// O((E + V) logV)
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
    int start;
    cin >> numV >> numE>>start;
    vector<pair<int, int>> graph[20001];
  
    // O(E)
    for (int i = 0; i < numE; i++) {
        int from, to, cost;
        cin >> from >> to >> cost;
        graph[from].push_back({ to, cost });
        //graph[to].push_back({ from, cost });
    }

    // O(V)
    for (int i = 1; i <= numV; i++) {
        dist[i] = INF;
    }

    // O((E + V) logV)
    dijkstra(start, graph);

    return 0;
}