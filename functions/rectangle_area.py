def rectangle_area_calc(width, height):
    area = width * height
    return area


input_width = int(input())
input_height = int(input())

result = rectangle_area_calc(input_width, input_height)
print(result)
