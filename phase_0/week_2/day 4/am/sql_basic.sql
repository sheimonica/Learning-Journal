-- membuat tabel
CREATE TABLE teachers (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    first_name varchar(25) NOT NULL,
    last_name varchar(50),
    school varchar(50) NOT NULL,
    hire_date date,
    salary numeric
    );
    
-- tambah column age
ALTER TABLE teachers ADD age INT;

-- hapus column age
ALTER TABLE teachers DROP COLUMN age;

-- ubah tipe data di column
ALTER TABLE teachers MODIFY COLUMN salary INT;

-- ubah nama column
ALTER TABLE teachers RENAME TO guru;

-- ubah nama column 2
ALTER TABLE guru RENAME TO teachers;

-- insert data
INSERT INTO teachers (id,first_name, last_name, school, hire_date, salary)
    VALUES (1,'Janet', 'Smith', 'MIT', '2011-10-30', 36200),
           (2,'Lee', 'Reynolds', 'MIT', '1993-05-22', 65000),
           (3,'Samuel', 'Cole', 'Cambridge University', '2005-08-01', 43500),
           (4,'Samantha', 'Bush', 'Cambridge University', '2011-10-30', 36200),
           (5,'Betty', 'Diaz', 'Cambridge University', '2005-08-30', 43500),
           (6,'Kathleen', 'Roush', 'MIT', '2010-10-22', 38500),
           (7,'James', 'Diaz', 'Harvard University', '2003-07-18', 61000),
           (8,'Zack', 'Smith', 'Harvard University', '2000-12-29', 55500),
           (9,'Luis', 'Gonzales', 'Standford University', '2002-12-01', 50000),
           (10,'Frank', 'Abbers', 'Standford University', '1999-01-30', 66000);

-- lihat isi tabel teachers
SELECT * FROM teachers;

-- menghapus isi dari table teachers
TRUNCATE TABLE teachers;
SELECT * FROM teachers;

-- menghapus tabel teachers
DROP TABLE teachers;

-- update data tabel
UPDATE teachers
SET salary=50000
WHERE id=3;

-- menghapus data di tabel
DELETE FROM teachers
WHERE id=6;
SELECT * FROM teachers;

-- menambah data baru
INSERT INTO teachers (first_name, last_name, school, hire_date, salary)
    VALUES ('Samuel', 'Abbers', 'Standford University', '2006-01-30', 32000),
           ('Jessica', 'Abbers', 'Standford University', '2005-01-30', 33000),
           ('Tom', 'Massi', 'Harvard University', '1999-09-09', 39500),
           ('Esteban', 'Brown', 'MIT', '2007-01-30', 36000),
           ('Carlos', 'Alonso', 'Standford University', '2001-01-30', 44000);
SELECT * FROM teachers;

-- melihat semua data di tabel
SELECT * FROM teachers;

-- melihat isi kolom spesifik kepada tabel
SELECT first_name, last_name, school
FROM teachers;

-- melihat dosen yang mengajar di MIT
SELECT *
FROM teachers


-- melihat dosen yang gajinya diatas 60000
SELECT *
FROM teachers
WHERE salary>60000;

-- dosen MIT gaji diatas 60000
SELECT *
FROM teachers
WHERE school="MIT" and salary>60000;

-- dosen dengan nama belakang
-- cara #1
SELECT *
FROM teachers
WHERE last_name="abbers" or last_name="smith";

-- cara #2
SELECT *
FROM teachers
WHERE last_name in ("abbers", "smith");

-- melihat jumlah data di tabel teachers
SELECT count(*) AS "jumlah data"
FROM teachers;

-- melihat unique value di column school
SELECT DISTINCT school
From teachers;

-- melihat jumlah sekolah dengan unique value di colum schooldemo
SELECT COUNT(DISTINCT(school)) as "jumlah school"
FROM teachers;

-- mengurutkan dosen berdasarkan last_name secara Z-A (descending)
SELECT *
FROM teachers
order by last_name DESC;

-- mengurutkan dosen berdasarkan last_name secara A-Z (ascending)
SELECT *
FROM teachers
order by last_name ASC;

-- mengurutkan dosen berdasarkan last_name secara Z-A (descending) dan school A-Z (ascending)
SELECT *
FROM teachers
order by last_name DESC, school ASC;


