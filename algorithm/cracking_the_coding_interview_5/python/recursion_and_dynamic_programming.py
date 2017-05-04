
"""
9.1 A child is running up a staircase with n steps,and can hop either 1 step, 2 steps,
or 3 steps at a time. Implement a method to count how many possible ways the
child can run up
"""

def count_possible_step(next_step, total_step_count, target_step_count, path_list):
    
    current_total = next_step + total_step_count
    path = list(path_list)
    path.append(next_step)
    if current_total == target_step_count:
        print path
        return 1
    elif current_total > target_step_count:
        return 0
    else:
        s1 = count_possible_step(1, current_total, target_step_count,path)
        s2 = count_possible_step(2, current_total, target_step_count,path)
        s3 = count_possible_step(3, current_total, target_step_count,path)
        return s1+s2+s3


def main_count_possible_step():
    print count_possible_step(0, 0, 10, [])
    
def count_possible_step_dynamic(next_step, total_step_count, target_step_count, path_list, map):
    
    current_total = next_step + total_step_count
    path = list(path_list)
    path.append(next_step)
    if current_total == target_step_count:
        print path
        return 1
    elif current_total > target_step_count:
        return 0
    else:
        if current_total in map:
            return map[current_total]
        else:
            s1 = count_possible_step_dynamic(1, current_total, target_step_count,path, map)
            s2 = count_possible_step_dynamic(2, current_total, target_step_count,path, map)
            s3 = count_possible_step_dynamic(3, current_total, target_step_count,path, map)
            map[current_total] = s1+s2+s3
            return map[current_total]


def main_count_possible_step_dynamic():
    map = {}
    print count_possible_step_dynamic(0, 0, 10, [], map)
    print map
    
    

if __name__ == "__main__":
    import timeit
    main_count_possible_step()
    
    t1 = timeit.timeit("main_count_possible_step()",setup="from __main__ import main_count_possible_step",number=10)
    t2 = timeit.timeit("main_count_possible_step_dynamic()",setup="from __main__ import main_count_possible_step_dynamic",number=10)
    
    print t1,t2
    
    print "Done"