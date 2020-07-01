# There is a horizontal row of  cubes. The length of each cube is given. 
# You need to create a new vertical pile of cubes. The new pile should follow these directions: if  is on top of  then .

# When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. 
# Print "Yes" if it is possible to stack the cubes. Otherwise, print "No". Do not print the quotation marks.


def checker(boxes, cubes):
    max_elem = 0
    if (boxes[0]>boxes[-1]):
        max_elem = boxes[0]
        del boxes[0]
    elif (boxes[0]<boxes[-1]):
        max_elem = boxes[-1]
        del boxes[-1]
    else:
        max_elem = boxes[0]
        del boxes[0]
    while(boxes):
        if(max_elem>= boxes[0]):
            if max_elem >= boxes[-1]:
                if boxes[0] >= boxes[-1]:
                    max_elem = boxes[0]
                    del boxes[0]
                else:
                    max_elem = boxes[-1]
                    del boxes[-1]
            else:
                max_elem = boxes[0]
                del boxes[0]
        elif max_elem >=boxes[-1]:
            max_elem = boxes[-1]
            del boxes[-1]
        else:
            return "No"
    return "Yes"

n = int(input())
for i in range(0, n):
    cubes = int(input())
    boxes = list(map(int,input().split()))
    print(checker(boxes, cubes))
