# kw_assignment

 Odoo employee wise subject wise mark database app

### Master :
* College master
* Stream Master (Btech/Mtech/MCA)
* Semester master
* Subject master

### Use case :
* College have multiple streams
* Each stream have multiple semester (Validation: Btech = 8, Mtech = 4, MCA = 6)
* Each semester has multiple subjects
* Employees are tagged with college, stream
* Each employee will add and update their subject wise mark out of 100
* If an employee skip particular subject then it will be treated as 0
* HR users will validate the entry
* After validation employee will not further modify (Make Fields Read Only)

### Output :
* HR user will view the subject wise highest mark and name of employees
* College wise student count and no of student with mark more than 90%
* Subject wise average mark
* Pivot report based on master data

### Note :
* Inherit the employee module
* HR user may be multiple