import matplotlib.pyplot as plt

acc = [0.3962, 0.3962, 0.4396, 0.3245, 0.3396, 0.3321, 0.3113, 0.3321, 0.2679, 0.2811]

plt.plot(acc, label='accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0, 0.8])
plt.legend(loc='lower right')

plt.show()

plt.clf()
acc = [0, 0.25, 0.5, 0.5, 0.5, 0.5, 0.75, 0.75, 0.75, 1]

plt.plot(acc, label='yo')
plt.xlabel('3214')
plt.ylabel('ssdg')
plt.ylim([0, 0.8])
plt.legend(loc='lower right')

plt.show()