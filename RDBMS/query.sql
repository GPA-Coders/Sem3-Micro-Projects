BEGIN
    CREATE TABLE Faculty
    (
        f_id NUMBER(2) PRIMARY KEY,
        f_name CHAR(15) NOT NULL,
        f_dept CHAR(10),
        f_desg CHAR(10)
    );

END;
/