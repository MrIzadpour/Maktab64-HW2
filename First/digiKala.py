def digikala(num):
    final_1 = []
    a = True
    while a:
        if final_1 == []:
            num_1 = [j for i,j in enumerate(num) if j not in num[:i]]
            rep = []
            for i in num_1:
                if num.count(i) > 1:
                    rep.append(num.count(i))
            string = "".join(num_1) + "".join(list(map(str, rep)))
            string = sorted(list(map(int, list(string))))
            string = "".join(map(str, string))
            final_1.append(string)
        else:
            num = final_1[-1]
            num_1 = [j for i,j in enumerate(num) if j not in num[:i]]
            rep = []
            for i in num_1:
                if num.count(i) > 1:
                    rep.append(num.count(i))
            string = "".join(num_1) + "".join(list(map(str, rep)))
            string = sorted(list(map(int, list(string))))
            string = "".join(map(str, string))
            final_1.append(string)
            a = num != string
    return final_1[-1]
print(digikala(list(input("Enter your number:   "))))
