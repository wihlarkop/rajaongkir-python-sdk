class InvalidAccountPlanException(Exception):
    def __init__(self, func_name: str = None, account_plan: str = None):
        if func_name and account_plan is not None:
            self.message = f"{func_name} is not available for the {account_plan} plan"
        self.message = "Invalid account plan provided"
        super().__init__(self.message)


class InvalidAPIKeyException(Exception):
    def __init__(self):
        self.message = "Invalid key provided"
        super().__init__(self.message)


class RajaOngkirException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
