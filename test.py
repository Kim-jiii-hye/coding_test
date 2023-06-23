
#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#
import json
import re

def fizzBuzz(n):
    answer = ''
    for i in range(1, n+1):
        res = str(i)
        if i % 3 == 0:
            res = 'Fizz'
        if i % 5 == 0:
            res = 'Buzz'
        if i == n:
            res = 'FizzBuzz'
        answer = answer + res + '\n'
    print(answer)
def pseudo_code(a, b):
    x = a
    y = b
    if x > y:
        answer = x-y
        print()
    if(x < y):
        answer = y - x
    print(answer)

# 약수 구하기 test case : 7/15
def PON(n):
    res = []
    for i in range(1, int(n ** (1 / 2)) + 1):
        if (n % i == 0):
            res.append(i)
            if ((i ** 2) != n):
                res.append(n // i)

    res.sort()
    if min(res) == 1:
        if len(res) > 2:
            find_idx = res.index(1)
            del res[find_idx]
        answer = min(res)
    print(answer)
    print(res)
    # res = []
    # for i in range(1, num+1):
    #     if num % i == 0:
    #         res.append(i)
    # print(res)

# REST API test cate : 5/8
def CallJSON(keyword):
    # url = f"https://jsonmock.hackerrank.com/api/weather/search?name={keyword}"
    # response = requests.request("GET", url, headers={}, data={})
    # resp = json.loads(response.text.encode('utf8'))
    file_path = "./test.json"

    with open(file_path, 'r') as file:
        resp = json.load(file)
        print(type(resp))
    result = []
    answer = ''
    getdata = resp['data']
    # ['Dallas,12,2,5']
    for i in getdata:
        answer = answer + i['name']
        getweather = i['weather'].split(' ')[0]
        answer = answer + "," + getweather
        getstatus = i['status']
        for j in getstatus:
            getStat = j.split(' ')[1]
            numbers = re.sub(r'[^0-9]', '', getStat)
            answer = answer + "," + numbers
        result.append(answer)
        answer = ''
    print(result)
# regularExpression = '^1+(1*01*01*)+$'

# Minimum Cache Capacity
def MCC(requests, k):
    print(requests)
    answer = 0
    cache_hit = ''
    cache_before = []
    cache_after = []
    for (idx, i) in enumerate(requests):
        print(i)
        print(f"cache_before:{cache_before}")
        cache_before = cache_after
        cache_after = i

        print(f"cache_after:{cache_after}")
        if idx + 1 < len(requests):
            if (cache_after  == requests[idx+1]):
                answer = answer + 1
    print(answer)

        # cache_before = cache_after
        # if i not in cache_after:
        #     cache_after.append(i)
        # if len(cache_after) > 1:
        #     del cache_after[0]

        # print(f"cache_before:{cache_before} cache_after:{cache_after} i:{i}")






if __name__ == '__main__':
    # pseudo_code(2437, 875)
    # n = int(input().strip())
    # fizzBuzz(15)
    # PON(1072843847)
    # PON(2)
    # PON(4)
    #
    # CallJSON('all')
    MCC(['item1', 'item1', 'item3', 'item1', 'item3'], 1)