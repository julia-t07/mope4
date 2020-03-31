import random, math
import scipy.stats

x1_min = -30
x1_max = 20
x2_min = -30
x2_max = 45
x3_min = -30
x3_max = 15
y_min = 170
y_max = 227
X = [[-1.0, -1.0, -1.0],#1
     [-1.0, -1.0, 1.0], #2
     [-1.0, 1.0, -1.0], #3
     [-1.0, 1.0, 1.0],  #4
     [1.0, -1.0, -1.0], #5
     [1.0, -1.0, 1.0],  #6
     [1.0, 1.0, -1.0],  #7
     [1.0, 1.0, 1.0]]   #8
Xf = [[-1.0, -1.0, -1.0, 1.0, 1.0, 1.0, -1.0],  # 1
       [-1.0, -1.0, 1.0, 1.0, -1.0, -1.0, 1.0],  # 2
       [-1.0, 1.0, -1.0, -1.0, 1.0, -1.0, 1.0],  # 3
       [-1.0, 1.0, 1.0, -1.0, -1.0, 1.0, -1.0],  # 4
       [1.0, -1.0, -1.0, -1.0, -1.0, 1.0, 1.0],  # 5
       [1.0, -1.0, 1.0, -1.0, 1.0, -1.0, -1.0],  # 6
       [1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0],  # 7
       [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]]  # 8
Gt = {1: 0.9065, 2: 0.7679, 3: 0.6841, 4: 0.6287, 5: 0.5892, 6: 0.5598, 7: 0.5365, 8: 0.5175, 9: 0.5017,
      10: 0.4884}
Gt2 = [(range(11, 17), 0.4366), (range(17, 37), 0.3720), (range(37, 145), 0.3093)]
def func(num):

    N = 8
    m = num
    Y = [[random.randint(y_min, y_max) for y in range(m)] for x in range(N)]
    print("Y: ")
    for i in range(len(Y)):
        print(Y[i])
    print("-------------------------")
    # матриця Х
    for i in range(len(X)):
        if X[i][0] == -1:
            X[i][0] = x1_min
        else:
            X[i][0] = x1_max
        if X[i][1] == -1:
            X[i][1] = x2_min
        else:
            X[i][1] = x2_max
        if X[i][2] == -1:
            X[i][2] = x3_min
        else:
            X[i][2] = x3_max
        X[i].append(X[i][0] * X[i][1])
        X[i].append(X[i][0] * X[i][2])
        X[i].append(X[i][1] * X[i][2])
        X[i].append(X[i][0] * X[i][1] * X[i][2])

    print("X: ")
    for i in range(len(X)):
        print(X[i])
    print("-------------------------")
    # середнє по рядках
    Ys = []
    for i in range(len(Y)):
        Ys.append(sum(Y[i]) / m)
    print("Ys: ")
    for i in range(len(Ys)):
        print(Ys[i])
    print("-------------------------")
    s1 = s2 = s3 = 0
    s12 = s13 = s23 = 0
    s123 = 0
    for i in range(N):
        s1 += Ys[i] * Xf[i][0]
        s2 += Ys[i] * Xf[i][1]
        s3 += Ys[i] * Xf[i][2]
        s12 += Ys[i] * Xf[i][3]
        s13 += Ys[i] * Xf[i][4]
        s23 += Ys[i] * Xf[i][5]
        s123 += Ys[i] * Xf[i][6]
    b0 = sum(Ys) / N
    b1 = s1 / N
    b2 = s2 / N
    b3 = s3 / N
    b12 = s12 / N
    b13 = s13 / N
    b23 = s23 / N
    b123 = s123 / N
    print("b0= {0} \n"
          "b1= {1} \n"
          "b2= {2} \n"
          "b3= {3} \n"
          "b12= {4} \n"
          "b13= {5} \n"
          "b23= {6} \n"
          "b123= {7} ".format(b0, b1, b2, b3, b12, b13, b23, b123))
    # нормоване рівняння
    print("Y={} + {}*x1 + {}*x2 + {}*x3 +{}*x1x2 + {}*x1x3 +"
          " {}*x2x3 + {}*x1x2x3".format(b0, b1, b2, b3,b12,b13,b23,b123))
    print("-------------------------")
    # перевірка
    print("Перевірка: ")
    print(b0 + b1 * Xf[0][0] + b2 * Xf[0][1] + b3 * Xf[0][2] + b12 * Xf[0][3] + b13 * Xf[0][4]
          + b23 * Xf[0][5] + b123 *Xf[0][6],"==", Ys[0])

    print(b0 + b1 * Xf[1][0] + b2 * Xf[1][1] + b3 * Xf[1][2] + b12 * Xf[1][3] + b13 * Xf[1][4]
          + b23 * Xf[1][5] + b123 * Xf[1][6], "==", Ys[1])

    print(b0 + b1 * Xf[2][0] + b2 * Xf[2][1] + b3 * Xf[2][2] + b12 * Xf[2][3] + b13 * Xf[2][4]
          + b23 * Xf[2][5] + b123 * Xf[2][6], "==", Ys[2])

    print(b0 + b1 * Xf[3][0] + b2 * Xf[3][1] + b3 * Xf[3][2] + b12 * Xf[3][3] + b13 * Xf[3][4]
          + b23 * Xf[3][5] + b123 * Xf[3][6], "==", Ys[3])

    print(b0 + b1 * Xf[4][0] + b2 * Xf[4][1] + b3 * Xf[4][2] + b12 * Xf[4][3] + b13 * Xf[4][4]
          + b23 * Xf[4][5] + b123 * Xf[4][6], "==", Ys[4])

    print(b0 + b1 * Xf[5][0] + b2 * Xf[5][1] + b3 * Xf[5][2] + b12 * Xf[5][3] + b13 * Xf[5][4]
          + b23 * Xf[5][5] + b123 * Xf[5][6], "==", Ys[5])

    print(b0 + b1 * Xf[6][0] + b2 * Xf[6][1] + b3 * Xf[6][2] + b12 * Xf[6][3] + b13 * Xf[6][4]
          + b23 * Xf[6][5] + b123 * Xf[6][6], "==", Ys[6])

    print(b0 + b1 * Xf[4][0] + b2 * Xf[7][1] + b3 * Xf[7][2] + b12 * Xf[7][3] + b13 * Xf[7][4]
          + b23 * Xf[7][5] + b123 * Xf[7][6], "==", Ys[7])
    print("Результат збігається з середніми значеннями")
    print("-------------------------")

     # перевірка однорідності за Кохреном
     # дисперсії по рядках
    print("Критерій Кохрена")
    D = []
    Summa = 0
    for i in range(N):
        for j in range(m):
            Summa += pow((Y[i][j] - Ys[i]), 2)
        D.append(1 / m * Summa)
        Summa = 0
    print("D: ")
    for i in range(len(D)):
        print(D[i])
    print("-------------------------")
    Gp = max(D) / sum(D)
    print("Gp= ", Gp)
    f1 = m - 1
    f2 = N
    q = 0.05
    if m >= 11:
        for i in range(len(Gt2)):
            if m in Gt2[i][0]:
                crit = Gt2[i][1]
                break
    else:
        crit = Gt[f1]
    if Gp <= crit:
        print("Дисперсія однорідна")
        print(Gp, "<=", crit)
    else:
        print("Дисперсія не однорідна")
        m += 1
        print("M:", m)
        return func(m)
    print("-------------------------")
     # критерій Стьюдента
    print("Критерій Стьюдента")
    S2_b = sum(D) / N
    S2_betta = S2_b / (N * m)
    S_betta = math.sqrt(S2_betta)
    print("S2_b= {0} \n"
          "S2_betta= {1} \n"
          "S_betta= {2}".format(S2_b, S2_betta, S_betta))
    print("-------------------------")
    Xs = [[1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0, -1.0],  # 1
          [1.0, -1.0, -1.0, 1.0, 1.0, -1.0, -1.0, 1.0],  # 2
          [1.0, -1.0, 1.0, -1.0, -1.0, 1.0, -1.0, 1.0],  # 3
          [1.0, -1.0, 1.0, 1.0, -1.0, -1.0, 1.0, -1.0],  # 4
          [1.0, 1.0, -1.0, -1.0, -1.0, -1.0, 1.0, 1.0],  # 5
          [1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, -1.0],  # 6
          [1.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0],  # 7
          [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]]  # 8
    betta = []
    for j in range(N):
        s = 0
        for i in range(N):
            s+=Ys[i]*Xs[i][j]
        betta.append(s/N)
    print("betta: ")
    for i in range(len(betta)):
        print(betta[i])

    print("-------------------------")
    t = []
    for i in range(len(betta)):
        t.append(abs(betta[i]) / S_betta)
    print("t: ")
    for i in range(len(t)):
        print(t[i])
    print("-------------------------")
    f3 = f1 * f2
    print("f3=", f3)
    b = []
    b.append(b0)
    b.append(b1)
    b.append(b2)
    b.append(b3)
    b.append(b12)
    b.append(b13)
    b.append(b23)
    b.append(b123)
    t_tabl = scipy.stats.t.ppf((1 + (1 - q)) / 2, f3)
    if t[i] < t_tabl:
        b[i] = 0
        print(t[i], "<", t_tabl)
    print("-------------------------")
    y = []
    y.append(b0 + b1 * Xf[0][0] + b2 * Xf[0][1] + b3 * Xf[0][2]+ b12 * Xf[0][3] +
                 b13 * Xf[0][4] + b23 * Xf[0][5]+ b123 * Xf[0][6])

    y.append(b0 + b1 * Xf[1][0] + b2 * Xf[1][1] + b3 * Xf[1][2]+ b12 * Xf[1][3] +
                 b13 * Xf[1][4] + b23 * Xf[1][5]+ b123 * Xf[1][6])

    y.append(b0 + b1 * Xf[2][0] + b2 * Xf[2][1] + b3 * Xf[2][2]+ b12 * Xf[2][3] +
                 b13 * Xf[2][4] + b23 * Xf[2][5]+ b123 * Xf[2][6])

    y.append(b0 + b1 * Xf[3][0] + b2 * Xf[3][1] + b3 * Xf[3][2]+ b12 * Xf[3][3] +
                 b13 * Xf[3][4] + b23 * Xf[3][5]+ b123 * Xf[3][6])

    y.append(b0 + b1 * Xf[4][0] + b2 * Xf[4][1] + b3 * Xf[4][2]+ b12 * Xf[4][3] +
                 b13 * Xf[4][4] + b23 * Xf[4][5]+ b123 * Xf[4][6])

    y.append(b0 + b1 * Xf[5][0] + b2 * Xf[5][1] + b3 * Xf[5][2]+ b12 * Xf[5][3] +
                 b13 * Xf[5][4] + b23 * Xf[5][5]+ b123 * Xf[5][6])

    y.append(b0 + b1 * Xf[6][0] + b2 * Xf[6][1] + b3 * Xf[6][2]+ b12 * Xf[6][3] +
                 b13 * Xf[6][4] + b23 * Xf[6][5]+ b123 * Xf[6][6])

    y.append(b0 + b1 * Xf[7][0] + b2 * Xf[7][1] + b3 * Xf[7][2]+ b12 * Xf[7][3] +
                 b13 * Xf[7][4] + b23 * Xf[7][5]+ b123 * Xf[7][6])

    print("y: ")
    for i in range(len(y)):
        print(y[i])
    print("-------------------------")
    for i in range(len(y)):
        print(y[i], "==", Ys[i])
    print("Нуль гіпотеза виконується")
    print("-------------------------")
    print("Критерій Фішера")
    # критерій Фішера
    d = 0
    for i in range(len(b)):
        if b[i] != 0:
            d += 1
    print("d=", d)
    f4 = N - d
    Sum = 0
    for i in range(len(y)):
        Sum += pow((y[i] - Ys[i]), 2)
    S_ad = (m / (N - d)) * Sum
    print("S_ad= ", S_ad)
    Fp = S_ad / S2_b
    print("Fp= {0} \n"
          "f3= {1} \n"
          "f4= {2}".format(Fp, f3, f4))
    print("-------------------------")
    Ft = scipy.stats.f.ppf(1 - q, f4, f3)
    if Fp > Ft:
        print("Рівняння регресії неадекватно оригіналу при рівні значимості 0.05")
        print("Значення критерію=", Ft)
        return (func(3))
    else:
        print("Рівняння регресії адекватно оригіналу при рівні значимості 0.05")
        print("Значення критерію=", Ft)

func(3)
