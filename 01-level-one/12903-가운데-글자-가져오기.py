"""
12930.가운데 글자 가져오기
https://programmers.co.kr/learn/courses/30/lessons/12903 
"""
def solution(s):
    i = len(s) // 2
    return  s[i-1:i+1] if len(s) % 2 == 0 else s[i]