import matplotlib.pyplot as plt

plt.style.use('ggplot')
mbr = ['김','이','박','최', '심']

mbr_idx = range(len(mbr))
score = [100, 80 , 60 ,50, 30]
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.bar(mbr_idx, score, align = 'center', color='blue')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
plt.xticks(mbr_idx, mbr, rotation = 0 , fontsize='small')
plt.xlabel('학생이름')
plt.ylabel('점수')
plt.title('학생별 점수')
plt.savefig('score.png', dpi=400, bbox_inches='tight') #  bbox_inches='tight' tight 는 그림여백을 제거
plt.show()
