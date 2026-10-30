from person import Person

class Student(Person):
    def __init__(self, name: str, age: int, major: str) -> None:
        super().__init__(name, age)
        self._major = major

    def __str__(self) -> str:
        return f"{self._name} - {self._age} years old and majoring in {self._major}."

    def __repr__(self) -> str:
        return f"Person('{self._name}', {self._age}, '{self._major}')"

    def __eq__(self, other: Person) -> bool:
        return self._name == other._name and self._age == other._age and self._major == other._major

    def __call__(self) -> None:
        print(f"Hello, I am {self._name}, {self._age} years old, and majoring in {self._major}.")
