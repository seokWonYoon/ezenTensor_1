import tensorflow as tf

'''
텐서플로우에는 세가지 핵심 데이터 구조인 상수-Constant 변수-Variable 플레이스홀더-Placeholder 가 잇다.

플레이스홀더는 placeholder 연산 노드를 가르키는 텐서(다차원배열)이며 텐서프롤우에서 그래프를 실행할 때 사용자가 데이터를 주입할 수 있는 통로
tf.placeholder와 tf.Variable의 차이점
tf.Variable을 사용하면서 선언할 때 초기값을 반드시 제공해야한다
tf.placeholder 를 사용하면 초기값을 제공할 필요가 없으므로 Session.run의 feed_dict 인수를 사용하여 런타임을 지정할 수 있다.

'''



p1 = tf.placeholder(dtype=tf.float32)
p2 = tf.placeholder(dtype=tf.float32)

multi_node_1 = p1 * 3
multi_node_2 = p1 * p2


session = tf.Session()
print(session.run(multi_node_2, {p1:4.0, p2:[2.0,5.0]}))