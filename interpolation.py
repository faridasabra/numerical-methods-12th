def newton_divided_difference(x, y, x_val):
    if len(x) != len(y):
        raise ValueError("x and y must have the same length")
    n = len(x)
    
    if n == 2:
        diff = (y[1] - y[0]) / (x[1] - x[0])
        differences = {"First divided differences": [diff]}
        px = y[0] + (x_val - x[0]) * diff
        return px, differences
    
    elif n == 3:
        diff1_0 = (y[1] - y[0]) / (x[1] - x[0])
        diff1_1 = (y[2] - y[1]) / (x[2] - x[1])
        diff2 = (diff1_1 - diff1_0) / (x[2] - x[0])
        differences = {
            "First divided differences": [diff1_0, diff1_1],
            "Second divided differences": [diff2]
        }
        px = y[0] + (x_val - x[0]) * diff1_0 + (x_val - x[0]) * (x_val - x[1]) * diff2
        return px, differences
    
    elif n == 4:
        diff1_0 = (y[1] - y[0]) / (x[1] - x[0])
        diff1_1 = (y[2] - y[1]) / (x[2] - x[1])
        diff1_2 = (y[3] - y[2]) / (x[3] - x[2])
        diff2_0 = (diff1_1 - diff1_0) / (x[2] - x[0])
        diff2_1 = (diff1_2 - diff1_1) / (x[3] - x[1])
        diff3 = (diff2_1 - diff2_0) / (x[3] - x[0])
        differences = {
            "First divided differences": [diff1_0, diff1_1, diff1_2],
            "Second divided differences": [diff2_0, diff2_1],
            "Third divided differences": [diff3]
        }
        px = y[0] + (x_val - x[0]) * diff1_0 + \
             (x_val - x[0]) * (x_val - x[1]) * diff2_0 + \
             (x_val - x[0]) * (x_val - x[1]) * (x_val - x[2]) * diff3
        return px, differences
    
    elif n == 5:
        diff1_0 = (y[1] - y[0]) / (x[1] - x[0])
        diff1_1 = (y[2] - y[1]) / (x[2] - x[1])
        diff1_2 = (y[3] - y[2]) / (x[3] - x[2])
        diff1_3 = (y[4] - y[3]) / (x[4] - x[3])
        diff2_0 = (diff1_1 - diff1_0) / (x[2] - x[0])
        diff2_1 = (diff1_2 - diff1_1) / (x[3] - x[1])
        diff2_2 = (diff1_3 - diff1_2) / (x[4] - x[2])
        diff3_0 = (diff2_1 - diff2_0) / (x[3] - x[0])
        diff3_1 = (diff2_2 - diff2_1) / (x[4] - x[1])
        diff4 = (diff3_1 - diff3_0) / (x[4] - x[0])
        differences = {
            "First divided differences": [diff1_0, diff1_1, diff1_2, diff1_3],
            "Second divided differences": [diff2_0, diff2_1, diff2_2],
            "Third divided differences": [diff3_0, diff3_1],
            "Fourth divided differences": [diff4]
        }
        px = y[0] + (x_val - x[0]) * diff1_0 + \
             (x_val - x[0]) * (x_val - x[1]) * diff2_0 + \
             (x_val - x[0]) * (x_val - x[1]) * (x_val - x[2]) * diff3_0 + \
             (x_val - x[0]) * (x_val - x[1]) * (x_val - x[2]) * (x_val - x[3]) * diff4
        return px, differences
    
    else:
        raise ValueError("Number of points must be between 2 and 5")

def print_differences(differences):
    print("\nDivided Differences Table:")
    for order, diffs in differences.items():
        print(f"{order}:")
        for i, diff in enumerate(diffs):
            print(f"  {order.split()[0]} f[x_{i}..x_{i+order.count('divided')-1}] = {diff:.6f}")

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def get_point_list(prompt, min_points=2):
    print(prompt)
    points = []
    while True:
        entry = input(f"Enter a number (or 'done' to finish, minimum {min_points} points): ")
        if entry.lower() == 'done':
            if len(points) < min_points:
                print(f"Error: You need at least {min_points} points.")
                continue
            return points
        try:
            points.append(float(entry))
        except ValueError:
            print("Please enter a valid number or 'done' to finish.")

if __name__ == "__main__":
    print("Newton's Divided Difference Interpolation (Up to 4th Degree)")
    print("----------------------------------------------------------")
    
    x_points = get_point_list("Enter the x-coordinates of your data points:", min_points=2)
    y_points = get_point_list("Enter the y-coordinates of your data points:", min_points=len(x_points))
    
    while len(x_points) != len(y_points):
        print(f"Error: {len(x_points)} x-points but {len(y_points)} y-points. Both must match.")
        x_points = get_point_list("Re-enter x-coordinates:", min_points=2)
        y_points = get_point_list("Re-enter y-coordinates:", min_points=len(x_points))
    
    x_interpolate = get_float_input("Enter the x-value to interpolate: ")
    
    try:
        y_interpolated, differences = newton_divided_difference(x_points, y_points, x_interpolate)
        degree_used = min(len(x_points) - 1, 4)
        print("\nResults:")
        print(f"Interpolated value at x = {x_interpolate}: {y_interpolated:.6f}")
        print(f"Polynomial degree used: {degree_used}")
        print_differences(differences)
    except ValueError as e:
        print(f"Error: {e}")
