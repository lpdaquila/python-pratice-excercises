# 

def create_multiplicator(multiplicator):
    def multiplicate(num):
        return num * multiplicator
    return multiplicate

duplicate = create_multiplicator(2)
triplicate = create_multiplicator(3)
quatruplicate = create_multiplicator(4)

print(duplicate(5))
print(triplicate(7))
print(quatruplicate(3))

