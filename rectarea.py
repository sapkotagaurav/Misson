def area(ax1,ay1,ax2,ay2,bx1,by1,bx2,by2):
    area1 = abs(ax2-ax1) *abs(ay2-ay1)
    area2 = abs(bx2-bx1) *abs(by2-by1)

    xd,yd =(min(ax2,bx2)-max(ax1,bx1)), (min(ay2,by2)-max(ay1,by1))
    ovr_area=0
    if xd>0 and yd>0:
        ovr_area= xd*yd
    

    return area1+area2-ovr_area 


print(area(-2,-2,2,2,3,3,4,4))


def rect_overlap(l1,l2):
    xd, yd = min(l1[2],l2[2]) - max(l1[0],l2[0]), min(l1[3],l2[3]) - max(l1[1],l2[1])
    return xd>0 and yd>0

print(rect_overlap([0,0,1,1],[2,2,3,3]))