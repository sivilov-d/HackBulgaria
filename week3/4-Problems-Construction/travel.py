def travel_costs(travels):
    a = " 1 "
    travel = []
    sum_travels = 0
    
    for runs in travels:        
        sum_travels += runs
        
    if sum_travels >= 50:
        a = "Mарийка да си вземе карта за цялата градска мрежа"
        travel += [a]
        
    else:        
        line = 1        
        for runs in travels:            
            if runs < 23:
                a = "Марийка да си купува билетчета за линия %s" % line
            else:
                a = "Марийка да си вземе карта за линия %s" % line

            line += 1
            travel += [a]

    return travel


d = travel_costs([23, 24, 2])
for i in d:
    print(i)
