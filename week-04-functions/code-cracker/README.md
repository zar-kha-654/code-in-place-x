# 💗 Week 04 — Functions: Code Cracker

> Stanford Code in Place X | Fall 2026  
> Learning Python through functions, parameters, return values, and problem-solving.

## 📌 About This Project

**Code Cracker** is the fourth-week assignment in Code in Place X. The challenge involves building a Caesar cipher decoder that can decrypt coded messages by trying different letter shifts.

Instead of being given the correct shift, the program tests all 25 possible shifts and prints the decoded results.

## 🎯 Main Assignment — Crack It

The program:

1. Prints a welcome message.
2. Asks the user to enter an encrypted message.
3. Calls `crack(message)` to test all possible shifts.
4. Uses `decode(message, shift)` to decode the message.
5. Prints all 25 possible decoded messages.

### Example

**Input:**
```text
Welcome to the Code Machine!
Enter a message: wkh wuhdvxuh lv xqghu wkh ehg
```

**Output (selected lines):**
```text
Shift 1: vjg vtgcuwtg ku wpfgt vjg dgf
Shift 2: uif usfbtvsf jt voefs uif cfe
Shift 3: the treasure is under the bed
```

## 📂 Project Structure

```text
code-cracker/
│
├── README.md
├── solution.py
│
└── twists/
    ├── missing-parameter.py
    ├── known-word.py
    ├── where-did-it-go.py
    ├── key-letter.py
    ├── mixed-up-arguments.py
    ├── double-lock.py
    ├── mirror-alphabet.py
    └── spy-briefing.py
```

## 🧩 Twists

Additional challenges that explore different ways to work with functions and decoding:

| # | Challenge | File |
|---|---|---|
| 01 | Missing Parameter | `missing-parameter.py` |
| 02 | Known Word | `known-word.py` |
| 03 | Where Did It Go? | `where-did-it-go.py` |
| 04 | Key Letter | `key-letter.py` |
| 05 | Mixed Up Arguments | `mixed-up-arguments.py` |
| 06 | Double Lock | `double-lock.py` |
| 07 | Mirror Alphabet | `mirror-alphabet.py` |
| 08 | Spy Briefing | `spy-briefing.py` |

## 🧠 Concepts Practiced

- Defining and calling functions
- Function parameters and arguments
- Return values
- Loops (`for` and `range()`)
- String manipulation
- Working with indexes
- Modulo operator (`%`)
- Caesar cipher and letter shifting
- Breaking down problems into smaller functions

## 🛠️ Technologies

- **Language:** Python
- **Platform:** Stanford Code in Place X
- **Editor:** Code in Place IDE

---

*One shift at a time, one challenge at a time. 💗*

**Part of my Stanford Code in Place X learning journey.**
