price = 5000
weight = 23

# price가 3000보다 작고 weight가 30보다 크다면 => 만족 X
if price > 3000 and weight > 30 :
    if price > 6000 :
        print("p1")
    else :
        print("p2")
# if문을 만족시키지 못했기 때문에 else문으로 넘어옴, weight가 10보다 크다면 => 참이기에 p3를 출력
else:
    if weight > 10:
        print("p3")
    else:
        print("p4")