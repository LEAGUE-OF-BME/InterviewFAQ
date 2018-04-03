集成学习是将多个模型组合在一起形成一个更强大的模型。往往单一的模型存在缺陷，只在某些方面表现的好，集成学习能够把这些有偏好的模型组合在一起，通过集体的决定将缺陷纠正。Bagging是集成学习的一种重要方法。

### Bagging
Bagging全称是Bootstrap Aggregation，bootstrap的意思是对样本集D有放回地抽取N个样本。Bagging的流程如下：

1. bootstrap获取样本子集$\tilde{D}$，并据此训练一个模型
2. 重复n次，得到n个模型
3. 将n个模型线性组合成最终模型

Bagging的每个模型是同类模型，训练数据是重采样获得的，因此每个模型肯定不相同但是两两之间存在相关性。从bias和variance的角度考虑，每个模型的期望和方差近似相等。显然$E[\frac{\sum X_i}{n}]=E[X_i]$，所以bias不变。

方差$Var(\frac 1n \sum X_i) = \frac 1{n^2}\sum Var(X_i) + Cov(X_1,X_2,...,X_i)$，所有模型的方差近似相等，并且协方差肯定大于0，所以最终模型的方差会比$\frac {Var(X_i)}n$大一些，但小于$Var(X_i)$（所有模型完全相同的情况）。

综上，Bagging能降低模型的variance而不能降低bias。因此，在选择Bagging的基学习器时，通常选用强学习器（高variance低bias），比如CART决策树，将容易过拟合的学习器“平均”成泛化能力强的学习器。显然，Bagging是可以并行的算法（同时训练n个模型）

### 随机森林
随机森林是Bagging和[决策树](https://github.com/LEAGUE-OF-BME/InterviewFAQ/blob/master/ML%26DL/%E5%86%B3%E7%AD%96%E6%A0%91.md)的组合。令D为样本集，随机森林算法如下：

```
for t = 1,2,...,T:
	对样本集D重采样得到子数据集
	根据子数据集拟合一个决策树模型
G = 线性组合所有T个决策树模型
return G 
```
这里的决策树模型一般选用CART决策树，并且不需要剪枝，希望得到低bias高variance的决策树用于bagging。

随机森林在CART决策树分裂时有一点改进：普通决策树是遍历所有M个特征，随机森林是从所有M个特征中随机选择m个（m << M），从这m个中选择最优分裂点。

### OOB（out of bag）
所有bagging类的算法，包括随机森林，都可以使用OOB样本来做测试集验证误差。OOB指的是那些每一次重采样都没有被选中的样本，一个样本是OOB的概率为$P=(1-\frac 1N)^N$，当重采样次数趋向于∞时，概率为$\frac 1e$。大约有不到三分之一的样本是OOB样本，不参与训练，可以直接作为验证集。
