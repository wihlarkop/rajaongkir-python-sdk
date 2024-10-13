from collections.abc import Callable
from typing import Any, TypeVar

from raja_ongkir.exception import InvalidAccountPlanException

F = TypeVar('F', bound=Callable[..., Any])


def restricted_to_plans(allowed_plans: list[str]) -> Callable[[F], F]:
    def decorator(func: F) -> F:
        def wrapper(self, *args: Any, **kwargs: Any) -> Any:
            if self._account_plan not in allowed_plans:
                raise InvalidAccountPlanException(func_name=func.__name__, account_plan=self._account_plan)
            return func(self, *args, **kwargs)
        return wrapper
    return decorator
