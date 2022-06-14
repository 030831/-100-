student_tuple = (('191102', '홍길동', '010-1234-5789'), ('191103', '임꺽정', '010-1357-2468'), ('191104', '장길산', '010-8282-5858'))
student_dict={}

for i in range(len(student_tuple)):
    student_dict[student_tuple[i][0]]=student_tuple[i][1]

print(student_dict)
while True:
    a=input("학번을 입력하세요: ")
    if a=='-1':
        print("프로그램을 종료합니다.")
        break
    else:
        print("%s번 학생은 %s입니다"%(a,student_dict[a]))