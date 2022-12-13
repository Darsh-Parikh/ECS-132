l = [21,22,22,25,25,25,25,30,46,52,13,15,16,16,19,20,20,33,33,35,35,35,35,36,40,45,70]
l_test = [5, 5, 4, 6, 2]
l2 = [21,22,22,25,25,25,25,30,46,52,13,15,16,16,19,20,20,33,33,35,35,35,35,36,40,45]
l.sort()
l2.sort()

def eval(l : list):
    hist_str = "*"
    last_val = l[0]
    mean = l[0]
    for i in range(1, len(l)):
        mean += l[i]
        if l[i] == last_val:
            hist_str += " *"
        else:
            print(f"{last_val :< 4} | " + hist_str)
            last_val = l[i]
            hist_str = "*"
    print(f"{last_val :< 4} | " + hist_str)
    mean /= len(l)
    variance = (l[0] - mean)**2
    for i in range(1, len(l)):
        variance += (l[i] - mean)**2
    variance /= len(l)-1

    median = 0
    if len(l) % 2 == 0:
        median = (l[int(len(l)/2)] + l[int(len(l)/2) + 1]) / 2
    else:
        median = l[int(len(l)/2)]
    print("The number of samples is %d" %len(l))
    print("The median is %.3f" %median)
    print("The mean is approximately %.3f" %mean)
    print("The variance is approximately %.3f" %variance)

eval(l2)