def get_digits(n):
    return [int(i) for i in str(n)]

attempts = [319, 680, 180,690,129,620,762,689,762,318,368,710,720,710,629,168,160,689,716,731,736,729,316,729,729,710,769,290,719,680,318,389,162,289,162,718,729,319,790,680,890,362,319,760,316,729,380,319,728,716]

nums = set([int(i) for i in "".join([str(n) for n in attempts])])
code = [0] * len(nums)
for num in nums:
    before = set()
    after = set()
    for k in attempts:
        digits = get_digits(k)
        if num == digits[0]:
            after.add(digits[1])
            after.add(digits[2])
        if num == digits[1]:
            before.add(digits[0])
            after.add(digits[2])
        if num == digits[2]:
            before.add(digits[0])
            before.add(digits[1])
        if len(nums) == len(before) + len(after) + 1:
            break
    code[len(before)] = num
    print (code)
    
print("".join([str(c) for c in code]))
