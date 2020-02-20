#zikl1.3

school = [{'school_class': '4a', 'scores': [5,5,5]}, 
 {'school_class': '4b', 'scores': [ 4, 4, 4]},
 {'school_class': '4c', 'scores': [ 3, 3, 3]}]


school_mid = []

for s in school:
    class_score =  sum(s['scores'])
    class_mid =  class_score/ ( len(s['scores']))
    print('Cредняя оценка в классе {0}: {1}'.format(s['school_class'], class_mid))
    school_mid.append( class_mid)

school_score =  round(sum(school_mid) / len(school_mid))
print('Среднее по школе: ', school_score)

