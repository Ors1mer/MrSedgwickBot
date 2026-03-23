from datetime import date, timedelta


"""
This class requires one parameter (a date object) to be created, e. g.:
    my_week = WeekSchedule(date.today())

An instance can either be viewed or edited, e. g.:
    my_week.edit("work", 0)
    print(my_week.view())
"""
class WeekSchedule:
    def __init__(self, day):
        self.first_wd = day - timedelta(days=day.today().weekday())
        self.schedule = [
            [self.first_wd + timedelta(days=wd), "empty 🌀"] for wd in range(7)
        ]

    def edit(self, text, day_num):
        self.schedule[day_num][1] = text

    def view(self):
        today = date.today()
        wd_names = [
            "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday"
        ]
        view = []

        for wd in self.schedule:
            name = wd_names[int(wd[0].strftime("%w"))]
            ft_wd = wd[0].strftime(f"<b>{name}</b> <i>(%d.%m)</i>:")

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
    week.edit("do stuff", 0)
    week.edit("chill", 4)
    print(week.first_wd)
    print(week.view())
