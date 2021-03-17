n, m = input().split()

n_set = set()
m_set = set()

for num in range(int(n)):
    n_set.add(input())
for number in range(int(m)):
    m_set.add(input())

result_set = set.intersection(n_set, m_set)

for result in result_set:
    print(result)
