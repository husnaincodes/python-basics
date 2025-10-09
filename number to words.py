
num = input("Enter Six digit number :")
if len(num)>6:
    print("Invalid Input")
else:
    words = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
    if len(num)==6:
        print(words[int(num[0])],words[int(num[1])],words[int(num[2])],words[int(num[3])],words[int(num[4])],words[int(num[5])])
    elif len(num)==5:
        print(words[int(num[0])],words[int(num[1])],words[int(num[2])],words[int(num[3]),words[int(num[4])]])
    elif len(num)==4:
        print(words[int(num[0])],words[int(num[1])],words[int(num[2])],words[int(num[3])])
    elif len(num)==3:
        print(words[int(num[0])],words[int(num[1])],words[int(num[2])])
    elif len(num)==2:
        print(words[int(num[0])],words[int(num[1])])
    elif len(num)==1:
        print(words[int(num[0])])