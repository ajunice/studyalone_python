#float 자료형 기본

output_a = "{:f}".format(99.123)
output_b = "{:15f}".format(99.123) #15칸 만들기
output_c = "{:+15f}".format(99.123) #15칸에 부호 추가하기
output_d = "{:+015f}".format(99.123) #15칸에 부호 추가하고 0으로 채우기

print(output_a)
print(output_b)
print(output_c)
print(output_d)