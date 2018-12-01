import tensorflow as tf

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

add = tf.add(X,Y)
mul = tf.multiply(X,Y)


# step1 node의 선택
add_hist = tf.summary.scalar("add_scalar", add) # return이 단일
add_hist = tf.summary.scalar("mul_scalar", mul) 

# step2 summary로 데이터 통합
merged = tf.summary.merge_all()  # 두개의 동작을 통합함

with tf.Session() as sess:    
    sess.run(tf.global_variables_initializer()) #변수초기화

# step3 writer 생성
    writer =tf.summary.FileWriter("./logs/add", sess.graph)
# step4 노드추가
    for i in range(100):
        summary = sess.run(merged, {X:i*1.0, Y:2.0})
        writer.add_summary(summary, i)
# step5 콘솔에서 명령실행 => 텐서보드 실행
