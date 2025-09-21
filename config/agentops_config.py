import os
from typing import List, Optional
import agentops

class AgentOpsConfig:
    """Configuration class for AgentOps integration"""
    
    def __init__(self):
        self.api_key = os.getenv("AGENTOPS_API_KEY")
        self.default_tags = [
            "crewai",
            "cyber-defense", 
            "deep-learning",
            "solana",
            "security-shield"
        ]
        self.trace_name = "CrewAI Cyber Defense Shield"
        self.auto_start_session = True
        
    def initialize_agentops(
        self, 
        tags: Optional[List[str]] = None,
        trace_name: Optional[str] = None,
        auto_start: bool = True
    ):
        """
        Initialize AgentOps with configuration
        
        Args:
            tags: Custom tags for this session
            trace_name: Custom trace name
            auto_start: Whether to auto-start session
        """
        
        if not self.api_key:
            print("⚠️  Warning: AGENTOPS_API_KEY not found in environment")
            print("Please set your AgentOps API key in .env file")
            return False
        
        session_tags = tags or self.default_tags
        session_trace_name = trace_name or self.trace_name
        
        try:
            agentops.init(
                api_key=self.api_key,
                tags=session_tags,
                trace_name=session_trace_name,
                auto_start_session=auto_start
            )
            
            print(f"✅ AgentOps initialized successfully")
            print(f"📊 Trace Name: {session_trace_name}")
            print(f"🏷️  Tags: {', '.join(session_tags)}")
            
            return True
            
        except Exception as e:
            print(f"❌ Failed to initialize AgentOps: {str(e)}")
            return False
    
    def start_custom_trace(self, name: str, tags: Optional[List[str]] = None):
        """Start a custom trace for specific workflows"""
        trace_tags = tags or self.default_tags
        return agentops.start_trace(name=name, tags=trace_tags)
    
    def end_trace_with_status(self, trace, success: bool, error_msg: Optional[str] = None):
        """End a trace with appropriate status"""
        if success:
            agentops.end_trace(trace, end_state="Success")
        else:
            print(f"⚠️  Trace failed: {error_msg}")
            agentops.end_trace(trace, end_state="Fail")
    
    def record_agent_action(self, action_name: str, parameters: dict, result: dict):
        """Record a custom agent action"""
        agentops.record(
            event_type="agent_action",
            action_name=action_name,
            parameters=parameters,
            result=result
        )
    
    def end_session_safely(self, success: bool = True):
        """Safely end the AgentOps session"""
        try:
            if success:
                agentops.end_session(end_state="Success")
                print("✅ AgentOps session ended successfully")
            else:
                agentops.end_session(end_state="Fail")
                print("⚠️  AgentOps session ended with failure")
        except Exception as e:
            print(f"⚠️  Warning: Could not end AgentOps session: {str(e)}")

# Global configuration instance
agentops_config = AgentOpsConfig()