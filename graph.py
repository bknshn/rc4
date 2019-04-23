import matplotlib.pyplot as plt

z1_data = list(open('z1_result.txt'))
z1 = [int(line.split(' ')[1]) for line in z1_data[1:]]
plt.plot(z1)
plt.show()

z2_data = list(open('z2_result.txt'))
z2 = [int(line.split(' ')[1]) for line in z2_data[4:]]
plt.plot(z2)
plt.show()
