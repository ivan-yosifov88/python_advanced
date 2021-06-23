# TODO solve this task with another method

amount_of_clock_cycles = [int(x) for x in input().split(", ")]

job_index = int(input())

jobs_dict = {}

for i in range(len(amount_of_clock_cycles)):
    element = amount_of_clock_cycles[i]
    jobs_dict[i] = element

sorted_jobs_dict = sorted(jobs_dict.items(), key=lambda x: x[1])

result = 0

for key, value in sorted_jobs_dict:
    if not key == job_index:
        result += value
    else:
        result += value
        break

print(result)