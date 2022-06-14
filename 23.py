person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]

person_list=person1+person2+person3+person4

def how_many_persons(person_list):
    return len(person_list)//4

def compute_average_age(person_list):
    count=0
    sum=0
    for i in range(1,len(person_list),5):
        sum+=person_list[i]
        count+=1
    return "%.1f"%(sum/count)


def count_males_females(person_list):
    male=0 ; female=0
    for i in range(2,len(person_list),5):
        if person_list[i]==0:
            female+=1
        else:
            male+=1
    return male,female

def display_persons(person_list):
    person=[]
    for i in range(len(person_list)):
        person.append(person_list[i])
        if (i+1)%5==0:
            print(person)
            person.clear()


n_persons=how_many_persons(person_list)
print(n_persons,'명의 정보가 담겨 있습니다')
print()
average_age = compute_average_age(person_list)
print('평균나이는',average_age,'세 입니다.')
print()
n_male, n_female = count_males_females(person_list)
print('리스트에는 남자가',n_male,'명, 여자가', n_female, '명 있습니다.')
print()

display_persons(person_list)
