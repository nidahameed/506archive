#Problem 1
candy_str = 'starburst, skittles, butterfinger, twix, candy corn, and m&ms'

candy_list = candy_str.split(', ')
print(candy_list)
candy_list[5] = candy_list[5].replace('and ', '')
print(candy_list)

candy_list.append('snickers')
candy_list.append('candy corn')
candy_list.append('a rock')
print(candy_list)

#candy_list.remove(candy_list[-1])
candy_list.pop(-1)
print(candy_list)



#Problem 2
first_three = candy_list[:3]
print(first_three)

reverse = candy_list[::-1]
print(reverse)

every_other = candy_list[::2]
print(every_other)



#Problem 3
candy_bags = (
    ['skittles', 'reeses cup', 'tootsie roll', 'hershey bar', 'candy corn'],#mike's bag
    ['tootise roll', 'snickers', 'airheads', 'snickers', 'skittles'],#jane's bag
    ['candy corn', 'skittles', 'airheads', 'starburst', 'snickers'],#andy's bag
)

mikes_bag, janes_bag, andys_bag = candy_bags

def judge_candy(candy):
    if candy == 'candy corn':
        print(f"{candy}? That's great!")
    else:
        print(f"{candy}? How unfortunate!")

def judge_bag(bag):
    for candy in bag:
        judge_candy(candy)

judge_bag(mikes_bag)
judge_bag(janes_bag)



#Problem 4
def sort_chocolate(bag):
    chocolate = []
    for candy in bag:
        if candy == 'snickers' or candy == 'hershey bar' or candy == 'reeses cup':
            chocolate.append(candy)
    return chocolate

#print(sort_chocolate(mikes_bag))

def sort_candy(bag):
    chocolate = []
    fruit = []
    other = []
    for candy in bag:
        if candy == 'snickers' or candy == 'hershey bar' or candy == 'reeses cup':
            chocolate.append(candy)
        elif candy == 'starburst' or candy == 'skittles' or candy == 'airheads':
            fruit.append(candy)
        else:
            other.append(candy)
    return (chocolate, fruit, other)

print(sort_candy(mikes_bag))