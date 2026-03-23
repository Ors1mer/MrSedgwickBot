from datetime import date, timedelta


class WeekSchedule:
    """
    This class requires one parameter (a date object) to be created, e. g.:
        my_week = WeekSchedule(date.today())

    An instance can either be viewed or edited, e. g.:
        my_week.edit()
        print(my_week.view())
    """

    def __init__(self, day):
        self.first_wd = day - timedelta(days=day.today().weekday())
        self.schedule = [
            [self.first_wd + timedelta(days=wd), "empty"] for wd in range(7)
        ]

    def edit(self):
        for wd in range(7):
            name = self.schedule[wd][0].strftime("%A")
            self.schedule[wd][1] = input(f"What will you do on {name}? ")

    def view(self):
        today = date.today()
        view = []

        for wd in self.schedule:
            ft_wd = wd[0].strftime("<b>%a</b> <i>(%d.%m)</i>:")

            if (
                wd[0].day < today.day
                and wd[0].month == today.month
                or wd[0].month < today.month
                or wd[0].year < today.year
            ):
                view.append(f"<s>{ft_wd} {wd[1]}</s>")
            else:
                view.append(f"{ft_wd} {wd[1]}")

        return "\n".join(view)


if __name__ == "__main__":
    week = WeekSchedule(date.today() + timedelta(days=7 * 0))
    week.edit()
    print(week.first_wd)
    print(week.view())
