# Fraction ETL
### Requirements:
- Docker
- Docker Compose

### Usage:
1- Run
```
docker-compose up --build
```
2- Wait until the ETL service posts a message to the terminal "`ETL is done!`".  
  
3- Connect the the db container and run:
```
psql -d postgres -U user
```
  
4- Run the following queries:-

a- Query `user` table:
```
SELECT * FROM "user" LIMIT 5;

/* OUTPUT
      name      |          email          |    phone     | unit |        street        |      city      | state | country | postal |                  id                  
----------------+-------------------------+--------------+------+----------------------+----------------+-------+---------+--------+--------------------------------------
 Elsy Hurd      | elsyhurd@gmail.com      | 751-704-6749 |      | 93 Harvey St         |  Framingham    | MA    |  US     |  01701 | 35ad91bc-4eb8-4d06-b6dd-29262867b738
 Blaire Condon  | blairecondon@gmail.com  | 118-721-2913 | 845  | 910 Linda St         |  Rock Hill     | SC    |  US     |  29730 | ad1921c8-5587-438f-86ea-4817c76befed
 Morgan Hansen  | morganhansen@gmail.com  | 121-866-3016 | 754  | 945 Lakewood Ave     |  Central Islip | NY    |  US     |  11722 | d6c59e47-6e00-4226-9164-122c61e909fb
 Emmey Kirwin   | emmeykirwin@gmail.com   | 732-918-9919 |      | 266 Sherwood Circle  |  Potomac       | MD    |  US     |  20854 | ccd8b572-34bc-43c6-9061-ceb405248cec
 Kellen Millman | kellenmillman@gmail.com | 725-811-5736 | 592  | 600 East Kirkland St |  Duarte        | CA    |  US     |  91010 | 9a119103-c634-4773-b426-f7c69b583395
*/
```

b- Query `property` table:
```
SELECT * FROM property LIMIT 5;

/* OUTPUT
                  id                  | unit  |        street        |     city      | state | postal | country | property_value | existing_mortgage 
--------------------------------------+-------+----------------------+---------------+-------+--------+---------+----------------+-------------------
 113782c1-1816-4045-9363-22f07b30c4b2 |       | 93 Harvey St         | Framingham    | MA    | 1701   | US      |       25038517 |          22446604
 34a8d19f-030d-4415-91a2-2d1304f36a0e | 845.0 | 910 Linda St         | Rock Hill     | SC    | 29730  | US      |      168964115 |         135760868
 6ea41ee3-8f37-4ae4-80db-81829a0d9928 | 754.0 | 945 Lakewood Ave     | Central Islip | NY    | 11722  | US      |      105608025 |          53744956
 e7770291-79ee-491a-80ed-16383751ecf0 |       | 266 Sherwood Circle  | Potomac       | MD    | 20854  | US      |      164673346 |          52039488
 9f00609c-be39-4a27-b07b-b3d42619a083 | 592.0 | 600 East Kirkland St | Duarte        | CA    | 91010  | US      |      186005298 |         140030873
*/
```
c- Query `event` table:
```
SELECT * FROM event LIMIT 5;

/* OUTPUT
      timestamp      |            email             |   type   |     message      
---------------------+------------------------------+----------+------------------
 2021-12-19 12:00:20 | leanorbartholomeus@gmail.com | applied  | User applied
 2021-12-19 12:00:46 | leanorbartholomeus@gmail.com | info     | sint aute
 2021-12-19 12:01:11 | leanorbartholomeus@gmail.com | rejected | User rejected
 2021-12-19 12:01:20 | leanorbartholomeus@gmail.com | debug    | ea
 2021-12-19 12:01:49 | leanorbartholomeus@gmail.com | debug    | est velit aliqua
*/
```
d- Query `metrics` view:
```
SELECT * FROM metrics;

/*                   metric                   |  date   | count 
--------------------------------------------+---------+-------
 Total Users Applied                        | 2021-10 |  5888
 Total Users Applied                        | 2021-11 |  5540
 Total Users Applied                        | 2021-12 |  6844
 Total Users Applied                        | 2022-01 |  1880
 Total Users Rejected                       | 2021-10 |  3484
 Total Users Rejected                       | 2021-11 |  3076
 Total Users Rejected                       | 2021-12 |  3944
 Total Users Rejected                       | 2022-01 |  1076
 Total Users Paid off 50% of their mortgage |         |  3296 OUTPUT

*/
```