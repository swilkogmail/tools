DROP TABLE minesweep;

CREATE TABLE minesweep
(
x NUMBER,
y NUMBER,
mine varchar2(1))
;

insert into mine values (1,1,'N');
insert into mine values (1,2,'N');
insert into mine values (1,3,'N');
insert into mine values (1,4,'N');
insert into mine values (1,5,'N');
insert into mine values (2,1,'Y');
insert into mine values (2,2,'Y');
insert into mine values (2,3,'N');
insert into mine values (2,4,'N');
insert into mine values (2,5,'Y');
insert into mine values (3,1,'Y');
insert into mine values (3,2,'N');
insert into mine values (3,3,'N');
insert into mine values (3,4,'Y');
insert into mine values (3,5,'N');
insert into mine values (4,1,'N');
insert into mine values (4,2,'N');
insert into mine values (4,3,'Y');
insert into mine values (4,4,'N');
insert into mine values (4,5,'N');
insert into mine values (5,1,'Y');
insert into mine values (5,2,'N');
insert into mine values (5,3,'Y');
insert into mine values (5,4,'Y');
insert into mine values (5,5,'N');


SELECT * FROM minesweep;

/*
count the number of mines that
surround the co-ordinates
*/
SELECT sum(mine) mines
  FROM
(
	(SELECT 1 mine FROM minesweep WHERE x = :x-1 AND y = :y AND mine = 'Y') -- LEFT
	UNION all
	(SELECT 1 mine FROM minesweep WHERE x = :x+1 AND y = :y AND mine = 'Y') -- RIGHT
	UNION all
	(SELECT 1 mine FROM minesweep WHERE x = :x-1 AND y = :y+1 AND mine = 'Y') -- LEFT up one
	UNION all
	(SELECT 1 mine FROM minesweep WHERE x = :x-1 AND y = :y-1 AND mine = 'Y') -- LEFT down one
	UNION all
	(SELECT 1 mine FROM minesweep WHERE x = :x+1 AND y = :y+1 AND mine = 'Y') -- RIGHT up one
	UNION all
	(SELECT 1 mine FROM minesweep WHERE x = :x+1 AND y = :y-1 AND mine = 'Y') -- RIGHT down one
	UNION all
	(SELECT 1 mine FROM minesweep WHERE x = :x   AND y = :y-1 AND mine = 'Y') -- DOWN
	UNION all
	(SELECT 1 mine FROM minesweep WHERE x = :x   AND y = :y+1 AND mine = 'Y') -- UP
);