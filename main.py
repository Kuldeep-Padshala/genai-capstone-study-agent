from memory.session_service import InMemorySessionService
from agents.coordinator import StudyCoordinator

def main():
    print("=== Smart AI Study Assistant (CLI Demo) ===")

    session_service = InMemorySessionService()
    coordinator = StudyCoordinator(session_service)

    sid = coordinator.create_or_get_session("cli_user")
    topics = [
        "Day 1 — Foundations of AI Agents",
        "Day 2 — Tools & Integrations",
        "Day 3 — Planning & Orchestration",
        "Day 4 — Budgeting & Optimization",
        "Day 5 — Deployment & Observability",
    ]

    plan = coordinator.plan_for(sid, topics)

    print("\n--- Summary ---")
    for t in topics:
        print(f"\n📘 {t}")
        print(f"Resources: {len(plan['resources'][t])}")
        print(f"Flashcards: {len(plan['flashcards'][t])}")
        print(f"Quiz Questions: {len(plan['quizzes'][t])}")

if __name__ == "__main__":
    main()
