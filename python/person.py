class Person:
    # Initialization
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    # String for output
    def __str__(self) -> str:
        return f"{self._name} - {self._age} years old."

    # String for repr()
    def __repr__(self) -> str:
        return f"Person('{self._name}', {self._age})"

    # Compare objects
    def __eq__(self, other: Person) -> bool:
        return self._name == other._name and self._age == other._age

    # Add two objects
    def __add__(self, other: Person) -> int:
        return self._age + other._age

    # Length
    def __len__(self) -> int:
        return len(self._name)

    # Less than - for comparison
    def __lt__(self, other: Person) -> bool:
        return self._age < other._age

    # Membership - in
    def __contains__(self, substr: str) -> bool:
        return substr in self._name

    # Function
    def __call__(self) -> None:
        print(f"Hello, I am {self._name} and I am {self._age} years old.")
