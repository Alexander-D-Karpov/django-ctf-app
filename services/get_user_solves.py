from ctf.models import UserSolve
from user.models import Person


def get_user_solves(user: Person) -> list[str]:
    solves = UserSolve.objects.all().filter(user_id=user.id)
    return [x.task.name for x in solves]
