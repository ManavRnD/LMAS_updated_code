

def ds_condition_check(settings,diagsat, as3935,mac_id,db):
    if settings.check_previous_AS:
        print(f"Check if count holds true for given time for a given master Return 0 or 1")
        ##put this query in a diffrent class so that if required we can call the same querry again and again
        result=db.count_as_trigger(mac_id,settings.AS_trigger)
        print('result',result)
        count_as_db= result[0]['count']
        if as3935 ==1 :
            count_as_db =+1
            print('count',count_as_db)

        if result and count_as_db >= settings.DS_AS_trigger_count:
            print(f"Count is greater than the threshold set")
            return 1
        else:
            print(f"Count is not crossing the threshold")
            return 0

    else:
        if as3935 == 1:
            print('Ds returns 1')
            return 1
        else:
            print(0)
            return 0
