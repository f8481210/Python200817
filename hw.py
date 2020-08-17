math = int(input("數學:"))
eng = int(input("英文:"))
if math >=0 and math <=100 and \
eng >=0 and eng<=100:
    if math>=90 and eng>=90:
        print("有獎品")
    elif math<60 and eng<60:
        print("有處罰")
    elif math<60 or eng<60:
        print("再加油")
else:
    print("ERROR")