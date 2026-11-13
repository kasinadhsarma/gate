# Mermaid sources for the DSA Deep Edition

Paste any block into https://mermaid.live or render with `mmdc -i x.mmd -o x.pdf --pdfFit`.

## d1
```mermaid
flowchart TD
  A["Problem statement"] --> B{"Constraints n?"}
  B -->|"n up to 20"| C["Brute force / backtracking"]
  B -->|"n up to 10^3"| D["O(n^2) is fine"]
  B -->|"n up to 10^5"| E["Need O(n log n)"]
  B -->|"n up to 10^6+"| F["Need O(n) / O(1)"]
  E --> G["Sort / heap / binary search / divide and conquer"]
  F --> H["Hash map / two pointers / prefix sums"]
```

## d2
```mermaid
flowchart LR
  P["Python object model"] --> I["Immutable: int, float, str, tuple, frozenset"]
  P --> M["Mutable: list, dict, set, deque"]
  I --> I1["x = x + 1 makes a NEW object"]
  M --> M1["lst.append changes the SAME object"]
  M1 --> T["Aliasing: b = a shares one list"]
  M1 --> W["Default argument list is created ONCE"]
```

## d3
```mermaid
flowchart TD
  S["Which data structure?"] --> Q1{"Need order of arrival?"}
  Q1 -->|"last in first out"| ST["Stack (list)"]
  Q1 -->|"first in first out"| QU["Queue (deque)"]
  Q1 -->|"no"| Q2{"Need fast lookup by key?"}
  Q2 -->|"yes"| HM["Hash table: dict / set  O(1) avg"]
  Q2 -->|"no"| Q3{"Need min or max repeatedly?"}
  Q3 -->|"yes"| HP["Heap: O(log n) push/pop"]
  Q3 -->|"sorted order + range queries"| BS["BST / balanced tree"]
```

## d4
```mermaid
flowchart LR
  A["Algorithm toolbox"] --> B["Searching"]
  A --> C["Sorting"]
  A --> D["Divide and conquer"]
  A --> E["Graphs"]
  B --> B1["Linear O(n)"]
  B --> B2["Binary O(log n), sorted only"]
  C --> C1["Quadratic: bubble, selection, insertion"]
  C --> C2["n log n: merge, quick, heap"]
  D --> D1["Split - Solve - Combine"]
  D1 --> D2["Master theorem"]
  E --> E1["BFS: shortest hops"]
  E --> E2["DFS: order, cycles, topo sort"]
```

## d5
```mermaid
flowchart TD
  R["mergeSort(arr)"] --> S{"len <= 1 ?"}
  S -->|"yes"| Z["return arr"]
  S -->|"no"| L["mergeSort(left half)"]
  S -->|"no"| Rr["mergeSort(right half)"]
  L --> M["merge two sorted halves, O(n)"]
  Rr --> M
  M --> O["return sorted array"]
```

## d6
```mermaid
flowchart TD
  A["Start BFS at s, dist[s]=0, queue=[s]"] --> B{"queue empty?"}
  B -->|"no"| C["u = pop front"]
  C --> D["for each neighbour v of u"]
  D --> E{"v unvisited?"}
  E -->|"yes"| F["dist[v]=dist[u]+1, push v"]
  E -->|"no"| D
  F --> D
  D --> B
  B -->|"yes"| G["done: dist = fewest edges"]
```

## d7
```mermaid
flowchart TD
  A["DFS(u)"] --> B["mark u GRAY (on stack)"]
  B --> C["for each neighbour v"]
  C --> D{"colour of v?"}
  D -->|"WHITE"| E["tree edge: DFS(v)"]
  D -->|"GRAY"| F["BACK edge: cycle found"]
  D -->|"BLACK"| G["forward / cross edge"]
  E --> C
  F --> C
  G --> C
  C --> H["mark u BLACK, append to finish order"]
```

## d8
```mermaid
flowchart LR
  A["Google-style problem"] --> B{"Pattern?"}
  B -->|"pair / triple in sorted data"| P1["Two pointers"]
  B -->|"best window of size k"| P2["Sliding window"]
  B -->|"have I seen this before"| P3["Hash set / map"]
  B -->|"sum of a range"| P4["Prefix sums"]
  B -->|"min x such that ok(x)"| P5["Binary search on answer"]
  B -->|"next greater element"| P6["Monotonic stack"]
  B -->|"shortest path unweighted"| P7["BFS on grid or graph"]
  B -->|"top k"| P8["Heap"]
```

## d9
```mermaid
sequenceDiagram
  participant Main
  participant f4 as fib(4)
  participant f3 as fib(3)
  participant f2 as fib(2)
  Main->>f4: call
  f4->>f3: call
  f3->>f2: call
  f2-->>f3: 1
  f3-->>f4: 2
  f4-->>Main: 3
```
