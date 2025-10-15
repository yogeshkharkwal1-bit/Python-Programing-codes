# Copilot Instructions for AI Coding Agents

## Overview
This workspace contains a collection of Python scripts organized by chapter and topic, primarily for educational and practice purposes. There is no monolithic application or framework; instead, the codebase is structured into folders representing chapters, practice sets, and individual problems.

## Architecture & Structure
- **Modular Organization:**
  - Each folder (e.g., `chap 1`, `chep 2 practice question`, `chep 4`) contains Python files for specific topics or exercises.
  - No central entry point; most files are standalone scripts.
- **Naming Conventions:**
  - Folders and files are named by chapter, topic, or problem number (e.g., `qu1.py`, `problem1.py`).
  - Practice sets and exercises are grouped by chapter for easy navigation.
- **Key Directories:**
  - `chap 1/`, `chep 2 practice question/`, `chep 3 practice/`, `chep 4/`, `chep 6,conditional statement/`, `chep 7 loops/`, `chep7 practice set/` — each contains relevant scripts for the chapter/topic.

## Developer Workflows
- **Running Code:**
  - Execute individual Python scripts directly (e.g., `python chap 1/module.py`).
  - No build system or test framework detected; scripts are intended for direct execution and experimentation.
- **Debugging:**
  - Debug scripts individually using VS Code's Python debugger or print statements.
- **Dependencies:**
  - No external dependencies or requirements files detected; all scripts use standard Python libraries.

## Project-Specific Patterns
- **Educational Focus:**
  - Scripts are designed for learning and practice, often containing simple functions, input/output operations, and basic data structures.
  - Example: `chep 4/list.py` demonstrates list operations; `chep 6,conditional statement/operators.py` covers conditional logic.
- **No Cross-Component Communication:**
  - Scripts do not import from each other; each file is self-contained.
- **No Advanced Patterns:**
  - No use of classes, modules, or package-level organization beyond basic file grouping.

## How to Contribute
- Add new scripts to the relevant chapter or topic folder.
- Follow existing naming conventions for files and folders.
- Keep scripts self-contained and focused on a single concept or exercise.

## Example Workflow
```powershell
# Run a script from a chapter folder
python "chep 4/list.py"
```

## Key Files & Directories
- `chap 1/first.py`, `chap 1/module.py` — examples of chapter-based scripts
- `chep 4/list.py`, `chep 4/tuple.py` — data structure practice
- `chep 6,conditional statement/operators.py` — conditional logic examples

---
For questions or unclear conventions, ask for clarification or review the structure of similar files in the relevant folder.
