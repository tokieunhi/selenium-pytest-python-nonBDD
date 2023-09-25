import allure
class Report():
    @classmethod
    def report_step(cls, step):
        with allure.step(step):
            pass