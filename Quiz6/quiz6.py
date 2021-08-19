import sys
try:
    file1 = open(sys.argv[1], "r")
    try:
        file2 = open(sys.argv[2], "r")
        for r in file1:
            print("------------")
            output = []
            r=r.strip("\n")
            r=r.strip(" ")
            r=r.split(" ")
            try:
                div = r[0]
                nondiv = r[1]
                start = r[2]
                finish = r[3]
                try:
                    div=int(round(float(div)))
                    nondiv=int(round(float(nondiv)))
                    start=int(round(float(start)))
                    finish = int(round(float(finish)))
                    try:
                        for number in range(start,finish+1):
                            if number%div==0 and number%nondiv!=0:
                                output.append(str(number))
                        t = file2.readline()
                        try:
                            t = t.strip("\n")
                            t = t.strip(" ")
                            t = t.split(" ")
                            print("My Results:" + "\t" + " ".join(output))
                            print("Results to compare:" + "\t" + " ".join(t))
                            if t != output:
                                raise AssertionError
                            else:
                                print("Goool!!!")
                        except AssertionError:
                            print("AssertionError:  results don’t match.")
                    except ZeroDivisionError:
                        print("ZeroDivisionError: You can’t divide by 0.")
                        t = file2.readline()
                        print("Given input:" + "\t" + " ".join(r))
                except ValueError:
                    print("ValueError: only  numeric  input  is  accepted.")
                    t = file2.readline()
                    print("Given input:" + "\t" + " ".join(r))
            except IndexError:
                print("IndexError: number of operands less than expected.")
                t = file2.readline()
                print("Given input:" + "\t" + " ".join(r))
    except IndexError:
        print("IndexError: number of input files less than expected.")
    except IOError:
        print("IOError:cannot open" + " " + sys.argv[2])
except IndexError:
    print("IndexError: number of input files less than expected.")
except IOError:
    print("IOError:cannot open"+" "+sys.argv[1])
except:
    print("kaBOOM: run for your life!")
finally:
    print()
    print("Game Over")