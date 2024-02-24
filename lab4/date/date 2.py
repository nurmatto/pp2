import datetime

timedelta = datetime.timedelta(days=1)
todayy_is_only_which_is_really_matter = datetime.datetime.today()
tomorrow_doesnot_matter = todayy_is_only_which_is_really_matter + timedelta
yeasterday_has_to_be_lesson = todayy_is_only_which_is_really_matter - timedelta

print('Today is', todayy_is_only_which_is_really_matter.date())
print('Yesterday is', yeasterday_has_to_be_lesson.date())
print('Tomorrow is', tomorrow_doesnot_matter.date())