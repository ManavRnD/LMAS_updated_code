def as_condition_check(settings,as3935):
    if not settings.multiple_as:
        print(f"Check if as_trigger_count {settings.as_trigger_count} <= count within as_trigger_time {settings.as_trigger_time}")

    else:
        if settings.as_redundant:
            print(f"Check if as_trigger_count {settings.as_trigger_count} <= count wihtin as trigger_time {settings.as_trigger_time}")
        else:
            print(f"check if any other As triggered in as_trigger_short_time{settings.as_trigger_short_time} and break and return if ture")
            print(f"Check the as_trigger_count {settings.as_trigger_count} distribution checking if the count is majorly "
                  f"from the as that just triggered,"
                  f" depending on the distribution we can return 0,1 or 2 ")


