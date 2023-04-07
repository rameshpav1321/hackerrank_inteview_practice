def truckTour(petrolpumps):
    # Write your code here
    start=0
    curr_gas,defecit_gas=0,0
    for index,pump in enumerate(petrolpumps):
        curr_gas+=pump[0]-pump[1]
        if curr_gas<0:
            start=index+1
            defecit_gas+=curr_gas
            curr_gas=0
    return start if curr_gas+defecit_gas>=0 else -1