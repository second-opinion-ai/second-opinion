from graphviz import Digraph

dot = Digraph(comment='AI-driven Car Repair Assistant Architecture')

# Setting graph direction (left to right)
dot.attr(rankdir='LR')

# Defining nodes with specific shapes for different components
dot.node('A', 'User Interface\n(Web Form)', shape='rectangle')
dot.node('B', 'Form Submission & Context Retrieval\n(form_routes -> util.py)', shape='component')
dot.node('C', 'ChatGPT Service\n(chat_gpt_service.py)', shape='cylinder')
dot.node('D', 'OpenAI API\n(GPT-3.5-turbo)', shape='cloud')

# Adding edges to represent the flow and interactions with descriptions
dot.edge('A', 'B', 'submits diagnostic form')
dot.edge('B', 'C', 'retrieves context &\nprompts ChatGPT')
dot.edge('C', 'D', 'sends request to\nOpenAI API')
dot.edge('D', 'C', 'returns generated response')
dot.edge('C', 'A', 'displays diagnosis in UI')


# Render the graph to a file and display it
file_path_with_flask = './imgs/AI_Driven_Car_Repair_Assistant_Architecture_Diagram_With_Flask.gv'
dot.render(file_path_with_flask, format='png', view=True)

file_path_with_flask + '.png'  # Return the path of the generated PNG file
