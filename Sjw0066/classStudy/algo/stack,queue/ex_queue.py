#선입선출 FIFO
#별도 모듈 사용 x
q=list()
q=[]
q.append(2)
q.append(3)
q.append(4)
q.append(5)
test=q.pop(0)
q.pop(0)
print(q)

# pop 을 index로 하면 시간 복잡도가 N이라 컬렉션 사용

from collections import deque #double ended queue 이중 연결형 큐

q1=deque()
q1.append(5)
q1.append(15)
q1.append(25)
q1.append(35)
print(q1)
# 자료형이 deque클래스 형이 되버림 리스트로 뽑을라면 리스트 씌워야됨
print(list(q1))

q1.popleft()
q1.popleft()
print(list(q1))


# 또 다른 모듈
import queue

q2=queue.Queue()





