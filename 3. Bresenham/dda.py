
def get_line(x0, y0, x1, y1):
    points = [(x0, y0)]
    
    dx = abs(x0 - x1)
    dy = abs(y0 - y1)
 
    steps = max(dx, dy)
 
    xk = dx/steps
    yk = dy/steps
 
    x = float(x0)
    y = float(y0)
 

 
    for i in range(steps+1):
        points.append((x, y))

        x = x + xk
        y = y + yk
    return points

if __name__ == "__main__":
    print(get_line(2, 2, 10, 5))