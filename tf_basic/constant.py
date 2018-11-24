# 텐서는 세션 내부에서 연산한다.
import tensorflow as tf
a= tf.constant(5.0, name= "a")
b= tf.constant(10.0, name= "b")
with tf.Session() as sess:
    print("a = ", sess.run(a))
    print("b = ", sess.run(b))