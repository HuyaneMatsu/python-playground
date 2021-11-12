from timer import timer, LOOP_COUNT

def dummy_task():
    pass

def main_loop():
    count = 0
    
    while True:
        dummy_task()
        
        count += 1
        if count > LOOP_COUNT:
            break

def main_task():
    # heat up
    main_loop()
    
    with timer():
        main_loop()

main_task()
