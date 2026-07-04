arr=[3,7,2,9,4]
max_val=arr[0]
for x in arr[1:]:
    if x> max_val:
        max_val=x
print(f"Max:{max_val}")