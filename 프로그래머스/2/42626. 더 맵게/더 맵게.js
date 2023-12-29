class MinHeap {
  constructor() {
    this.heap = [null];
  }

  size() {
    return this.heap.length - 1;
  }

  getMin() {
    return this.heap[1] ? this.heap[1] : null;
  }

  swap(a, b) {
    [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
  }

  // 새로운 노드 삽입
  add(value) {
    this.heap.push(value);
    this.bubbleUp();
  }

  // 새로 추가된 요소를 부모노드와 비교하는 메서드
  bubbleUp() {
    let newIndex = this.size(); // 새로 추가된 요소의 인덱스 = 힙의 크기.
    let parentIndex = Math.floor(newIndex / 2);

    while (parentIndex >= 1 && this.heap[newIndex] < this.heap[parentIndex]) {
      this.swap(newIndex, parentIndex);
      newIndex = parentIndex;
      parentIndex = Math.floor(newIndex / 2);
      // 부모노드의 인덱스 업데이트를 나중에 한 이유는 하나의 연산으로 끝낼 수 있어서
      // 자식노드는 2개 이므로 연산을 나눠서 해야한다.
    }
  }

  // 힙의 속성을 유지하도록 재조정
  // 1. 루트노드에서 시작해 내려감
  // 2. 각 뎁스마다 현재노드가 자식노드보다 크면 위치 교환
  // 3. 왼쪽 오른쪽 자식노드의 인덱스 계산하고, 범위내에 있으면 비교 수행

  heappop() {
    const min = this.heap[1];
    if (this.heap.length <= 2) this.heap = [null];
    else this.heap[1] = this.heap.pop();

    let curIdx = 1;
    let leftIdx = curIdx * 2;
    let rightIdx = curIdx * 2 + 1;

    /*    ???    */
    if (!this.heap[leftIdx]) return min;
    if (!this.heap[rightIdx]) {
      if (this.heap[leftIdx] < this.heap[curIdx]) {
        this.swap(leftIdx, curIdx);
      }
      return min;
    }

    while (
      this.heap[leftIdx] < this.heap[curIdx] ||
      this.heap[rightIdx] < this.heap[curIdx]
    ) {
      const minIdx =
        this.heap[leftIdx] > this.heap[rightIdx] ? rightIdx : leftIdx;
      this.swap(minIdx, curIdx);
      curIdx = minIdx;
      leftIdx = curIdx * 2;
      rightIdx = curIdx * 2 + 1;
    }

    return min;
  }

  peek() {
    return this.heap[1];
  }
}

function solution(scoville, K) {
  let answer = 0; // 카운트 변수
  const minHeap = new MinHeap();

  for (const item of scoville) {
    minHeap.add(item);
  }

  // 반복조건 : 힙에 아이템이 최소 2개이상은 있어야하고, peek()한 아이템이 K지수보다 작아야한다.
  while (minHeap.size() >= 2 && minHeap.peek() < K) {
    // 무엇을 반복?
    // => 가장 작은 음식 두개 빼내서
    // => 섞은 후 다시 넣기
    first = minHeap.heappop();
    second = minHeap.heappop();
    minHeap.add(first + second * 2);
    answer += 1;
  }

  // peek한게 K보다 크면 성공했으므로 카운터 반환.
  return minHeap.peek() < K || minHeap.size() === 0 ? -1 : answer;
}
