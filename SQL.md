# SQL语句表

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
class_id INT NOT NULL,  /* 班级id */
PRIMARY KEY (id)  /* 学生表主键 */
);
```

```sql
INSERT INTO student(school_id, name, sex, age, class_id) VALUES(100005, 'Bob', 1, 17, 1);
```

### 班级表

```sql
CREATE TABLE class(
id INT NOT NULL AUTO_INCREMENT, /* 班级表id */
class_name VARCHAR(10) NOT NULL, /* 班级名称 */
master_id INT, /* 班长id */
is_key INT NOT NULL, /* 是否重点班级 */
PRIMARY KEY (id) /* 班级表主键 */
);
```

```sql
INSERT INTO class(class_name, master_id, is_key) VALUES('3-1', 1, 1);
```

### 课程表

```sql
CREATE TABLE course(
id INT NOT NULL AUTO_INCREMENT, /* 课程表id */
course_name VARCHAR(10) NOT NULL, /* 课程名称 */
president_id INT, /* 课代表id */
is_neces INT NOT NULL, /* 是否必修课 */
credit INT NOT NULL, /* 学分 */
PRIMARY KEY (id) /* 课程表主键 */
);
```

```sql
INSERT INTO course(course_name, president_id, is_neces, credit) VALUES('math', 1, 1, 4);
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

## 数据表查询

```sql
SELECT c.class_name, s.name FROM student s, class c WHERE s.class_id=c.id; /* 查询各个班级上的学生姓名 */
```

```sql
SELECT c.class_name, s.name FROM student s JOIN class c WHERE s.class_id=c.id; /* 查询各个班级上的学生姓名 */
```

```sql
SELECT * FROM student s CROSS JOIN class c; /* 查询student表和class表的笛卡尔积 */
```

```sql
SELECT s.name, c.class_name FROM student s LEFT JOIN class c ON s.class_id=c.id;
```

```sql
SELECT * FROM student s LEFT JOIN class c ON s.class_id;
```
