import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sb
sb.set()

df = pd.read_csv('student_scores.csv')
y = df['Scores']
x1 = df['Hours']
x = sm.add_constant(x1)
result = sm.OLS(y, x).fit()
print(result.summary())
plt.scatter(x1, y)
Y = 9.7758*x1+2.4837
fig = plt.plot(x1, Y, lw=2, color='red', label='regression line')
plt.title('HOURS VS SCORES')
plt.xlabel('HOURS', fontsize=20)
plt.ylabel('SCORES', fontsize=20)
plt.show()
