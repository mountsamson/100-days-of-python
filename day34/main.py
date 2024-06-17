# age: int
# name: str
# height: float
# is_human: bool


def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
        return "YES WAY G"
    else:
        can_drive = False
    return "They can't drive"


print(police_check(22))


