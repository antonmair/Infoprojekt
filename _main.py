#solve Trassenfinder
class Request:
    def __init__(self, polist):##unfinished
        self.polist = polist


def main():  
    #Create pointlist (polist) using user imput
    # x1 = input("x 1:")#start of vec1 x
    # x2 = input("x 2:")#end of vec1 x 
    # x3 = input("x 3:")#end of vec2 x
    # x4 = input("x 4:")#start of vec2 x
    # y1 = input("y 1:")#start of vec1 y
    # y2 = input("y 2:")#end of vec 1 y 
    # y3 = input("y 3:")#end of vec 2 y
    # y4 = input("y 4:")#start of vec 2 y
    
    #dev version

    #this example is a bit off
    # x1=2
    # x2=2.1
    # x3=5
    # x4=6
    # y1=1
    # y2=2
    # y3=5
    # y4=5

    #this example works perfectly, i think
    # x1=1
    # x2=2
    # x3=20
    # x4=21
    # y1=5
    # y2=6
    # y3=21
    # y4=22

    #this one doesnt work
    # x1=1
    # x2=2
    # x3=3
    # x4=4
    # y1=5
    # y2=6
    # y3=7
    # y4=8

    #example with multiple same works perfectly until i=4
    x1=1
    x2=2
    x3=8
    x4=9
    y1=3
    y2=3
    y3=3
    y4=3
    polist = [
        [x1,x2,x3,x4],
        [y1,y2,y3,y4]
    ]
    #polist range on first iteration is from [0][0] and [1][3]
    #first index 0 = x 1 = y
    #create request as class (not sure why)
    request = Request(polist)

    for i in range(4):# amount of iterations (line versions) sollte nicht ueber 10 sein weil to much
        
        #insert and move points
        from pointinserter import spawner
        if __name__ == '__main__':
            polist = spawner(polist)
        print(polist) #cosmetic

        #plot polist
        from plotter import polistplot
        if __name__ == '__main__':
            polistplot(polist)

main()
