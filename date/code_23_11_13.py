s=int(input("请输入路程:"))
val=0
if s<=2:
    val+=8
elif s>=2 and s<=12:
    val=8+(s-2)*1.5
else:
    val=8+10*1.5+(s-12)*2

print(val)