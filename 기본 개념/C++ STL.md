STL 이란?
================


STL을 설명하기 전에 알고리즘 풀이 때 C++을 사용하는 이유를 말하면,		

첫번째로 C의 빠른 연산 처리를 혼용해서 쓸 수 있다는 점, 		

둘째로 **STL(Standard Template Library)**을 사용할 수 있다는 점이다.

<br>

**STL**은 크게 **Container 와 Iterator, Algorithm**으로 분류된다.			

<br>


### 1. Container

+ **Sequence Container**

  배열처럼 객체들을 순차적으로 보관하는 컨테이너

  ex) vector, deque, list, array		

+ **Associative Container**

  키 : 값 쌍으로 객체를 저장하는 컨테이너

  ex) set,map

  

### 2. Iterator & Algorithm

+ **RandomAccessIterator**

  index를 통해 임의의 위치에 접근할 수 있는 반복자

  ex) vector, deque에서 사용



+ **BidirectionalIterator**

  양방향으로 이동할 수 있지만, 한 칸씩 밖에 이동할 수 없는 반복자

  ex) 나머지 컨테이너에서 사용

  
