# SQL语句表

## 目录
[TOC]

## 创建数据库
```sql
CREATE DATABASE school;
```

## 创建数据表

### 学生表

```sql
CREATE TABLE student(
id INT NOT NULL AUTO_INCREMENT,  /* 学生表id */
school_id INT(11) NOT NULL,  /* 学号 */
name VARCHAR(30) NOT NULL, /* 姓名 */
sex INT NOT NULL,  /* 性别 */
age INT NOT NULL,  /* 年龄 */
class_name INT NOT NULL,  /* 班级名称 */
PRIMARY KEY (id)  /* 学生表主键 */
);
```

```sql
INSERT INTO student(school_id, name, sex, age, class_name) VALUES(100005, 'Bob', 1, 17, 301);
```

### 班级表

```sql
CREATE TABLE class(
id INT NOT NULL AUTO_INCREMENT, /* 班级表id */
class_name INT NOT NULL, /* 班级名称 */
master_id INT, /* 班长id */
is_key INT NOT NULL, /* 是否重点班级 */
PRIMARY KEY (id) /* 班级表主键 */
);
```

```sql
INSERT INTO class(class_name, master_id, is_key) VALUES(301, 1, 1);
```

### 课程表

```sql
CREATE TABLE course(
id INT NOT NULL AUTO_INCREMENT, /* 课程表id */
course_name VARCHAR(10) NOT NULL, /* 课程名称 */
grade INT NOT NULL, /* 当前课程所属年级 */
president_id INT, /* 课代表id */
is_neces INT NOT NULL, /* 是否必修课 */
credit INT NOT NULL, /* 学分 */
PRIMARY KEY (id) /* 课程表主键 */
);
```

```sql
INSERT INTO course(course_name, grade, president_id, is_neces, credit) VALUES('math', 3, 100214, 1, 4);
```

```sql
ALTER table course ADD column class_name INT;
```

### 成绩表

```sql
CREATE TABLE score(
id INT NOT NULL AUTO_INCREMENT, /* 成绩表id */
course_id INT NOT NULL, /* 课程id */
school_id INT NOT NULL, /* 学号 */
score INT, /* 考试成绩 */
PRIMARY KEY (id) /* 成绩表主键 */
);
```

```sql
INSERT INTO score(course_id, school_id, score) VALUES(1, 100005, 88);
```

## 导入导出
```sql
/* 导出数据库 */
MYSQLDUMP -u root -p school > F:/Data/MySQL/school.sql
/* 导入数据库 */
SOURCE /root/upload/school.sql;
```

## 查询实战

### 查询所有课程名称
```sql
SELECT course_name FROM course GROUP BY course_name;
```

### 查询一个学生全部课程
```sql
/* 子查询 */
SELECT course_name FROM course WHERE id in (SELECT course_id FROM score WHERE school_id=100005);
```

### 统计每个班级有多少学生
```sql
SELECT class_name, count(*) FROM student GROUP BY class_name;
```

### 根据学号查询一个学生的成绩单
```sql
/* WHERE */
SELECT st.name, co.course_name, sc.score
FROM student st, score sc, course co
WHERE sc.school_id=st.school_id
AND co.id=sc.course_id
AND st.school_id=100005;
```

```sql
/* JOIN */
SELECT st.name, co.course_name, sc.score
FROM student st
JOIN score sc ON sc.school_id=st.school_id
JOIN course co ON co.id=sc.course_id
WHERE st.school_id=100005;
```

### 查询各个班级的班长姓名
```sql
/* WHERE */
SELECT cl.class_name, st.name
FROM class cl, student st
WHERE cl.master_id=st.school_id;
```

```sql
/* JOIN */
SELECT cl.class_name, st.name
FROM class cl
JOIN student st
ON cl.master_id=st.school_id;
```

```sql
/* LEFT JOIN */
SELECT cl.class_name, st.name
FROM class cl
LEFT JOIN student st
ON cl.master_id=st.school_id;
```

```sql
/* RIGHT JOIN */
SELECT cl.class_name, st.name
FROM student st
RIGHT JOIN class cl
ON cl.master_id=st.school_id;
```

### 其他查询
```sql
SELECT name, class_name FROM student GROUP BY class_name
UNION ALL
SELECT id, class_name FROM class;
```