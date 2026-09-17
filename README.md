# Python Hangman — Program Logic & UML Design

A Python-based Hangman implementation designed to demonstrate **program logic, control flow, input validation, and UML flowchart design**.

Rather than focusing on the game itself, this project demonstrates the process of breaking a programming problem into logical states, decisions, and execution paths before implementing the code.

## UML Flowchart

The following flowchart represents the program's logic from initialization through the win or loss conditions.

![Python Hangman Logic Flowchart](UML%20diagrams.jpeg)

## Logic Design

The program was designed by identifying the major states and decisions that control execution.

### 1. Initialization

The program begins by:

- Selecting the secret word
- Creating the collection used to track guessed letters
- Setting the number of attempts to `6`

This establishes the initial state of the program before user interaction begins.

### 2. Input Validation

The program then enters its primary interaction loop.

The player's input is evaluated to determine whether:

- The input is valid
- The letter has already been guessed

Invalid input does not advance the program state. Instead, the program displays a validation error and returns to the input stage.

This creates a validation loop within the larger program loop.

### 3. State Changes

Once valid input is received, the program determines whether the selected letter exists in the secret word.

A correct input follows this execution path:

```text
Input
  ↓
Letter exists?
  ↓ Yes
Reveal matching letters
  ↓
Update guessed letters
  ↓
Check completion
```

An incorrect input follows a different execution path:

```text
Input
  ↓
Letter exists?
  ↓ No
Add letter to guessed letters
  ↓
Decrement attempts
  ↓
Check remaining attempts
```

These paths demonstrate how a single input can cause different changes to the program's state.

### 4. Decision Points

The flowchart represents the primary decision points within the program:

- **Is the input valid and unseen?**
- **Is the letter contained in the secret word?**
- **Has the entire word been guessed?**
- **Are there any attempts remaining?**

Each decision produces a defined execution path.

### 5. Program Loops

The flowchart also demonstrates how the program returns to previous states.

For example:

```text
Display Current State
        ↓
    Get Input
        ↓
  Validate Input
        ↓
     Invalid?
      ↙    ↘
    Yes      No
     ↓        ↓
Display      Continue
 Error       Program
     ↓
 Get Input
```

After a valid guess, the program updates its state and returns to the display/input cycle unless a terminal condition has been reached.

This makes the control flow explicit before implementation.

## Design Approach

The program was modeled as a sequence of:

**States → Decisions → Actions → State Changes**

The UML flowchart provides a visual blueprint for how information moves through the program.

The design was then translated into Python control structures such as:

- `while` loops
- `if / elif / else` statements
- Input validation
- Variables representing program state
- Collections for tracking data
- Conditional termination

## Why UML?

Creating a flowchart before or alongside implementation helps identify potential problems in the program's logic, including:

- Missing conditions
- Infinite loops
- Unhandled input
- Incorrect state transitions
- Missing termination conditions
- Repeated or unnecessary logic

The UML diagram therefore serves as a **design blueprint**, rather than simply documenting the finished application.

## Software Engineering Concepts Demonstrated

This project demonstrates an understanding of:

- **Control Flow** — defining how execution moves through a program
- **Decision Logic** — modeling conditional execution paths
- **State Management** — tracking changes to program data
- **Input Validation** — preventing invalid data from advancing execution
- **Loop Design** — creating controlled repetition
- **Termination Conditions** — defining when execution should end
- **UML/Flowchart Design** — visually modeling program behavior before implementation

## Technologies

- Python
- UML / Flowchart Design
- Control Flow
- Input Validation
- State Management

## Project Structure

```text
python-hangman/
│
├── hangman.py
├── UML diagrams.jpeg
└── README.md
```

## Key Takeaway

This project demonstrates the ability to take a programming problem, **break it into logical states and decision points, model those relationships visually, and translate the resulting design into executable code.**
