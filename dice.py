# import random
# import plotly.express as px
# import plotly.figure_factory as ff

# diceSum = []
# time = []
# for times in range(0,100):
#     die1 = random.randint(1,6)
#     die2 = random.randint(1,6)
#     dice = die1 + die2
#     diceSum.append(dice)
#     time.append(times)
# fig = px.bar(x=diceSum, y=time)
# fig.show()

import random
import plotly.figure_factory as ff

diceSum = []
for times in range(0,100):
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    dice = die1 + die2
    diceSum.append(dice)

fig = ff.create_distplot([diceSum],["result"])
fig.show()