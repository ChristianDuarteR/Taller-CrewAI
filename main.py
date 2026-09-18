from crew import aurora_triage_crew
from tickets import TEST_TICKETS


def main() -> None:
    print("=== INICIANDO TRIAGE AUTOMATIZADO CON CREWAI ===\n")

    for test in TEST_TICKETS:
        print("=" * 60)
        print(f"PROCESANDO TICKET {test['id']}: {test['text']}")
        print("=" * 60)

        result = aurora_triage_crew.kickoff(inputs={"ticket_text": test["text"]})

        print(f"\n--- RESULTADO OBTENIDO PARA {test['id']} ---")
        print(result.raw)


if __name__ == "__main__":
    main()