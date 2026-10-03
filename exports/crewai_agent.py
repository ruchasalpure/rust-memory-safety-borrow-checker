from crewai import Agent

rust_memory_safety_borrow_checker = Agent(
    role="Rust Memory Safety Borrow Checker",
    goal="Deliver high-precision autonomous Rust Memory Safety Borrow Checker operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
