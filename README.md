# 🛡️ AI Threat Hunter – Autonomous Threat Intelligence Agent

## 📌 Overview

AI Threat Hunter is an autonomous cybersecurity analysis platform designed to function as a SOC (Security Operations Center) analyst in code.

The system automatically investigates IPs, domains, and URLs, correlates data from multiple threat intelligence sources, and uses a local LLM (Llama-based) to generate contextual security analysis, risk scoring, and threat hypotheses.

---

## 🎯 Project Vision

The goal of this project is to build a self-operating Threat Intelligence Agent capable of:

- Automating repetitive SOC analysis tasks
- Reducing analyst workload
- Providing contextual, human-like security insights
- Scaling investigations across multiple data sources
- Acting as a foundation for future AI-driven threat hunting systems

In a real-world environment, this tool can be used as:

- 🔍 Tier 1 / Tier 2 SOC assistant
- 🧠 Threat intelligence enrichment engine
- ⚡ Incident triage accelerator
- 📊 IOC investigation platform

---

## 🧠 Core Capabilities

### 1. Target Analysis

The agent accepts:

- IP addresses
- Domain names
- URLs

Example:

`python threat_agent.py 8.8.8.8`

---

## 2. Multi-Source Threat Intelligence

The system integrates multiple intelligence providers:

🔹 VirusTotal

- Malware detections
- Reputation analysis
- Community verdicts

🔹 AbuseIPDB

- Historical abuse reports
- Confidence score
- Report categories

🔹 Shodan

- Open ports and services
- Banners and exposed technologies
- Infrastructure fingerprinting

🔹 GreyNoise

- Internet scanning classification
- Benign vs malicious behavior
- Noise vs targeted activity

---

## 3. Correlation Engine

The system analyzes collected data to detect patterns such as:

- Multiple detections across sources
- Suspicious service exposure
- Abuse history + scanning behavior

This transforms raw data into **actionable intelligence**.

## 4. IOC Discovery Engine

The agent automatically extracts new indicators:

- Domains from Shodan hostnames
- Related infrastructure

This enables:

`IP → Domain → Additional context`

---

## 5. Recursive Investigation Engine

The system can automatically investigate discovered IOCs.

Example:

`Initial IP → Hostnames → New lookup → Expanded intelligence`

Features:

- Depth control (prevents infinite loops)
- Duplicate avoidance
- Safe validation of targets

---

## 6. Risk Scoring Engine

The agent calculates a risk level:

- LOW
- MEDIUM
- HIGH
- CRITICAL

Based on:

- Number of detections
- Abuse history
- Exposure of services
- Behavioral classification

---

## 🤖 LLM-Powered Threat Analysis

The system integrates a local **LLM (Llama-based)** to act as a **cybersecurity analyst**.

🔹 Supported Models

- Llama 3
- Mistral
- Mixtral
- CodeLlama

Recommended runtime:

- Ollama
- LocalAI
- llama.cpp

---

## 🔹 What the LLM does

The model receives:

- Threat intelligence data
- Correlation results
- Risk score
- Recursive investigation data

And generates:

| Action | description |
|----------|----------|
| Executive Summary|Clear explanation of the target|
| Threat Assessment|Is it malicious, suspicious, or benign?|
| Key Findings|Important signals from the data|
| Hypotheses|Possible attacker behavior: Scanning activity, Phishing infrastructure or Command & Control|
| MITRE ATT&CK Mapping|Potential techniques used|
| Risk Justification|Why the score was assigned|
| Recommendations|What actions should be taken|

---

## 🧠 Why LLM?

Traditional tools show raw data.

This system:

`Data → Context → Intelligence → Decision`

The LLM acts as a **human** analyst layer.

---

## ⚙️ Architecture

```txt
Input Target
    ↓
Validation
    ↓
Threat Intelligence APIs
    ↓
Correlation Engine
    ↓
IOC Discovery
    ↓
Recursive Investigation
    ↓
Risk Scoring
    ↓
LLM Analysis
    ↓
Report Output
```

---

## 🔐 Security Considerations

- API keys stored in environment variables
- Input validation for all targets
- Controlled recursion depth
- Error handling for external APIs
- Rate limit awareness

---

## 🔮 Future Improvements

- Database persistence (IOC history)
- Web dashboard
- MITRE ATT&CK live mapping
- Advanced risk scoring
- Multi-agent orchestration

---

### ⚠️ Disclaimer

This tool is intended for educational and defensive cybersecurity purposes only.
