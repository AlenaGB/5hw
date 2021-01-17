import json
profit = {}
all_profit = {}
negative = {}
prof = 0
prof_aver = 0
i = 0
with open('file7.txt', 'r') as file:
    for line in file:
        name, firm, proceeds, expenses = line.split()
        profit[name] = int(proceeds) - int(expenses)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
        else:
            negative[name] = int(proceeds) - int(expenses)
    if i != 0:
        prof_aver = prof / i
        print(f'the average profit  - {prof_aver:.2f}')

    all_profit = {'the average profit ': round(prof_aver)}
    profit.update(all_profit)
    print(f'profit of each company  - {profit}')
    print(f'negative profit   - {negative}')

with open('file7.json', 'w') as write_js:
    json.dump(profit, write_js)

    # js_str = json.dumps(profit)
    # print(f'{js_str}')