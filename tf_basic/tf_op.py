import tensorflow as tf
# 텐서는 3개의 파라미터를 갖는다.
'''
Arithmetic operations : add, subtract, multiply, ...
Matrix operations : matmul, matrix_inverse, ...
Control flow operations : tuple, group, …
Logical operations : logical_and, logical_not, …
Comparison operations : equal, less, not_equal, …
Debugging operations : is_finite, is_inf, ...

'''

# x = tf.constant([[1,2]])
# print(x)

# Tensor("Const:0", shape=(1, 2), dtype=int32)
# Tensor(랭크, 쉐입, 데이터타입)
# 랭크(Rank)는 텐서의 차원(Dimension)을 의미함
# 랭크가 0 이라면 스칼라
# 1이면 벡터
# 2는 행렬
# 3은 텐서
# 쉐입은 행1 * 열2
# 타입은 정수
# 텐서는 그래프 생성 / 그래프 실행 이라는 두가지를 거친다
# 컴공에서 그래프를 노드와 엣지로 이루어진 자료구조로 정의한다

# 텐서플로는 노드에 연산 변수 산수 등을 정의하고 노드들간의 연결인 엣지를 통해 실제 텐서를 주고 받으며 계산을 실행함
node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0, dtype=tf.float32)
node3 = node1 + node2
print(node3)
#Tensor("add:0", shape=(), dtype=float32)
with tf.Session() as sess:
    print(sess.run(node3))