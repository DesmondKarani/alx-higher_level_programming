### JavaScript Warm Up

#### Project Overview

This project is an introduction to JavaScript, focusing on its basic concepts and applications in both scripting and web front-end development. The goal is to lay a foundation for further exploration into JavaScript, culminating in making our AirBnB clone project dynamic using JavaScript and JQuery.

#### Learning Objectives

By the end of this project, learners will be able to:

- Understand why JavaScript programming is essential for web development.
- Run JavaScript scripts effectively.
- Create variables and constants using `var`, `let`, and `const`, and explain their differences.
- Identify and use all JavaScript data types.
- Implement control flow with `if`, `if...else` statements, and loops (`while`, `for`).
- Understand the use and functionality of `break` and `continue` statements.
- Define and invoke functions, and comprehend the implications of functions without a `return` statement.
- Grasp the concept of variable scope.
- Utilize arithmetic operators for various operations.
- Manipulate objects (referred to as dictionaries in some languages) and arrays.
- Import files within a JavaScript project.

#### Requirements

- Development environment: All scripts should be tested on Ubuntu 20.04 LTS using Node.js version 14.x.
- Coding style: Code must follow the semistandard style (version 16.x.x), incorporating rules from Standard with semicolons, and adhere to AirBnB style guidelines.
- All files must end with a newline, and the first line should be `#!/usr/bin/node` to ensure they are executable with Node.js.
- A `README.md` file is required at the root of the project directory.

#### Setup Instructions

1. **Install Node.js version 14:**

   ```bash
   curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
   sudo apt-get install -y nodejs
   ```

2. **Install Semistandard for linting:**

   ```bash
   sudo npm install semistandard --global
   ```

#### Quiz Answers Overview

1. JavaScript does not have a native "Dictionary" data type; objects serve a similar purpose.
2. `let` is used to define a variable that is block-scoped, can be reassigned, and does not define a global variable.
3. JavaScript recognizes "String" as a native data type.
4. `const` is used to define a constant variable that cannot be reassigned and is block-scoped.
5. JavaScript has "Array" as a native data type.
6. JavaScript also does not have "Set" as a native data type.
