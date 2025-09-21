# CrewAI AgentOps Integration

This project demonstrates a smooth and seamless integration of AgentOps SDK with CrewAI for comprehensive cyber defense, deep learning security, and Solana blockchain protection.

## 🚀 Quick Start

### 1. Install Dependencies

```bash
python setup.py
```

Or manually:

```bash
pip install -r requirements.txt
```

### 2. Configure API Keys

Copy `.env.example` to `.env` and add your API keys:

```bash
cp .env.example .env
```

Edit `.env`:
```env
AGENTOPS_API_KEY=your_agentops_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Run the Cyber Defense Shield

```bash
python main.py
```

## 🏗️ Architecture

### AgentOps Integration Features

- **Automatic Session Management**: Sessions start/end automatically with proper error handling
- **Custom Trace Management**: Individual traces for different security analysis workflows
- **Decorator-Based Instrumentation**: Agents, operations, and tools are properly instrumented
- **Comprehensive Monitoring**: Full visibility into agent actions, tool usage, and execution flow

### Key Components

#### 1. Main Application (`main.py`)
- Entry point with AgentOps initialization
- CrewAI crew orchestration
- Integrated error handling and session management

#### 2. Agent Classes (`agents/cyber_defense_agents.py`)
- **ThreatIntelligenceAgent**: APT detection and threat analysis
- **DeepLearningSecurityAgent**: ML model security and adversarial defense
- **SolanaSecurityAgent**: Blockchain security and smart contract auditing
- **CyberDefenseOrchestrator**: Coordinates multi-agent analysis workflows

#### 3. Security Tools (`tools/security_tools.py`)
- **VulnerabilityScanner**: Automated vulnerability detection
- **ThreatIntelFeed**: Real-time threat intelligence
- **SecurityConfigAnalyzer**: Configuration compliance checking
- **SolanaSecurityAuditor**: Smart contract security auditing
- **MLModelSecurityChecker**: ML model adversarial robustness testing

#### 4. AgentOps Configuration (`config/agentops_config.py`)
- Centralized AgentOps configuration management
- Custom trace creation and management
- Session lifecycle management with error handling

## 🛡️ Security Focus Areas

### Cyber Defense
- Threat intelligence analysis
- Vulnerability assessment
- Security configuration auditing
- Incident response planning

### Deep Learning Security
- Adversarial attack detection and mitigation
- Model privacy protection
- Backdoor detection
- Robustness testing

### Solana Blockchain Security
- Smart contract auditing
- DeFi protocol security analysis
- Transaction security monitoring
- Consensus mechanism protection

## 📊 AgentOps Monitoring

### Automatic Tracking
- **Agent Actions**: All agent decisions and reasoning
- **Tool Usage**: Security tool executions and results  
- **Task Execution**: CrewAI task progression and outcomes
- **Error Handling**: Failed operations and recovery attempts

### Custom Traces
- **ThreatIntelligenceAnalysis**: Threat detection workflows
- **MLSecurityAnalysis**: Machine learning security assessments
- **SolanaSecurityAnalysis**: Blockchain security audits
- **CyberDefenseOrchestration**: Multi-agent coordination

### Session Management
```python
# Automatic session management
agentops_config.initialize_agentops(
    tags=["custom", "deployment"],
    trace_name="Production Security Scan"
)

# Manual trace control
trace = agentops_config.start_custom_trace("CustomWorkflow")
# ... perform operations ...
agentops_config.end_trace_with_status(trace, success=True)
```

## 🔧 Advanced Configuration

### Custom Agent Instrumentation

```python
from agentops.sdk.decorators import agent, operation

@agent(name="CustomSecurityAgent")
class CustomSecurityAgent:
    @operation
    def analyze_threat(self, threat_data):
        # Custom security analysis
        return analysis_results
```

### Custom Tool Creation

```python
from agentops.sdk.decorators import tool

@tool(name="CustomSecurityTool", cost=0.02)
def custom_security_tool(target: str) -> dict:
    # Custom security tool implementation
    return security_results
```

### Workflow Orchestration

```python
# Coordinate multiple agents with AgentOps tracking
orchestrator = CyberDefenseOrchestrator()
results = orchestrator.coordinate_defense_analysis("target_system")
```

## 📈 Monitoring Dashboard

Access your AgentOps dashboard at [https://app.agentops.ai](https://app.agentops.ai) to view:

- Real-time agent execution metrics
- Security analysis results and trends
- Tool usage statistics and costs
- Error rates and performance analytics
- Custom trace visualizations

## 🚨 Security Best Practices

1. **API Key Security**: Store API keys in environment variables, never in code
2. **Trace Naming**: Use descriptive trace names for better monitoring
3. **Error Handling**: Always implement proper error handling with AgentOps tracking
4. **Session Management**: Ensure sessions are properly closed to avoid resource leaks
5. **Cost Monitoring**: Monitor tool usage costs through AgentOps dashboard

## 🔍 Troubleshooting

### AgentOps Connection Issues
```bash
# Verify API key
echo $AGENTOPS_API_KEY

# Test connection
python -c "import agentops; agentops.init('your_key_here')"
```

### Missing Dependencies
```bash
pip install --upgrade crewai agentops openai python-dotenv
```

### Agent Execution Errors
Check the AgentOps dashboard for detailed execution logs and error traces.

## 📚 Documentation Links

- [AgentOps Documentation](https://docs.agentops.ai/)
- [CrewAI Documentation](https://docs.crewai.com/)
- [Solana Security Best Practices](https://docs.solana.com/developing/on-chain-programs/developing-rust#security)

## 🤝 Contributing

This integration demonstrates enterprise-grade AgentOps implementation for security applications. Contributions and improvements are welcome!

---

**🛡️ Cyber Defense Shield - Powered by CrewAI & AgentOps**