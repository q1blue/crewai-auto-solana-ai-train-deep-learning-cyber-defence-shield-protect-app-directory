#!/usr/bin/env python3

import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from config.agentops_config import agentops_config
from agents.cyber_defense_agents import CyberDefenseOrchestrator
from tools.security_tools import (
    vulnerability_scanner,
    threat_intelligence_feed,
    security_config_analyzer,
    solana_security_auditor,
    ml_model_security_checker
)

load_dotenv()

if not agentops_config.initialize_agentops():
    print("⚠️  Continuing without AgentOps tracking...")
    AGENTOPS_ENABLED = False
else:
    AGENTOPS_ENABLED = True

def create_cyber_defense_agents():
    threat_analyst = Agent(
        role='Threat Intelligence Analyst',
        goal='Analyze and identify potential cyber threats and vulnerabilities',
        backstory="""You are an expert cybersecurity analyst with deep knowledge of 
        threat intelligence, malware analysis, and attack patterns. You specialize in 
        identifying and categorizing security threats.""",
        verbose=True,
        allow_delegation=False,
        tools=[vulnerability_scanner, threat_intelligence_feed]
    )
    
    security_engineer = Agent(
        role='Security Systems Engineer',
        goal='Design and implement defensive security measures',
        backstory="""You are a seasoned security engineer with expertise in building 
        robust defense systems, implementing security protocols, and hardening systems 
        against cyber attacks.""",
        verbose=True,
        allow_delegation=False,
        tools=[security_config_analyzer, ml_model_security_checker]
    )
    
    blockchain_security_specialist = Agent(
        role='Blockchain Security Specialist',
        goal='Secure Solana blockchain applications and smart contracts',
        backstory="""You are a blockchain security expert specializing in Solana 
        ecosystem security, smart contract auditing, and DeFi protocol protection.""",
        verbose=True,
        allow_delegation=False,
        tools=[solana_security_auditor, vulnerability_scanner]
    )
    
    return threat_analyst, security_engineer, blockchain_security_specialist

def create_defense_tasks(threat_analyst, security_engineer, blockchain_security_specialist):
    threat_analysis_task = Task(
        description="""Analyze current threat landscape for blockchain applications,
        focusing on Solana ecosystem vulnerabilities, common attack vectors,
        and emerging security threats. Provide a comprehensive threat assessment.""",
        agent=threat_analyst,
        expected_output="Detailed threat analysis report with identified vulnerabilities and risk levels"
    )
    
    security_implementation_task = Task(
        description="""Design and recommend security implementation strategies
        based on the threat analysis. Focus on defensive measures, monitoring
        systems, and incident response procedures.""",
        agent=security_engineer,
        expected_output="Security implementation plan with specific defensive measures and protocols"
    )
    
    blockchain_audit_task = Task(
        description="""Conduct security audit of Solana blockchain integration,
        review smart contract security patterns, and recommend blockchain-specific
        security measures for the application.""",
        agent=blockchain_security_specialist,
        expected_output="Blockchain security audit report with recommendations for Solana integration"
    )
    
    return [threat_analysis_task, security_implementation_task, blockchain_audit_task]

def run_cyber_defense_crew():
    orchestrator = CyberDefenseOrchestrator()
    
    try:
        threat_analyst, security_engineer, blockchain_security_specialist = create_cyber_defense_agents()
        
        tasks = create_defense_tasks(threat_analyst, security_engineer, blockchain_security_specialist)
        
        crew = Crew(
            agents=[threat_analyst, security_engineer, blockchain_security_specialist],
            tasks=tasks,
            process=Process.sequential,
            verbose=2
        )
        
        print("🛡️ Starting Cyber Defense Shield Analysis...")
        
        # Use orchestrator for coordinated analysis if AgentOps is enabled
        if AGENTOPS_ENABLED:
            orchestration_results = orchestrator.coordinate_defense_analysis("blockchain_ai_system")
            print("🤖 Orchestrated Agent Analysis:")
            for key, value in orchestration_results.items():
                print(f"   {key}: {value}")
        
        result = crew.kickoff()
        
        print("\n" + "="*50)
        print("🎯 CYBER DEFENSE ANALYSIS COMPLETE")
        print("="*50)
        print(result)
        
        return result
        
    except Exception as e:
        print(f"❌ Error running cyber defense crew: {str(e)}")
        if AGENTOPS_ENABLED:
            agentops_config.end_session_safely(success=False)
        raise
    finally:
        if AGENTOPS_ENABLED:
            agentops_config.end_session_safely(success=True)

if __name__ == "__main__":
    if not os.getenv("AGENTOPS_API_KEY"):
        print("⚠️  Warning: AGENTOPS_API_KEY not found in environment variables")
        print("Please set your AgentOps API key in .env file")
    
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  Warning: OPENAI_API_KEY not found in environment variables")
        print("Please set your OpenAI API key in .env file")
    
    run_cyber_defense_crew()