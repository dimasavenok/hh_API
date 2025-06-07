from typing import Any, Dict, List


class Vacancy:
    def __init__(self, title: str, url: str, salary: Any, description: str) -> None:
        self.title: str = title
        self.url: str = url
        self.salary: float = self.validate_salary(salary)
        self.description: str = description


    def __repr__(self) -> str:
        return (
            f"{self.title} ({self.format_salary(self.salary)})\n"
            f"{self.url}\n"
            f"{self.description[:100]}...)")


    def __lt__(self, other: "Vacancy") -> bool:
        return self.salary < other.salary


    def format_salary(self, salary:float) -> str:
        rubles = int(salary)
        kopecks = int(round((salary - rubles)*100)) if salary % 1 != 0 else 0
        formated_rubles = "{:,}".format(rubles).replace(",", " ")
        if kopecks > 0:
            return f"{formated_rubles}, {kopecks:02d} валют"
        return f"{formated_rubles} валют"


    @classmethod
    def cast_to_object_list(cls, data: List[Dict[str, Any]]):
        vacancies: List[Vacancy] = []
        for item in data:
            vacancies.append(
                cls(
                    title=item.get("name", "Не указано"),
                    url=item.get("alternate_url", ""),
                    salary=item.get("salary"),
                    description=item.get("snippet", {}).get("requirement", "Нет описания")
                )
            )
        return vacancies


    @staticmethod
    def validate_salary(salary: Any) -> float:
        if isinstance(salary, dict) and salary.get("from"):
            return salary.get("from")
        return float(0)

