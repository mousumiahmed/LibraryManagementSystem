Library Management System:

Project Requirements :

	Create a Python program that allows users to:
	Add, remove, and search for books in a library database
	Check out and return books
	View book details (title, author, publication date, etc.)
	Use a database like MySQL or PostgreSQL to store book information
	Implement user authentication and authorization to restrict access to certain 	features


Requirement Analysis:

    Authentication and Authorization -
        -Registration(New User) ,Login(Existing User)
    	-Admin :read, write, delete permission
    	-User  :read ,checkout ,return permission
        -Admin verifications
        -Forgot Password
    
    Targeted User -
    	-Admin : librarians, administrators
    	-User  :student ,faculty
    
    Functional Requirements: 
        -User registration and authentication
        -Book cataloging (adding, updating, deleting books)
        -Searching for books
        -Borrowing and returning books
        -verification and Validation user and book data
        -Late return penalty fees collection through barcode
    
    Non-functional Requirements: Identify performance, usability, and security requirements.
        - Inputing User Data
        - Inputing Book Details
        - Keeping different accessibility between common and admin user
        - supporting to manage all user and book data efficiently





Proof Of Concept (POC):

    1.Objectives:
        To achive a library management System where we can manage users, store books , checkout, return and search book . 
    
        Purpose: To build a library management System within estimated time and cost which work effectively for member management, monitoring, storing, and circulation of books.
        Scope: We can use to manage and monitoring any new / existing organization's library


    2. Design the POC
    Architecture:
        Data Flow and Design : go with flowchart and project flow
    
    3. Develop the POC-
        Set Up Environment & Tools: PyCharm,setup env and requirement.txt file
    
        Technology Stack : python,mysql
    
        Implement Core Features: Functionalities identified in the requirements phase:
            User Management: User registration, login.
            Book Cataloging: Adding, updating, and deleting books in the catalog.
            Search Functionality: Implement a search feature to find books based on title.
            Borrowing/Returning Books: Users can borrow and return books, and as per user action book catalog will update accordingly.


    4.Test the POC
            Unit Testing : Check with Unit Test Cases using unittest/ doctest/PyTest
    
            Integration Testing: verify that different modules work together seamlessly or not .Evaluation 	 of compilence of a module with its functional requirements.
            
            User Acceptance Testing (UAT): End User testing - evaluating UI as user friendly and functionality working as expected.
       
            Performance Testing: Load Testing is not implemented yet


    5.Evaluate the POC- Review and Feedback
            Gather Feedback: Collect feedback from stakeholders and users. Identify any issues or areas for improvement.
       
            Technical Challenges: Document any technical challenges encountered and how they were addressed.
       
            Assess Feasibility: Evaluate whether the demonstrated functionality meets the project’s goals and if any adjustments are needed.
       
            Demo: Demonstration for end users.
     
    6.Documentation
            User Guide : Go to project flow design and different user modules
            
            Documentation: Includes Project design/architecture, implementation details,reference and developments steps.


