import tensorflow as tf
'''
변수로 할달된 값은 반드시 초기화 이후에 사용해야한다
'''
var_node_1 = tf.Variable([5.0], dtype=tf.float32)
const_node_1 = tf.constant([10.0], dtype=tf.float32)
session = tf.Session()
init = tf.global_variables_initializer()
session.run(init)
print(session.run(var_node_1 * const_node_1))
session.run(var_node_1.assign([10.0]))
print(session.run(var_node_1))