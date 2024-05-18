import sys, os
import ollama
import argparse

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Utils.data_helper import load_df, get_section_dict
from Utils.constants import OLLAMA_SYS_PROMPT_PATH, OLLAMA_PROMPT_PATH, OLLAMA_PROMPT_NL_PATH

class OllamaSectioner():
    """
    This class creates a text sectioning object.
    """

    def __init__(self, model):
        # add parameters and model path
        self.model = model
        self.system_prompt, self.prompt = self.get_system_prompt()
        #self.example_text, self.example_output = self.get_example()
        pass

    def get_system_prompt(self):
        # Load the system prompt
        with open(OLLAMA_SYS_PROMPT_PATH, 'r', encoding='utf-8') as file:
            sys_prompt = file.read()

        with open(OLLAMA_PROMPT_NL_PATH, 'r', encoding='utf-8') as file:
            prompt = file.read()
        return sys_prompt, prompt

    def get_example(self):
        # Load the example
        with open('Sectioning/Ollama/example.txt', 'r', encoding='utf-8') as file:
            example = file.read()
        
        # Split into example text and example output
        examples = example.split('-----')
        example_sections = []
        for ex in examples:
            example_sections.extend(ex.split('---'))
        return [example_sections[0], example_sections[2]], [example_sections[1], example_sections[3]]

    def get_response(self, input_text):
        response = ollama.chat(model=self.model, keep_alive=0, options={'temperature': 0.0, 'seed': 42, "top_p": 0.0}, messages=[
            {
                'role': 'system',
                'content': self.system_prompt
            },
            {
                'role': 'user',
                'content': self.prompt + input_text
            },
        ])
        return response

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ollama sectioning')
    parser.add_argument('--input', default='', help='Pick the csv to load.')
    parser.add_argument('--model', choices=['phi2', 'phi3', 'gemma', 'wizardlm2', 'mistral', 'llama3', 'llama2'], help='Choose LLM')
    parser.add_argument('--temp', default=0.0, help='Sets the temperature.')
    parser.add_argument('--top_p',default=0.0, help='Sets the top p')
    args = parser.parse_args()

    segmenter = OllamaSectioner('llama3:instruct')
    #input_df = load_df(args.input)
    ex = """ 5. Anders dan verweerder acht het College het aannemelijk dat appellant kennelijk ook de bedoeling heeft gehad om subsidie voor een warmtepomp aan te vragen. De bijlagen die appellant bij de SEEH-aanvraag heeft meegestuurd, zien vrijwel allemaal op een warmtepomp. Uit de aanvraag hadden de beoordelaars van SEEH-aanvragen kunnen afleiden dat appellant niet alleen voor vloer- en gevelisolatie en een aantal aanvullende energiebesparende maatregelen subsidie wilde aanvragen, maar ook voor een warmtepomp. Het lag daarom op de weg van de beoordelaars van SEEH-aanvragen om niet alleen een beoordeling op grond van de SEEH te doen, maar ook – eventueel na het stellen van nadere vragen aan appellant – de aanvraag op grond van artikel 2:3, eerste lid, van de Awb onmiddellijk door te sturen naar de beoordelaars van ISDE-aanvragen. Dat de SEEH en de ISDE aan verschillende bestuursorganen zijn opgedragen, zoals verweerder naar voren brengt, maakt het voorgaande, gelet op het bepaalde in artikel 2:3, eerste lid, van de Awb, niet anders. Daar komt nog bij dat de beide regelingen feitelijk worden uitgevoerd door RVO. Het College stelt vast dat de aanvraag niet is doorgezonden en dat pas in augustus, toen de termijn voor de ISDE op grond van artikel 4.5.12, eerste lid, aanhef en onder f, van de Regeling al was verstreken, door de beoordelaar van de SEEH-aanvraag nadere vragen aan appellant zijn gesteld over zijn aanvraag. Appellant heeft die vragen direct beantwoord. Onder deze omstandigheden kan appellant niet worden tegengeworpen dat zijn ISDE-aanvraag te laat bij verweerder is ingediend. Verweerder moet de ISDE-aanvraag dan ook opnieuw in behandeling nemen, uitgaande van de datum van indiening van de SEEH-aanvraag.
"""
    response = segmenter.get_response(ex)
    print(response['message']['content'])
