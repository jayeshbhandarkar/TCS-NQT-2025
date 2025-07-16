def classify_temperature(temp):
    if temp < 10:
        return "it's very cool"
    elif 10 <= temp <= 20:
        return "it's cold"
    else:
        return "it's warm"

temp1 = int(input())
temp2 = int(input())

category1 = classify_temperature(temp1)
category2 = classify_temperature(temp2)

average = (temp1 + temp2) / 2.0

print(f"{category1}, {category2}, {average}, {temp2}, {temp1}")
