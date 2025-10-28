# DEMO.py

class LibraryManagementSystem:
    def __init__(self):
        print("Library Management System initialized")

    def start_demo(self):
        print("Demo is now running...")
        print("You can add books, borrow books, return books, etc.")
        print("Demo complete!")


def run_demo():
    # ❌ WRONG: library = ("LibraryManagementSystem")()
    # ✅ CORRECT:
    library = LibraryManagementSystem()
    library.start_demo()


if __name__ == "__main__":
    print("============================================================")
    print("LIBRARY MANAGEMENT SYSTEM - DEMO")
    print("============================================================")
    run_demo()
