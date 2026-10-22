from person import Person
from student import Student

def main() -> None:
    myself = Person("Peter", 19)
    friend = Person("Tung", 19)
    pers3 = Person("Marc", 36)
    pers4 = Person("Marco", 28)
    pers5 = Person("Ramy", 22)

    print(myself) # Peter - 19 years old
    print(myself == friend) # False
    print(myself + friend) # 38
    print(len(myself)) # 5
    print(sorted([myself, friend, pers3, pers4, pers5]))

    print()
    myself()
    myself()
    myself()

    print()
    me_student = Student("Peter", 19, "Computer Science")
    print(me_student)
    me_student()

if __name__ == "__main__":
    main()