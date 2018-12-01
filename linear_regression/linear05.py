import tensorflow as tf
import matplotlib.pyplot as plt

tf.set_random_seed(777)
W = tf.placeholder(tf.float32)
#b = tf.Variable([-.3],tf.float32) # 차트보기위해 b 생략

# Model input and output
X = [1,2,3]
Y = [1,2,3]

linear_model = X * W # + b

cost = tf.reduce_sum(tf.square(linear_model - Y))
sess = tf.Session()
W_history =[]
cost_history =[]
for i in range(-30,50):
    curr_W = i *0.1
    curr_cost = sess.run(cost,{W:curr_W})
    W_history.append(curr_W)
    cost_history.append(curr_cost)

plt.plot(W_history, cost_history)
plt.show()