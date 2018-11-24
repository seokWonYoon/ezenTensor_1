
# 텐서 보드
import tensorflow as tf
a = tf.constant(20, name='cons_a')
b = tf.constant(30, name='cons_b')
y = tf.Variable(a + b + 7 , name='val_y')
init = tf.global_variables_initializer()
# 세션을 초기화 하는 순간 변수에 값이 지정된다/ 데이터를 가지고 학습시켜서 적정한 값을 찾는다.
# 그래프를 관련정보를 기본 디렉토리 하위에 logs 폴더에 저장한다. 
with tf.Session() as sess:
    writer = tf.summary.FileWriter('./logs', sess.graph)
    sess.run(init)
    res = sess.run(y)
    print(res)