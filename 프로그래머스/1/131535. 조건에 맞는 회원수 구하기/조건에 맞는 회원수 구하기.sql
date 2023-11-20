-- 코드를 입력하세요
SELECT count(*) as USERS
FROM USER_INFO
WHERE date_format(JOINED, '%Y') = "2021"
    AND AGE between 20 and 29;