# Architecture

Threat Intelligence Orchestration Platform with AI-assisted analysis.

```txt
                   +----------------------+
                   |      Dashboard       |
                   | FastAPI + Chart.js   |
                   +----------+-----------+
                              |
                              v

                     +----------------+
                     |  API Gateway   |
                     |   FastAPI      |
                     +--------+-------+
                              |
                              v

                   +----------------------+
                   |  Orchestrator Agent  |
                   | Investigation Brain  |
                   +----------+-----------+
                              |
          ---------------------------------------------------
          |            |            |           |           |
          v            v            v           v           v

   IOC Analyzer   Intel Collector  Correlator  Risk Engine  LLM Agent

          |            |            |           |           |
          ---------------------------------------------------
                              |
                              v

                   +----------------------+
                   |  MITRE Mapper Agent  |
                   +----------+-----------+
                              |
                              v

                   +----------------------+
                   | Reporting Engine     |
                   | CLI / JSON / PDF     |
                   +----------+-----------+
                              |
                              v

                     +------------------+
                     | Threat DB        |
                     | IOC Memory       |
                     | PostgreSQL       |
                     +------------------+


```

## Output Example

Verision 01

![Verson 01](/img/threatAgentV03.png)
