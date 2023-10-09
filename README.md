#### **Project Name**: Simple Task Manager (STM)

#### **Objective**: 
Develop a terminal-based task management application in Python, focusing on utilizing object-oriented programming (OOP) concepts such as classes and objects, encapsulation, and inheritance.

---

### **1. Overview**

**1.1 Description**

STM is a terminal-based task management application where a user can create, delete, view, and manage tasks. Tasks can be viewed/sorted based on their due date, state (done/open), or priority.

**1.2 Goals**

- Provide a simple, user-friendly interface for task management in the terminal.
- Enable task creation, deletion, and status updates (done/open).
- Allow task viewing sorted by various attributes (due time, state, priority).

---

### **2. Functional Requirements**

**2.1 Task Management**

- **2.1.1 Create Task**
  - Users should be able to create a new task, specifying the task name, due date, and priority.

- **2.1.2 Delete Task**
  - Users should be able to delete a task by specifying its ID or name.

- **2.1.3 Update Task**
  - Users should be able to mark a task as "done" or revert it to "open".

- **2.1.4 View Tasks**
  - Users should be able to view tasks, optionally sorted by due time, state, or priority.

**2.2 User Interface**

- **2.2.1 Task Input**
  - The system should allow users to input task attributes: name, due date, and priority via the terminal.

- **2.2.2 Task Display**
  - The system should display tasks in a readable format in the terminal.

---

### **3. Non-Functional Requirements**

**3.1 Usability**

- The application should have clear instructions and prompts to ensure that the user can easily navigate and perform task management operations.

**3.2 Performance**

- The application should be able to handle up to 100 tasks without significant delay in user interactions.

**3.3 Extensibility**

- Code should be structured in a way that allows future addition of features (like user profiles, notifications, etc.) without major rework.

---

### **4. Technical Requirements**

**4.1 Technology Stack**

- **Programming Language**: Python
- **Libraries**: (if any, such as datetime for handling date and time)

---

### **5. OOP Implementation Guidelines**

**5.1 Class Definitions**

- **Task Class**: Should contain attributes (task name, due date, priority, and state) and methods relevant for a single task’s lifecycle (e.g., mark as done).
  
- **TaskManager Class**: Should contain methods and attributes for managing multiple tasks (e.g., add task, delete task, view tasks).

**5.2 Encapsulation**

- Ensure that data (task attributes) are hidden and can only be modified using defined methods (e.g., mark a task as done).

**5.3 Inheritance**

- While not strictly necessary for a simple app, consider a base class and derived classes if additional task types (e.g., timed tasks, multi-part tasks) may be added in the future.

**5.4 Method Definitions**

- Define methods for adding, deleting, updating, and viewing tasks within the appropriate class(es).

---

### **6. Milestones**

**M1:** Core Classes Definition and Method Stubs (Task, TaskManager)

**M2:** Implementation of Task Creation, Deletion, and Viewing Functionality

**M3:** Implementation of Task Updating and Viewing Sorting Options

**M4:** User Interface and Interaction Handling in Terminal

**M5:** Testing and Debugging

**M6:** Documentation and Submission

---

### **7. Deliverables**

- Source code, including classes and methods implementing the described functionality.
- A user guide describing how to use the application.
- (Optional) Test cases and results.
- (Optional) Documentation of the code (can use tools like Doxygen).

### **8. Assessment Criteria**

- Correctness and completeness of the implementation.
- Proper use of OOP concepts.
- Code clarity and documentation.
- User interface simplicity and ease of use.

---

### Note to Students
Ensure to follow the principles of OOP and keep the code modular and well-documented. Focus on ensuring the application is bug-free and user-friendly. Always test thoroughly and try to think like a user while testing. Good luck!
