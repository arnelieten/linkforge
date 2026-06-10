# The decisisons made and the reasons behind them

## telegram vs whatsapp
telegram integration is just way less administrative work so easier to setup for hobby project

## database choice
sqlite since only 1 user will be using it and sqlitesession works well with the agents

Sqlitesession uses some tables, created 1 table for state, created 1 table for approved drafts

## .commands
chose . instead of / commands just because it is easier on mobile to type a dot then to type a slash on my keyboard.

Also the . commands are more administrative functions and do not need to be integrationed or kept in the chat memory. No injection in the sqlitesession or need for a custom session management solution.

## agent & tools
wanted natural language intereaction with the linkedin post generator therefore agent to route to the right tools. Subagents seemed overkill in this situation, and tools are more deterministic.

## genai gateway
relying on litellm to switch between models easily. Google has free tier on some models which is nice to use for the interaction with the chat_agent and power the research_agent. However for real writing Antropic models are better and those will be injected in the function tools for the chat_agent
