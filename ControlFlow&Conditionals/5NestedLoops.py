import time
start_time=time.time()
# # Outer Loop
# for i in range(10):
#     # inner loop
#     for j in range(10):
#         print(0,end=" ")
#     print()

# print('Different loop')

# Outer Loop
for i in range(2):
    # Inner Loop
    for j in range(10):
        print(0, end=" ")
    print()

print(round((time.time()-start_time),2))





