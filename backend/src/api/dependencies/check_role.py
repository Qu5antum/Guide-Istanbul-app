from fastapi import Depends, HTTPException, status
from backend.src.api.dependencies.current_user import get_current_user
from backend.src.models.models import User

# Провкрка пользователя на админа или простого пользователя
def require_roles(allowed_roles: list[str]):
    async def checker(
        current_user: User = Depends(get_current_user)
    ):
        user_roles = [role.name for role in current_user.roles]

        if not set(user_roles) & set(allowed_roles):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Недостаточно прав."
            )

        return current_user

    return checker
