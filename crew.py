from crewai import Crew, Process

from agent import triage_agent
from task import triage_task


aurora_triage_crew = Crew(
    agents=[triage_agent],
    tasks=[triage_task],
    process=Process.sequential,
    verbose=True,
)