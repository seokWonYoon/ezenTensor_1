from student import Student

'''
클래스에 학생의 이름을 추가한 후 학생의 과목은 총 5개 평균을 구한뒤 a~f 가 출력되도록 하시오
ex) 홍길동 평균 87점 b
'''

 
def main():
    st = Student(input("학생 이름 : "))
    
    for i in ["국어", "영어", " 수학", "과학", "사회"]:
        st.addmarks(int(input("점수 : ")))
    avg = st.avg()
    
    if avg>=90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    elif avg >= 50:
        grade = "E"
    else:
        grade = "F"
    print("{} 평균 {}점 {}".format(st.name, st.avg(), grade))

if __name__ == "__main__":
    main()
