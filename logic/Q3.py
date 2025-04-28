def find_last_person(n):
    if n <= 0 or n > 100:
        return "請輸入 1 到 100 之間的數字"

    people = list(range(1, n + 1))
    index = 0 
    count = 0 

    while len(people) > 1:
        count += 1
        if count == 3:
            people.pop(index)
            count = 0
        else:
            index += 1

        if index >= len(people):
            index = 0 

    return f"最後留下的是第 {people[0]} 順位的人"

if __name__=="__main__":
    n = int(input("請輸入人數 (1-100): "))
    print(find_last_person(n))
