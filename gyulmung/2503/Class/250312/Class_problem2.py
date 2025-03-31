import sys
sys.stdin = open('input.txt','r')

import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:

