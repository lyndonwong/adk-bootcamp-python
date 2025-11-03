# O'Reilly AI Agent Workshop
Based on Google ADK (agent development kit)

https://google.github.io/adk-docs/

### This repository saves working code 
For [Workshop Module 1 Lab 2](https://github.com/inardini/oreilly-ai-agents-gcp/blob/main/module_1/labs/lab_2.md#3-method-2-programmatic-execution-with-runner
):

Required some modification of the run_programmatically.py instructional code to get this working. Used Gemini 2.5 Pro to help diagnose and converge on set of fixes.

### The bug:
The [tutorial](https://github.com/inardini/oreilly-ai-agents-gcp/blob/main/module_1/labs/lab_2.md#create-the-runner-script) tells us to create a runner script file inside of the my_first_agent directory:
> Inside your my_first_agent directory, create a new file named run_programmatically.py.

--> this causes the runner script to fail silently.

### The fix

But to get the runner script to work, needed to move this up a level, and edit some python code to recognize this arrangement of files:

> The adk command is smart about finding your agent, but a direct Python script is not. Your run_programmatically.py script should be in the project's root directory, outside of the my_first_agent package folder.

Verify your project structure looks like this:

![file directory structure](/runner-script-directory-diagram.png)

If your structure is correct, your import statement inside run_programmatically.py must correctly reference the package:

Python
> from my_first_agent.agent import root_agent

--> with the above changes, the runner script successfully runs the agent code.
