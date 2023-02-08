class sinhvien:
  def __init__(sv,ma,ten):
    sv.msv = ma;
    sv.name = ten;
  def inthongtin(sv):
    print("ma sinh vien: ",sv.msv)
    print("ten sinh vien: ",sv.name)
sinhviena = sinhvien('2211020','vo van tai')

sinhviena.inthongtin()