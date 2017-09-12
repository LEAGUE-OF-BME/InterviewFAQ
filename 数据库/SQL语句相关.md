# SQL语句总结

"Persons" 表：

| Id_P | LastName | FirstName | Address        | City     |
| ---- | -------- | --------- | -------------- | -------- |
| 1    | Adams    | John      | Oxford Street  | London   |
| 2    | Bush     | George    | Fifth Avenue   | New York |
| 3    | Carter   | Thomas    | Changan Street | Beijing  |

"Orders" 表：

| Id_O | OrderNo | Id_P |
| ---- | ------- | ---- |
| 1    | 77895   | 3    |
| 2    | 44678   | 3    |
| 3    | 22456   | 1    |
| 4    | 24562   | 1    |
| 5    | 34764   | 65   |



## 1. Join关键字的使用

- ### 内连接（INNER JOIN）

![INNER JOIN](https://user-gold-cdn.xitu.io/2017/9/11/40e1382d25d9b8fc2059bf71bd254baa?imageView2/0/w/1280/h/960)

```mysql
SELECT Persons.LastName, Persons.FirstName, Orders.OrderNo
FROM Persons
INNER JOIN Orders
ON Persons.Id_P=Orders.Id_P
ORDER BY Persons.LastName
```

**查询结果：**

| LastName | FirstName | OrderNo |
| -------- | --------- | ------- |
| Adams    | John      | 22456   |
| Adams    | John      | 24562   |
| Carter   | Thomas    | 77895   |
| Carter   | Thomas    | 44678   |

INNER JOIN 关键字在表中存在至少一个匹配时返回行。如果 "Persons" 中的行在 "Orders" 中没有匹配，就不会列出这些行。

- ### 左连接（LEFT JOIN）

![LEFT JOIN](https://user-gold-cdn.xitu.io/2017/9/11/cd7bd77cfb29669ad3002517ff5b9f9b?imageView2/0/w/1280/h/960)

```mysql
SELECT Persons.LastName, Persons.FirstName, Orders.OrderNo
FROM Persons
LEFT JOIN Orders
ON Persons.Id_P=Orders.Id_P
ORDER BY Persons.LastName
```

**查询结果：**

| LastName | FirstName | OrderNo |
| -------- | --------- | ------- |
| Adams    | John      | 22456   |
| Adams    | John      | 24562   |
| Carter   | Thomas    | 77895   |
| Carter   | Thomas    | 44678   |
| Bush     | George    |         |

LEFT JOIN 关键字会从左表 (Persons) 那里返回所有的行，即使在右表 (Orders) 中没有匹配的行。

- ### 右连接（RIGHT JOIN）

![RIGHT JOIN](https://user-gold-cdn.xitu.io/2017/9/11/2b9aac7f389b2d9a99a71294010564d8?imageView2/0/w/1280/h/960)

```mysql
SELECT Persons.LastName, Persons.FirstName, Orders.OrderNo
FROM Persons
RIGHT JOIN Orders
ON Persons.Id_P=Orders.Id_P
ORDER BY Persons.LastName
```

**查询结果：**

| LastName | FirstName | OrderNo |
| -------- | --------- | ------- |
| Adams    | John      | 22456   |
| Adams    | John      | 24562   |
| Carter   | Thomas    | 77895   |
| Carter   | Thomas    | 44678   |
|          |           | 34764   |

RIGHT JOIN 关键字会从右表 (Orders) 那里返回所有的行，即使在左表 (Persons) 中没有匹配的行。

- ### 全连接（FULL JOIN）

  ![FULL OUTER JOIN](https://user-gold-cdn.xitu.io/2017/9/11/1bf21aee32cd03858703c9956c43cb4a?imageView2/0/w/1280/h/960)

```mysql
SELECT Persons.LastName, Persons.FirstName, Orders.OrderNo
FROM Persons
FULL JOIN Orders
ON Persons.Id_P=Orders.Id_P
ORDER BY Persons.LastName
```

**查询结果：**

| LastName | FirstName | OrderNo |
| -------- | --------- | ------- |
| Adams    | John      | 22456   |
| Adams    | John      | 24562   |
| Carter   | Thomas    | 77895   |
| Carter   | Thomas    | 44678   |
| Bush     | George    |         |
|          |           | 34764   |

FULL JOIN 关键字会从左表 (Persons) 和右表 (Orders) 那里返回所有的行。如果 "Persons" 中的行在表 "Orders" 中没有匹配，或者如果 "Orders" 中的行在表 "Persons" 中没有匹配，这些行同样会列出。



## 2.Union关键字的使用

UNION 操作符用于合并两个或多个 SELECT 语句的结果集。

请注意，UNION 内部的 SELECT 语句必须拥有相同数量的列。列也必须拥有相似的数据类型。同时，每条 SELECT 语句中的列的顺序必须相同。

默认地，UNION 操作符选取不同的值。如果允许重复的值，请使用 UNION ALL。

UNION 结果集中的列名总是等于 UNION 中第一个 SELECT 语句中的列名。

```mysql
SELECT LastName FROM Persons WHERE Id_P = 1
UNION
SELECT LastName FROM Persons WHERE Id_P = 2
```

**查询结果为：**Adams 和 Bush



## 3.SQL 子查询

子查询用于为主查询返回其所需数据，或者对检索数据进行进一步的限制。

子查询可以在 SELECT、INSERT、UPDATE 和 DELETE 语句中，同 =、<、>、>=、<=、IN、BETWEEN 等运算符一起使用。

使用子查询必须遵循以下几个规则：

- 子查询必须括在圆括号中。
- 子查询的 SELECT 子句中只能有一个列，除非主查询中有多个列，用于与子查询选中的列相比较。
- 子查询不能使用 ORDER BY，不过主查询可以。在子查询中，GROUP BY 可以起到同 ORDER BY 相同的作用。
- 返回多行数据的子查询只能同多值操作符一起使用，比如 IN 操作符。
- SELECT 列表中不能包含任何对 BLOB、ARRAY、CLOB 或者 NCLOB 类型值的引用。
- 子查询不能直接用在集合函数中。
- BETWEEN 操作符不能同子查询一起使用，但是 BETWEEN 操作符可以用在子查询中。

**单行子查询**：

```mysql
SELECT LastName FROM Persons WHERE Id_P = (SELECT Id_P FROM orders where Id_O=3)
```

**多行子查询**：

```mysql
SELECT LastName FROM Persons WHERE Id_P in (SELECT Id_P FROM orders where Id_O<4)
```

**多列子查询**:

```mysql
SELECT OrderNo,Id_P FROM orders WHERE (OrderNo,Id_P) in (SELECT max(OrderNo),Id_P FROM orders  GROUP BY Id_P)
```

**内联视图子查询:**

```mysql
SELECT lastname,firstname FROM( SELECT lastname, firstname, city FROM persons ORDER BY city) tmp
```



## 4.SQL GROUP BY 语句

GROUP BY 语句用于结合合计函数，根据一个或多个列对结果集进行分组。

```mysql
SELECT Id_P, sum(OrderNo) as Num from orders GROUP BY Id_P
```

**查询结果：**

| Id_P | Num    |
| ---- | ------ |
| 1    | 47018  |
| 3    | 122573 |
| 65   | 34764  |

**GROUP BY 一个以上的列**，即合并Id_P, Id_O均相同的记录

```
SELECT Id_P,Id_O, sum(OrderNo) as Num from orders GROUP BY Id_P,Id_O;
```

## 5. SQL HAVING 子句

在 SQL 中增加 HAVING 子句原因是，WHERE 关键字无法与合计函数一起使用。

HAVING 子句使你能够指定过滤条件，从而控制查询结果中哪些组可以出现在最终结果里面。

WHERE 子句对被选择的列施加条件，而 HAVING 子句则对 GROUP BY 子句所产生的组施加条件。

```mysql
SELECT Id_P, sum(OrderNo) as Num from orders GROUP BY Id_P HAVING sum(OrderNo)<50000
```

