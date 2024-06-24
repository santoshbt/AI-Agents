from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from task import research, write


crew = Crew(
  agents=[blog_researcher, blog_writer],
  tasks=[research, write],
  process=Process.sequential,  # Optional: Sequential task execution is default
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True
)

result=crew.kickoff(inputs={'topic':'Realtime Multimodal RAG Usecase Part 3 | MultiVectorRetriever with Langchain | RAG Application'})
print(result)
