""" A script to update the counts of matches. """
import pandas as pd
import os

from jinja2 import Template 


MAPPED_FILE = "Mapping/Output/Mapped_files/SimaProv94-ecoinventEFv3.7.csv"
INPUTS_EI = "Mapping/Input/Flowlists/ecoinventEFv3.7.csv"
INPUTS_SP = "Mapping/Input/Flowlists/SimaProv9.4.csv"
STATUS_DEBUG = os.getenv('STATUS_DEBUG', True) 

def update_status_file(new_status:dict):
    """Load the status_update template and update the status file `status.md`.

    Args:
        new_status (dict): keys: matched_inputs, matched_outputs

    """
    with open('status_template.md') as template_f:
        template = Template(template_f.read())
    output = template.render(new_status)
    with open('status.md', "w+") as status_file:
        status_file.write(output)

    
def run():
    df_mapped = pd.read_csv(MAPPED_FILE)
    df_inputs_ei = pd.read_csv(INPUTS_EI)
    df_inputs_sp = pd.read_csv(INPUTS_SP)

    if STATUS_DEBUG:
        print(df_mapped.info())
        print(df_inputs_ei.info())
        print(df_inputs_sp.info())

    count_matched_inputs = 0
    count_matched_outputs= 0

    update_status_file({'matched_inputs':count_matched_inputs, 'matched_outputs':count_matched_outputs})

if __name__ == "__main__":
    run()
