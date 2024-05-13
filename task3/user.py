from datetime import date


class User:
    """Describe user"""
    def __init__(self, last_name: str, first_name: str, surname: str, birthday: date, email: str) -> None:
        """Initialize user attributes"""
        self.last_name = last_name
        self.first_name = first_name
        self.surname = surname
        self.birthday = birthday
        self.email = email

    def get_full_name(self) -> str:
        """Return full username"""
        return "{} {} {}".format(self.last_name, self.first_name, self.surname)

    def get_short_name(self) -> str:
        """Return short username"""
        return "{} {}.{}.".format(self.last_name, self.first_name[0], self.surname[0])

    def get_age(self) -> int:
        """Calculate user age"""
        today = date.today()
        born = self.birthday
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def __str__(self) -> str:
        """Print user info"""
        return f"{self.last_name} {self.first_name} {self.surname}, birthday: {self.birthday}"
