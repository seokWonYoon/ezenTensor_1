import tensorflow as tf
def test1():
    a = tf.placeholder(tf.int16)
    b = tf.placeholder(tf.int16)
    add = tf.add(a,b)
    mul = tf.multiply(a,b)

    with tf.Session() as sess:
        r1 = sess.run(add, feed_dict = {a : 2,b:4})
        r2 = sess.run(mul, feed_dict = {a : 2,b:4})

        print(r1, r2)
def test2():
    x = tf.Variable([1.0, 2.0])
    y = tf.constant([3.0, 3.0])
    
    sub = tf.subtract(x, y)
    with tf.Session() as sess:
        x.initializer.run()
        r1 = sess.run(sub)
        print(r1)
if __name__ == "__main__":
    test2()